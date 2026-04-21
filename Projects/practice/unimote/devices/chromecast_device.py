from .base_device import NetworkDevice
import pychromecast

class ChromecastDevice(NetworkDevice):
    @staticmethod
    def discover():
        devices = pychromecast.get_chromecasts()
        return [ChromecastDevice(device.host) for device in devices]

    def __init__(self, ip):
        super().__init__(ip)
        self.device = pychromecast.Chromecast(ip)

    def get_info(self):
        return self.device.device

    def send_command(self, command):
        if command == "play":
            self.device.media_controller.play()
        elif command == "pause":
            self.device.media_controller.pause()
        else:
            print(f"Command '{command}' not supported by Chromecast.")

    def get_supported_commands(self):
        return ["play", "pause"]
