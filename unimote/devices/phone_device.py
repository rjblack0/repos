import subprocess
from .base_device import NetworkDevice

class PhoneDevice(NetworkDevice):
    @staticmethod
    def discover():
        # This would scan the network or find devices with ADB enabled
        print("Scanning for Android phones...")
        return [PhoneDevice("192.168.1.102")]

    def __init__(self, ip):
        super().__init__(ip)

    def get_info(self):
        return f"Android Phone at {self.ip}"

    def send_command(self, command):
        if command == "adb_reboot":
            return self.adb_command("reboot")
        elif command.startswith("adb_shell:"):
            adb_cmd = command.split(":", 1)[1]
            return self.adb_command(f"shell {adb_cmd}")
        else:
            return "Unsupported command"

    def adb_command(self, adb_cmd):
        try:
            result = subprocess.run(
                f"adb connect {self.ip} && adb {adb_cmd}",
                shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return f"ADB command failed: {e.stderr.decode()}"

    def get_supported_commands(self):
        return ["adb_reboot", "adb_shell:<command>"]
