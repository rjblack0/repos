from .base_device import NetworkDevice
import requests

class HomeAssistantDevice(NetworkDevice):
    @staticmethod
    def discover(ip, token):
        return [HomeAssistantDevice(ip, token)]

    def __init__(self, ip, token):
        super().__init__(ip)
        self.base_url = f"http://{ip}:8123/api"
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_info(self):
        try:
            response = requests.get(f"{self.base_url}/states", headers=self.headers)
            response.raise_for_status()  # Check for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to get info from Home Assistant: {e}")
            return "Error fetching device info"

    def send_command(self, command):
        # Example to toggle a light entity
        if command == "toggle_light":
            data = {"entity_id": "light.living_room"}
            response = requests.post(f"{self.base_url}/services/light/toggle", headers=self.headers, json=data)
            print("Light toggled" if response.status_code == 200 else "Failed to toggle light")
        else:
            print(f"Command '{command}' not supported by Home Assistant Device.")

    def get_supported_commands(self):
        return ["toggle_light"]

