from onvif import ONVIFCamera
from .base_device import NetworkDevice

class IPCameraDevice(NetworkDevice):
    @staticmethod
    def discover():
        # Custom discovery logic for ONVIF cameras
        print("Scanning for IP Cameras...")
        return [IPCameraDevice("192.168.1.103")]

    def __init__(self, ip):
        super().__init__(ip)
        self.camera = ONVIFCamera(ip, 80, "username", "password")

    def get_info(self):
        try:
            return self.camera.devicemgmt.GetDeviceInformation()
        except Exception as e:
            return f"Failed to get camera info: {e}"

    def send_command(self, command):
        if command == "move_left":
            return self.move_camera("left")
        elif command == "move_right":
            return self.move_camera("right")
        else:
            return "Unsupported command"

    def move_camera(self, direction):
        # Example for moving the camera; may vary by model
        ptz = self.camera.create_ptz_service()
        if direction == "left":
            ptz.ContinuousMove({"PanTilt": {"x": -1.0}})
            return "Camera moving left"
        elif direction == "right":
            ptz.ContinuousMove({"PanTilt": {"x": 1.0}})
            return "Camera moving right"

    def get_supported_commands(self):
        return ["move_left", "move_right"]
