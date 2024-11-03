from wakeonlan import send_magic_packet
import paramiko
from .base_device import NetworkDevice

class ComputerDevice(NetworkDevice):
    @staticmethod
    def discover():
        # Discovery could be done by pinging a list of IPs or with custom logic
        print("Scanning for Computers...")
        return [ComputerDevice("192.168.1.101")]

    def __init__(self, ip, mac_address=None):
        super().__init__(ip)
        self.mac_address = mac_address

    def get_info(self):
        return f"Computer at {self.ip} (MAC: {self.mac_address})"

    def send_command(self, command):
        if command == "wake_on_lan" and self.mac_address:
            send_magic_packet(self.mac_address)
            return f"Sent Wake-on-LAN packet to {self.mac_address}"
        elif command.startswith("ssh:"):
            ssh_command = command.split(":", 1)[1]
            return self.execute_ssh_command(ssh_command)
        else:
            return "Unsupported command or missing MAC address"

    def execute_ssh_command(self, ssh_command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.ip, username="your_username", password="your_password")
            stdin, stdout, stderr = ssh.exec_command(ssh_command)
            return stdout.read().decode()
        except Exception as e:
            return f"SSH command failed: {e}"
        finally:
            ssh.close()

    def get_supported_commands(self):
        return ["wake_on_lan", "ssh:<command>"]
