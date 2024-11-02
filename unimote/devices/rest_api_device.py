import requests
from .base_device import NetworkDevice

class RESTAPIDevice(NetworkDevice):
    @staticmethod
    def discover():
        # Implement REST API discovery logic if applicable
        return []

    def __init__(self, ip):
        super().__init__(ip)
        self.base_url = f"http://{ip}/api"

    def get_info(self):
        response = requests.get(f"{self.base_url}/info")
        return response.json()

    def send_command(self, command):
        response = requests.post(f"{self.base_url}/command", json={"command": command})
        if response.status_code == 200:
            print("Command executed successfully.")
        else:
            print(f"Failed to execute command: {response.text}")

    def get_supported_commands(self):
        response = requests.get(f"{self.base_url}/commands")
        return response.json().get("commands", [])
