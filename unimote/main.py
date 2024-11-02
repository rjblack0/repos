from devices import RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice
from utils.discovery import discover_all_devices
from colorama import init

init(autoreset=True)

def main():
    devices = discover_all_devices()
    if not devices:
        print("No devices found on the network.")
        return

    print("Discovered Devices:")
    for idx, device in enumerate(devices, start=1):
        print(f"{idx}. {device.__class__.__name__} at {device.ip}")

    choice = int(input("Select a device by number: ")) - 1
    selected_device = devices[choice]

    while True:
        print("\nAvailable Commands:")
        print("1. Get Device Info")
        print("2. Send Command")
        print("q. Quit")
        option = input("Select an option: ").strip().lower()

        if option == '1':
            print("Device Info:", selected_device.get_info())
        elif option == '2':
            print("Supported Commands:", selected_device.get_supported_commands())
            command = input("Enter command: ").strip()
            selected_device.send_command(command)
        elif option == 'q':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
