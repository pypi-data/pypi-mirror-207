import asyncio
import logging
import re
from collections import OrderedDict

from enum import Enum, auto
from typing import Union, Tuple, Optional, Coroutine, Any, Dict

import aiohttp
from aiohttp import ClientTimeout
from renault_api.exceptions import RenaultException
from renault_api.kamereon.models import KamereonPersonResponse, KamereonPersonAccount, KamereonVehiclesResponse, \
    KamereonVehicleContract
from renault_api.models import BaseModel
from renault_api.renault_account import RenaultAccount

from renault_api.renault_client import RenaultClient
from renault_api.renault_vehicle import RenaultVehicle

from renault.excpetion import RenaultVehicleException


class RenaultVehicleClient:
    """
    Lightweight communication class for querying status info for variety of Renault vehicle models

    Uses renault-api as backend:
    https://github.com/hacf-fr/renault-api
    """
    class _StatusMapper:
        """
        Internal class for mapping status responses to a more convenient format (JSON parsable)
        containing the following data types:
            * dict
            * list
            * other 'primitive types' (e.g. int, float, str)
        """

        def __init__(self, response: list[BaseModel | list[KamereonVehicleContract]]):
            self.__response = response

        def map_status_response(self) -> OrderedDict[str, Any]:
            """
            Maps a Kamereon status response into a more straight-forward dict-based format (JSON parsable)
            containing the following data types:
                * dict
                * list
                * other 'primitive types' (e.g. int, float, str)

            :return: Dict containing mapped key/value pairs
            """
            mapped_response: Dict[str, Any] = {}

            for item in self.__response:
                mapped_name, mapped_value = self.__map_item(item)
                mapped_response[mapped_name] = mapped_value

            return self.__order_dict(mapped_response)

        def __map_item(self, item: BaseModel | list | dict | Any) -> Tuple[str, Any]:
            """
            Recursively maps a given item into a JSON parsable format consisting the following data type:
                * dict
                * list
                * 'primitive types'
            :param item: item to map
            :return: mapped item
            """

            if isinstance(item, BaseModel):
                return self.__map_model_item(item)

            elif isinstance(item, list):
                return self.__map_list_item(item)

            elif isinstance(item, dict):
                return self.__map_dict_item(item)

            elif self.__is_primitive(item):
                return item

            else:
                raise RenaultVehicleException(f"Error mapping response: Got item of unknown type {type(item)}")

        def __map_model_item(self, item: BaseModel) -> Tuple[str, Dict[str, Any]]:
            """
            Recursively maps a BaseModel element to into it's more convenient form
            :param item: item to map
            :return: mapped item
            """

            mapped_name = self.__convert_element_name_to_convenient_format(item.__class__.__name__)

            # content of a BaseModel object can be handled like a dict item
            mapped_content = self.__map_dict_item(item.__dict__)

            return mapped_name, mapped_content[1]

        def __map_list_item(self, item: list[BaseModel]) -> Tuple[str, list[Dict[str, Any]]]:
            """
            Recursively maps a list element into it's mor convenient form
            :param item: item to map
            :return: mapped item
            """
            if len(item) < 1:
                return "unknown", []

            mapped_name = self.__convert_element_name_to_convenient_format(item[0].__class__.__name__)

            mapped_content = []

            for list_element in item:
                list_element_name, list_element_content = self.__map_item(list_element)
                mapped_content.append(list_element_content)

            return mapped_name, mapped_content

        def __map_dict_item(self, item: dict[str, BaseModel]) -> Tuple[str, dict[str, Any]]:
            """
            Recursively maps a dict element into it's more convenient form
            :param item: item to map
            :return: mapped item
            """
            mapped_name = self.__convert_element_name_to_convenient_format(item.__class__.__name__)

            mapped_content: Dict[str, Any] = {}

            for element_name, element_value in item.items():

                if element_name in ['raw_data']:
                    continue

                element_name = self.__convert_element_name_to_convenient_format(element_name)

                # map value in case of 'non-primitive' type
                if not self.__is_primitive(element_value):
                    element_value = self.__map_item(element_value)[1]

                mapped_content[element_name] = element_value

            return mapped_name, mapped_content

        @classmethod
        def __convert_element_name_to_convenient_format(cls, name: str) -> str:
            """
            Internal method to convert a 'technical' element name into it's more convenient form
            :param name: name to convert
            :return: converted name
            """

            result = re.match(r'^(kamereon_vehicle_)?(.*)', cls.__convert_capwords_to_underscore(name))
            return result.group(2) if result else ""

        @staticmethod
        def __convert_capwords_to_underscore(name: str) -> str:
            """
            Internal method to convert a name in capwords notation to underscore notation
            :param name: name to convert
            :return: converted name
            """
            return re.sub(r'(?<=[a-z])[A-Z]|(?<!^)[A-Z](?=[a-z])', r"_\g<0>", name).lower()

        @staticmethod
        def __order_dict(dict_to_order: Dict[Any, Any]) -> OrderedDict[Any, Any]:
            """
            Takes a dictionary and creates an OrderedDict ordered by keys (ascending)

            :param dict_to_order: dict to order
            :return: OrderedDict
            """
            ordered_dict = OrderedDict()

            for key in sorted(dict_to_order.keys()):
                ordered_dict[key] = dict_to_order[key]

            return ordered_dict

        @staticmethod
        def __is_primitive(variable: Any) -> bool:
            """
            Returns if a given variable is one of a 'primitive' :type

            :param variable: variable to check
            :return:
            """
            return not hasattr(variable, '__dict__') \
                and not isinstance(variable, list) \
                and not isinstance(variable, dict)

    __vehicle: RenaultVehicle

    class StatusType(Enum):
        """
        Queryable status elements
        """
        BATTERY = auto()
        COCKPIT = auto()
        CAR_ADAPTER = auto()
        CHARGE_MODE = auto()
        CHARGE_SETTINGS = auto()
        CONTRACTS = auto()
        DETAILS = auto()
        HVAC_SETTING = auto()
        HVAC_STATUS = auto()
        LOCATION = auto()

    # predefined query selection: minimum
    STATUS_MINIMUM = (
        StatusType.CAR_ADAPTER,
        StatusType.COCKPIT,
    )

    # predefined query selection: battery only
    STATUS_BATTERY_ONLY = (
        StatusType.BATTERY,
    )

    # predefined query selection: full / all elements
    STATUS_FULL = (
        StatusType.BATTERY,
        StatusType.COCKPIT,
        StatusType.CAR_ADAPTER,
        StatusType.CHARGE_MODE,
        StatusType.CHARGE_SETTINGS,
        StatusType.CONTRACTS,
        StatusType.DETAILS,
        StatusType.HVAC_SETTING,
        StatusType.HVAC_STATUS,
        StatusType.LOCATION,
    )

    def __init__(self,
                 login_id: str,
                 password: str,
                 account_locale: str = "de_DE",
                 vin: Optional[str] = None,
                 backend_log_level: Union[int, str] = logging.INFO,
                 prepare_connection: bool = True,
                 timeout: float = 5.0) -> None:
        """
        Initialises connection to a vehicle

        :param login_id: Login id / E-Mail of "My Renault" account
        :param password: Password for "My Renault" account
        :param account_locale: Locale of the region for which the login_id (Renault account) is registered. Defaults
        to 'de_DE', which may work for most european countries. If unsure, use your specific locale
        :param vin: Select a specific vehicle by its VIN. Only needed if several vehicles are registered within account
        :param backend_log_level: Optional log level for renault-api backend. Defaults to logger.INFO
        :param prepare_connection: Establish connection (perform login) on instance creation. Defaults to True.
        Otherwise, connection is established on-the-fly when querying the vehicle.
        :param timeout: Timeout for requests to backend in seconds. Default 5.0
        """
        if login_id == "":
            raise ValueError("login_id needs to be set")

        if password == "":
            raise ValueError("password needs to be set")

        self.__login_id = login_id
        self.__password = password
        self.__account_locale = account_locale
        self.__vin = vin
        self.__timeout = timeout

        if not logging.getLogger("renault_api").hasHandlers():
            logging.basicConfig()

        logging.getLogger("renault_api").setLevel(backend_log_level)

        self.__initialize_backend()

        if prepare_connection:
            self.__establish_vehicle_connection()

    def __initialize_backend(self) -> None:
        """
        Internal method that brings preparations in place for underlying renault-api client (backend) and its async
        context

        :return:
        """
        # save event loop for further usage with later async calls
        self.__async_loop = asyncio.get_event_loop_policy().get_event_loop()

        # prepare AIOHTTP client session (automatically uses the asyncio event loop of the current thread)
        self.__aiohttp_client_session = aiohttp.ClientSession(timeout=ClientTimeout(total=self.__timeout))

        self.__renault_client = RenaultClient(websession=self.__aiohttp_client_session, locale=self.__account_locale)

    def __run_async(self, coroutine: Coroutine) -> Any:
        """
        Internal method to run a coroutine using the instance's async context

        :return:
        """
        return self.__async_loop.run_until_complete(coroutine)

    def __establish_vehicle_connection(self) -> None:
        """
        Establishes a connection to vehicle backend:
        Logs in into account, selects person and vehicle
        :return:
        """
        # perform login at Renault backend
        try:
            self.__run_async(self.__renault_client.session.login(self.__login_id, self.__password))
        except RenaultException as e:
            raise RenaultVehicleException(f"Got error from backend 'renault-api': {str(e)}") from e

        # get account
        account = self.__get_unique_account_from_renault_client(self.__renault_client)

        # get vehicle (by VIN if given, otherwise search for it)
        vehicle = self.__get_unique_vehicle_from_account(account)

        self.__vehicle = vehicle

    def __get_unique_account_from_renault_client(self, renault_client: RenaultClient) -> RenaultAccount:
        """
        Returns the account object from the RenaultClient. Raises an Exception, if more than one account
        is available within the account (which should not happen)

        :param renault_client: RenaultClient
        :return: selected RenaultAccount
        """
        try:
            person: KamereonPersonResponse = self.__run_async(renault_client.session.get_person())
        except RenaultException as e:
            raise RenaultVehicleException(f"Got error from backend 'renault-api': {str(e)}") from e

        account_id = self.__get_unique_account_id(person.accounts)

        if not account_id:
            raise RenaultVehicleException(f"Login '{self.__login_id}' has associated more than 1 Renault accounts. "
                                          f"Cannot proceed. (This should not happen, please report a bug if you feel "
                                          f"this is an error)")

        account: RenaultAccount = self.__run_async(renault_client.get_api_account(account_id))
        return account

    @staticmethod
    def __get_unique_account_id(accounts: Optional[list[KamereonPersonAccount]]) -> str | None:
        """
        Searches for a single account (status 'ACTIVE', type 'MYRENAULT') and returns its id
        :param accounts:
        :return: account_id if exactly 1 account could be found, otherwise None
        """

        if not accounts:
            return None

        active_accounts = [account for account in accounts
                           if account.accountStatus == "ACTIVE"
                           and account.accountType == "MYRENAULT"]

        return active_accounts[0].accountId if len(accounts) == 1 else None

    def __get_unique_vehicle_from_account(self, account: RenaultAccount) -> RenaultVehicle:
        """
        Retrieves a single and unique vehicle from a Renault account.

        If a VIN is specified for this class instance, the VIN gets retrieved, otherwise the vehicle is selected
        automatically

        :param account: RenaultAccount
        :return: selected RenaultVehicle
        """
        try:
            vehicles: KamereonVehiclesResponse = self.__run_async(account.get_vehicles())
        except RenaultException as e:
            raise RenaultVehicleException(f"Got error from backend 'renault-api': {str(e)}") from e

        # check for wish for a specific VIN
        if self.__vin:
            if not vehicles.vehicleLinks or len(
                    [vehicleLink.vin for vehicleLink in vehicles.vehicleLinks if vehicleLink.vin == self.__vin]) == 0:
                raise RenaultVehicleException(
                    f"No vehicle with given VIN '{self.__vin}' available within Renault account"
                    f" Available vehicles: {self.__get_vehicle_list_from_vehicles(vehicles)}")

            vehicle_id = self.__vin

        # not VIN wished, retrieve VIN from account
        else:
            vehicle_id = self.__get_unique_vehicle_id(vehicles)

            if not vehicle_id:
                vehicle_list = self.__get_vehicle_list_from_vehicles(vehicles)

                error_message = f"Could not select vehicle ({len(vehicle_list)} vehicles available."

                if len(vehicle_list) > 1:
                    error_message += " Please provide VIN of vehicle to select to class constructor."
                    error_message += f" Available vehicles: {vehicle_list}"

                raise RenaultVehicleException(error_message)

        # we have a valid VIN, retrieve vehicle object
        vehicle: RenaultVehicle = self.__run_async(account.get_api_vehicle(vehicle_id))
        return vehicle

    @staticmethod
    def __get_unique_vehicle_id(vehicles: KamereonVehiclesResponse) -> str:
        """
        Searches for a single VIN and returns it
        :param vehicles: object containing vehicles of a Renault account
        :return: VIN if exactly 1 vehicle could be found, otherwise None
        """
        if not vehicles.vehicleLinks or len(vehicles.vehicleLinks) != 1:
            return ""

        if not vehicles.vehicleLinks[0].vin:
            return ""

        return vehicles.vehicleLinks[0].vin

    @staticmethod
    def __get_vehicle_list_from_vehicles(vehicles: KamereonVehiclesResponse) -> list[dict[str, str]]:
        """
        Creates a list containing data for each vehicle within a Renault account

        Tuple for each vehicle:
            * model_name
            * vin
        :param vehicles: object containing vehicles of a Renault account
        :return:
        """
        if not vehicles.vehicleLinks:
            return []

        vehicle_list = []

        for vehicle_link in vehicles.vehicleLinks:

            vin = vehicle_link.vin if vehicle_link.vin else "unknown vin"

            if vehicle_link.vehicleDetails \
                    and vehicle_link.vehicleDetails.model \
                    and vehicle_link.vehicleDetails.model.label:

                model = vehicle_link.vehicleDetails.model.label

            else:
                model = "unknown model"

            vehicle_list.append({
                "model": model,
                "vin": vin
            })

        return vehicle_list

    def get_status(self, status_type: StatusType | Tuple[StatusType, ...] = STATUS_MINIMUM) \
            -> OrderedDict[str, Any]:
        """
        Retrieves and returns vehicle status

        :param status_type: Single StatusType element or tuple of StatusType elements to request from backend.
            Several predefined Tuples are available as class variable.
            If not set, RenaultVehicleClient.STATUS_MINIMUM is used as selection
        :return:
        """
        if not self.__vehicle:
            self.__establish_vehicle_connection()

        try:
            response = self.__run_async(self.__request_status_elements(status_type))

        except RenaultException as e:
            raise RenaultVehicleException(f"Got error from backend 'renault-api': {str(e)}") from e
        return self._StatusMapper(response).map_status_response()

    async def __request_status_elements(self, status_type: StatusType | Tuple[StatusType, ...]) \
            -> tuple[BaseModel | list[KamereonVehicleContract], ...]:
        """
        Returns the given status information by performing parallel calls to the function for each requested
        StatusType
        :param status_type: :return:
        """
        if type(status_type) is RenaultVehicleClient.StatusType:
            status_type = (status_type, )

        request_list = self.__create_status_requests(status_type)  # type: ignore
        response_list = await asyncio.gather(*request_list)

        return response_list

    def __create_status_requests(self, status_type_tuple: Tuple[StatusType, ...]) -> list[Coroutine]:
        """
        Creates and returns the coroutines for the requested StatusType tuple
        :param status_type_tuple: requested status types
        :return: list of coroutines
        """
        request_list: list[Coroutine] = []

        for status_element in status_type_tuple:

            match status_element:
                case RenaultVehicleClient.StatusType.BATTERY:
                    request_list.append(self.__vehicle.get_battery_status())

                case RenaultVehicleClient.StatusType.CAR_ADAPTER:
                    request_list.append(self.__vehicle.get_car_adapter())

                case RenaultVehicleClient.StatusType.CHARGE_MODE:
                    request_list.append(self.__vehicle.get_charge_mode())

                case RenaultVehicleClient.StatusType.CHARGE_SETTINGS:
                    request_list.append(self.__vehicle.get_charging_settings())

                case RenaultVehicleClient.StatusType.COCKPIT:
                    request_list.append(self.__vehicle.get_cockpit())

                case RenaultVehicleClient.StatusType.CONTRACTS:
                    request_list.append(self.__vehicle.get_contracts())

                case RenaultVehicleClient.StatusType.DETAILS:
                    request_list.append(self.__vehicle.get_details())

                case RenaultVehicleClient.StatusType.HVAC_SETTING:
                    request_list.append(self.__vehicle.get_hvac_settings())

                case RenaultVehicleClient.StatusType.HVAC_STATUS:
                    request_list.append(self.__vehicle.get_hvac_status())

                case RenaultVehicleClient.StatusType.LOCATION:
                    request_list.append(self.__vehicle.get_location())

                case _:
                    raise RenaultVehicleException(f"Unknown status of type {status_element} requested")

        return request_list
