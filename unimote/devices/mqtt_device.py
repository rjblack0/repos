from .base_device import NetworkDevice
import paho.mqtt.client as mqtt

class MQTTDevice(NetworkDevice):
    @staticmethod
    def discover(broker_ip):
        return [MQTTDevice(broker_ip)]

    def __init__(self, ip):
        super().__init__(ip)
        self.client = mqtt.Client()
        self.client.connect(ip)

    def get_info(self):
        return f"MQTT Device connected to broker at {self.ip}"

    def send_command(self, command):
        if command == "publish_example":
            self.client.publish("home/device", "Example message")
        else:
            print(f"Command '{command}' not supported by MQTT Device.")

    def get_supported_commands(self):
        return ["publish_example"]
