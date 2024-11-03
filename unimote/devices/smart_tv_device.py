import requests
from .base_device import NetworkDevice

class SmartTVDevice(NetworkDevice):
    @staticmethod
    def discover():
        # Example for discovering LG or Samsung TVs; adjust as needed
        print("Scanning for Smart TVs...")
        return [SmartTVDevice("192.168.1.100")]  # Replace with real discovery

    def __init__(self, ip):
        super().__init__(ip)
        self.api_url = f"http://{ip}:8001/api/v2/"

    def get_info(self):
        try:
            response = requests.get(f"{self.api_url}/device-info")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return f"Error fetching TV info: {e}"

    def send_command(self, command):
        # Example command for turning the TV on/off
        if command == "toggle_power":
            response = requests.post(f"{self.api_url}/power")
            return "Power toggled" if response.ok else "Failed to toggle power"
        else:
            return f"Unsupported command: {command}"

    def get_supported_commands(self):
        return ["toggle_power"]
