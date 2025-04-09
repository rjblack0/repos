from .base_device import NetworkDevice
from roku import Roku

class RokuDevice(NetworkDevice):
    @staticmethod
    def discover():
        return [RokuDevice(device.host) for device in Roku.discover(timeout=5)]

    def __init__(self, ip):
        super().__init__(ip)
        self.device = Roku(ip)

    def get_info(self):
        return self.device.info

    def send_command(self, command):
        try:
            getattr(self.device, command)()
        except AttributeError:
            print(f"Command '{command}' not supported by Roku.")

    def get_supported_commands(self):
        return ["home", "power", "volume_up", "volume_down", "select"]
