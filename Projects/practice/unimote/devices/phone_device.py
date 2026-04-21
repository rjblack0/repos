# devices/phone_device.py

from .base_device import NetworkDevice

class PhoneDevice(NetworkDevice):
    @staticmethod
    def discover():
        # Replace with actual discovery logic for phones
        print("Scanning for Phones...")
        return [PhoneDevice("192.168.1.102")]

    def __init__(self, ip):
        super().__init__(ip)

    def get_info(self):
        # Replace with actual info retrieval
        return f"Phone at {self.ip}"

    def send_command(self, command):
        # Example command for sending notifications
        if command == "send_notification":
            return "Notification sent to phone"
        return f"Unsupported command: {command}"

    def get_supported_commands(self):
        return ["send_notification"]
