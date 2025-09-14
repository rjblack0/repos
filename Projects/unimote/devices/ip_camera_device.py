# devices/ip_camera_device.py

from .base_device import NetworkDevice

class IPCameraDevice(NetworkDevice):
    @staticmethod
    def discover():
        # Replace with actual discovery logic for IP cameras
        print("Scanning for IP Cameras...")
        return [IPCameraDevice("192.168.1.103")]

    def __init__(self, ip):
        super().__init__(ip)

    def get_info(self):
        # Replace with actual info retrieval
        return f"IP Camera at {self.ip}"

    def send_command(self, command):
        # Example command to capture an image or video
        if command == "capture_image":
            return "Captured image from IP Camera"
        return f"Unsupported command: {command}"

    def get_supported_commands(self):
        return ["capture_image"]
