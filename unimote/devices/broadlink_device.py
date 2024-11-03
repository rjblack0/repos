from .base_device import NetworkDevice
import broadlink

class BroadlinkDevice(NetworkDevice):
    @staticmethod
    def discover():
        return [BroadlinkDevice(device.host[0]) for device in broadlink.discover(timeout=5)]

    def __init__(self, ip):
        super().__init__(ip)
        self.device = broadlink.gendevice(0x2737, (ip, 80), "mac address")  # Replace with correct device type & MAC

    def get_info(self):
        return f"Broadlink Device at {self.ip}"

    def send_command(self, command):
        # Example: Sending a power on/off command
        if command == "power_on":
            self.device.auth()
            self.device.set_power(True)
        elif command == "power_off":
            self.device.auth()
            self.device.set_power(False)
        else:
            print(f"Command '{command}' not supported by Broadlink.")

    def get_supported_commands(self):
        return ["power_on", "power_off"]
