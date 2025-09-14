## Use this cover to implement new devices

from abc import ABC, abstractmethod

class NetworkDevice(ABC):
    def __init__(self, ip):
        self.ip = ip

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def send_command(self, command):
        pass

    @staticmethod
    @abstractmethod
    def discover():
        pass

    @abstractmethod
    def get_supported_commands(self):
        pass
