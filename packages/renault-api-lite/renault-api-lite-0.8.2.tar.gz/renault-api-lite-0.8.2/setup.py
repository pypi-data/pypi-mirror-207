from setuptools import setup  # type: ignore

# read the contents of README.md file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='renault-api-lite',
    version='0.8.2',
    packages=['renault'],
    url='https://github.com/bkogler/renault-api-lite',
    license='MIT',
    author='Bernhard Kogler',
    author_email='bernhard.kogler@supersonnig.org',
    description='Lightweight Python API for querying status info for a variety of Renault vehicle models',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="Renault Z.E. ZOE Twingo Megane Kangoo Electric vehicle EV status API",
    python_requires='>=3.10',
    install_requires=[
        'renault-api>=0.1.13'
    ]
)
