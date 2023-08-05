# [renault API (lite)](https://github.com/bkogler/renault-api-lite)
Lightweight Python API for querying status info for a variety of Renault vehicle models

# Features
Conveniently read status info for Renault vehicles (e.g. EVs), including:

* battery status (level, autonomy, plug status, temperature, ...)
* charging configuration / charge schedule
* fuel autonomy (for combustion vehicles)
* HVAC / pre-conditioning status
* GPS location

# Installation
`pip install renault-api-lite`

# Usage Examples

## Query battery status
````python
from renault import RenaultVehicleClient

car = RenaultVehicleClient(
    login_id="Your E-Mail", password="Your password", # --> change to your credentials
    account_locale="de_DE" # --> optional
)

# get battery status
status = car.get_status(car.STATUS_BATTERY_ONLY)
````
#### Hint: Pretty Print Status
````python
import json

print(json.dumps(status, indent=4))
````
````
{
    "battery_status_data": {
        "timestamp": "2022-08-145T07:24:12Z",
        "battery_level": 90,
        "battery_temperature": 25,
        "battery_autonomy": 207,
        "battery_capacity": 0,
        "battery_available_energy": 20,
        "plug_status": 0,
        "charging_status": -1.1,
        "charging_remaining_rime": 10,
        "charging_instantaneous_power": 0.0
    }
}
````

## Query custom data selection (battery and cockpit data)
````python
# get battery status, cockpit data
status = car.get_status((
    car.StatusType.BATTERY,
    car.StatusType.COCKPIT,
))
````
#### Hint: Pretty Print Status
````python
import json

print(json.dumps(status, indent=4))
````
````
{
    "battery_status_data": {
        "timestamp": "2022-08-145T07:24:12Z",
        "battery_level": 90,
        "battery_temperature": 25,
        "battery_autonomy": 207,
        "battery_capacity": 0,
        "battery_available_energy": 20,
        "plug_status": 0,
        "charging_status": -1.1,
        "charging_remaining_rime": 10,
        "charging_instantaneous_power": 0.0
    },
    "cockpit_data": {
        "fuel_autonomy": null,
        "fuel_quantity": null,
        "total_mileage": 1234.22
    }
}
````

# Disclaimer
This project is not affiliated with, endorsed by, or connected to Renault. I accept no responsibility for any consequences, intended or accidental, as a result of interacting with Renault's API using this project.

# Credits
This project is based on [hacf-fr's renault-api](https://github.com/hacf-fr/renault-api) for Python

# Links
[renault-api-lite GitHub repository](https://github.com/bkogler/renault-api-lite)

[renault-api-lite on PyPi](https://pypi.org/project/renault-api-lite/)

[hacf-fr's renault-api](https://github.com/hacf-fr/renault-api) 
