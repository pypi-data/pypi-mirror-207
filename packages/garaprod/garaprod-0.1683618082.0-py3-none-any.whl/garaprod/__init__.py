import asyncio
import time
import os
import signal
import json
import sys
import threading
import traceback
# import garaprod.version as version
import argparse
import binascii
import subprocess
import msgpack
import shutil
import esptool
from dataclasses import dataclass, asdict, field


import requests
from enum import Enum
from termcolor import colored

import colorama
colorama.init()


# try:
#     import requests
#     req = requests.get('https://pypi.org/pypi/garaprod/json')
#     package_info = req.json()
#     latest_version = package_info['info']['version']
#     if latest_version != version.version:
#         print("Warning: Please update to latest version of this library")
# except Exception as err:
#     # print(err)
#     pass

# print('Running versions', version.version)



PYTHON = sys.executable
ESPTOOL = f'"{PYTHON}" "{esptool.__file__}"'
print('python_path', colored(PYTHON, 'yellow'))


def cmd(s):
    print('Run: ', colored(s, 'yellow'))
    return s


class Board(Enum):
    # GCP: str = 'GRobot Creator Plus'
    # GCF: str = 'GRobot Creator (No AI/IoT)'
    # IOT: str = 'GRobot IoT Board'
    CREATOR_PLUS: str = 'PLUS'
    CREATOR_LITE: str = 'LITE'
    CREATOR_IOT : str = 'IOT'
    
    def __str__(self):
        return self.value
    


@dataclass
class BuildOption:
    board: Board = None
    mac: str = colored('not_defined', 'red')
    port: str = colored('not_defined', 'red')
    nostub: bool = False
    # branchs: list = None
    tag: str = None
    imei: str = None

    # send back from server
    built: dict = field(default_factory=dict)
    
    
def get_mac(opts):
    output = subprocess.getoutput(
        cmd(f'{ESPTOOL} -p {opts.port} {" --no-stub " if opts.nostub else " "} read_mac')
    )
    print(colored(output, 'magenta'))
    for line in output.splitlines():
        if line.startswith('MAC'):
            mac = line.split(' ')[-1]
            break
    else:
        raise Exception("Can't read the MAC Address of this device, try reconnect")
    
    mac = mac.split(':')
    mac = bytes([int(f'0x{ids}', 16) for ids in mac])
    mac = binascii.b2a_base64(mac).strip().decode('utf8')
    opts.mac = mac
    print('get_mac -> ', colored(mac, 'magenta'))
    
    return mac

def query_firmware_version(opts):
    import requests

def get_verification():
    return None

    
    
def get_branch(opts):
    req = requests.get('https://api.garastem.com/api/v1/public/list_firmware')
    print(req.content)
    # opts.branches = json.loads(req.content)
    # print('branches', opts.branchs)
    
        
    
    
def build_firmware(opts):
    params = dict(
        build_options = asdict(opts),
        verification = get_verification()
    )
    print('Options', params)
    print(
        '\nDownloading ......\n'
    )
    req = requests.post('https://api.garastem.com/api/v1/public/build_firmware', 
        data = msgpack.dumps(params)
    )
    print('Fimware Request -> ', req)
    response = msgpack.loads(req.content)
    return response


def program_device(opt: BuildOption):
    # read the elf specifier
    # read the result
    path = os.path.join("image", 'dist')
    
    try:
        shutil.rmtree(path)
    except:
        pass
    os.makedirs(path, exist_ok=True)
    
    if opt.built is None:
        raise RuntimeError()

    print(opt.built.keys())
    
    opt.built['partitions'] = opt.built.get(b'partitions')
    if len(opt.built['partitions']) == 0:
        raise RuntimeError("No Partitions received")
    
    for partition in opt.built['partitions']:
        print('PARTITION', partition['file'], str(partition['offset']), len(partition['data']))
        with open(os.path.join(path, partition['file']), 'wb') as f:
            f.write(partition['data'])
        
    partition_params = ' '.join([
        f'{p["offset"]} {os.path.join(path, p["file"])}' for p in opt.built['partitions']
    ])
    os.system(
        cmd(f'{ESPTOOL}  -p {opt.port} -b 460800 --before default_reset --after hard_reset --chip auto {"--no-stub" if opt.nostub else ""} write_flash --flash_mode dio --flash_size=keep {partition_params}'))


opt = BuildOption()    
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--board', type=Board, choices=list(Board), required=True, help='Select board type')
parser.add_argument('-p', '--port', help="Select the COM port (COM* , /dev/tty/****)", required=True)
parser.add_argument('-t', '--tag', type=str, help="Firmware tag: (dev)",default='dev')
parser.add_argument('-i', '--imei', type=str, help="IMEI code",default=None)

parsed = parser.parse_args()
opt.board = parsed.board.value
opt.port = parsed.port
opt.tag = parsed.tag

if parsed.board == Board.CREATOR_PLUS:
    opt.nostub=True

if opt.imei is None:
    print(colored('IMEI is not DEFINED !', 'red'))



get_mac(opt)
get_branch(opt)


print('======== Build Option =========')
for k, v in asdict(opt).items():
    print(k, colored(v, 'yellow'), sep='\t')
print()



opt.built = build_firmware(opt)
program_device(opt)

