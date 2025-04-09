from .base_device import NetworkDevice
from pyHS100 import Discover, SmartPlug

class TPLinkDevice(NetworkDevice):
    @staticmethod
    def discover():
        return [TPLinkDevice(ip) for ip, dev in Discover.discover().items() if isinstance(dev, SmartPlug)]

    def __init__(self, ip):
        super().__init__(ip)
        self.device = SmartPlug(ip)

    def get_info(self):
        return self.device.sys_info

    def send_command(self, command):
        if command == "turn_on":
            self.device.turn_on()
        elif command == "turn_off":
            self.device.turn_off()
        else:
            print(f"Command '{command}' not supported by TP-Link Smart Plug.")

    def get_supported_commands(self):
        return ["turn_on", "turn_off"]
