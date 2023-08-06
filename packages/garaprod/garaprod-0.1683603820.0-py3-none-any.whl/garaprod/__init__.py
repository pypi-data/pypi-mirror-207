import asyncio
import time
import bleak
import os
import signal
import sys
import threading
import traceback
import garaprod.version as version
import argparse



from termcolor import colored




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
