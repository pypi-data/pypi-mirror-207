import asyncio
import time
import bleak
import os
import signal
import sys
import threading
import traceback
import garastem.version as version

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
    req = requests.get('https://pypi.org/pypi/garastem/json')
    package_info = req.json()
    latest_version = package_info['info']['version']
    if latest_version != version.version:
        print("Warning: Please update to latest version of this library")
except Exception as err:
    # print(err)
    pass

print('Running versions', version.version)

#! Coroutine setup, do not touch this magic block please
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
def create_task(coro):
    global loop
    loop.create_task(coro)
    if not hasattr(create_task, 'thread_started'):
        create_task.thread_started = True
        threading.Thread(target=loop.run_forever, daemon=True).start()
        
def exit():
    if sys.platform == 'darwin':
        os.kill(os.getpid(), signal.SIGINT)
    elif sys.platform == 'win32':
        os._exit()
    
class Port:
    def __init__(self, device: 'GRobot', id: int):
        self.device = device
        self.id = id
        self.module = None
    def connect(self, module):
        self.module = module
        print(f'gr/ connect port {self} with {module}')
    def symbol(self):
        if self.module is None:
            return 'f'
        else:
            return self.module.symbol

class ModuleButton:
    symbol = 'B'
    def __init__(self, port: Port):
        self.port = port
        self.port.connect(self)
import string
        
        
        
        

class GRobot:
    discovered_devices = {}
    def __init__(self, name):
        self.name = name
        self.device = None
        self.client = None
        self.send_queues = []
        self.is_connected = False
        self.is_ready = False
        self.recvbuff = ''
        create_task(self.routine())
        
        self.PORT1 = Port(self, 0)
        self.PORT2 = Port(self, 1)
        self.PORT3 = Port(self, 2)
        self.PORT4 = Port(self, 3)
        self.PORT5 = Port(self, 4)
        self.PORT6 = Port(self, 5)
        
        self.ports = [
            self.PORT1,
            self.PORT2,
            self.PORT3,
            self.PORT4,
            self.PORT5,
            self.PORT6,
        ]
        
    
        
    async def declare_modules(self):
        # wait 1 seconds for all the modules to be declare ?
        # only 100ms for this
        print('gs/ declaring modules')
        await asyncio.sleep(1)
        # write the string
        # self.write('*G#\r\n', priority=True, expect="G")
        await asyncio.sleep(1)
        modulestring = ''.join([port.symbol() for port in self.ports])
        setupstring = '*' + modulestring + '#\r\n'
        self.write('*G#' + setupstring, priority=True, expect="ffffff")
        # await asyncio.sleep(5)
        print('reveived', self.recvbuff)
        self.is_ready = True
        
        # wait for confirm
    async def routine(self):
        # start connect first
        try:
            while True:
                await asyncio.sleep(0.01)
                # print('ROUTINE', end = '')
                if not self.is_connected:
                    try:
                        device = await BleakScanner.find_device_by_filter(self._handle_filter)
                    except:
                        print(colored("Please turn on Bluetooth first", 'red'))
                        continue
                    if device is None:
                        print(f'gr/ still finding {self.name}')
                        continue
                    self.device = device
                    self.client = BleakClient(
                        self.device,
                        disconnected_callback=self._handle_disconnect
                    )
                    
                    await self.client.connect()
                    print(f'gr/ {self.name} connected')
                    await self.client.start_notify(UART_RX_CHAR_UUID, self._handle_rx)
                    create_task(self.declare_modules())
                    self.is_connected = True
                    print("now wait")
                    
                    
                else:
                    # Process the out data
                    print('.', end = '')
                    while len(self.send_queues):
                        send = self.send_queues.pop(0)
                        print('gs/ [{}] written\t'.format(len(self.send_queues)), colored(send.strip(), 'yellow'))
                        send = bytes(send, 'utf8')
                        await self.client.write_gatt_char(UART_RX_CHAR_UUID, send)
        except Exception as err:
            traceback.print_exc()
            global killed
            killed = True
            exit()
    
                
    def write(self, data, priority=False, expect=None):
        while not self.is_ready and priority == False:
            time.sleep(0.01)
        self.recvbuff = ''
        print('write queue', data)
        self.send_queues.append(data)
        time.sleep(0.01)
        if expect:
            future = time.time() + 3
            while time.time() < future:
                print('waiting for response of {} in {}'.format(expect,self.recvbuff))
                if expect in self.recvbuff:
                    self.recvbuff = ''
                    print('done')
                    return True
                time.sleep(1)
            raise RuntimeError('This board is not in Yellow Mode ?')
                
        # if len(self.send_queues) > 100:
        #     print('gr/ overflowed send buffer, slow down')
        #     while len(self.send_queues) > 10:
        #         time.sleep(0.01)
            
    def _handle_rx(self, _: BleakGATTCharacteristic, data: bytearray):
        # print('gr/ data:', data)
        # pipe data
        try:
            self.recvbuff += data.decode('utf8')
            self.recvbuff = self.recvbuff.replace('\r\n', '\n').replace('\n', '')
            # print("DATA", self.recvbuff)
            print("gs/ received\t", colored(self.recvbuff, 'magenta'))
            
        except:
            pass
    
    def _handle_disconnect(self, _: BleakClient):
        self.is_connected = False
        print("gr/ device disconnected, retrying...")
    
    def _handle_filter(self, device: BLEDevice, adv: AdvertisementData):
        if device.name == self.name:
            print('Device Found: ', self.name)
            return True
        if device.name is not None:
            if device.name not in GRobot.discovered_devices:
                GRobot.discovered_devices[device.name] = None
                print('Found: ', device.name)
        return False
    
    def set_buzzer(self, state):
        if state:
            self.write('*B1#\r\n')
        else:
            self.write('*B0#\r\n')
    
    def stop(self):
        self.write('*M0|#\r\n')
    
    def move_forward(self, speed: float):
        speed = int(speed)
        self.write(f"M1|{'1' if speed < 0 else ''}{abs(speed)}#\r\n")
    
    def move_backward(self, speed: float):
        speed = int(speed)
        self.write(f"M2|{'1' if speed < 0 else ''}{abs(speed)}#\r\n")
    
    def rotate_left(self, speed: float):
        speed = int(speed)
        self.write(f"M3|{'1' if speed < 0 else ''}{abs(speed)}#\r\n")
    
    def rotate_right(self, speed: float):
        speed = int(speed)
        self.write(f"M4|{'1' if speed < 0 else ''}{abs(speed)}#\r\n")

    def set_motor(self, motor: int, speed: float):
        speed = int(speed)
        self.write(f"M{'5' if motor == 0 else '6'}|{'1' if speed < 0 else ''}{abs(speed)}#\r\n")
    
    def digitalRead(self, port):
        pass
    
    def digitalWrite(self, port):
        pass
    
    def analogRead(self, port):
        pass
    
# from enum import Enum
# class Button(Enum):
#     LEFT = 0
#     RIGHT = 1
#     PRESSED = 99
#     RELEASE = 100
#     PRESSED_ONE_TIME = 1
#     PRESSED_TWO_TIMES = 2
#     PRESSED_THREE_TIMES = 3
#     PRESSED_FOUR_TIMES = 4
#     PRESSED_FIVE_TIMES = 5
    
    
    
#     def __init__(self, port: Port):
#         self.port = port
    
#     def is_pressed(self, button) -> bool:
#         pass
    
#     def read_position(self) -> int:
#         pass
    
#     def was(self, button: int, event: int):
#         return True
#         pass
    
import esptool
PYTHON = sys.executable
ESPTOOL = esptool.__file__

    


__all__ = [
    'GRobot'
]