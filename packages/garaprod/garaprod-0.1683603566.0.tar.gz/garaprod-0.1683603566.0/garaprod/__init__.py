import asyncio
import time
import bleak
import os
import signal
import sys
import threading
import traceback
import garastem.version as version
import argparse


from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

from termcolor import colored
UART_SERVICE_UUID = "0000ffe0-0000-1000-8000-00805f9b34fb"
UART_RX_CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
killed = False

try:
    import requests
    req = requests.get('https://pypi.org/pypi/garaprod/json')
    package_info = req.json()
    latest_version = package_info['info']['version']
    if latest_version != version.version:
        print("Warning: Please update to latest version of this library")
except Exception as err:
    # print(err)
    pass

print('Running versions', version.version)
