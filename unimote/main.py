import sys
from menu import show_agreement, display_main_menu, show_instructions, scan_for_devices
from menu import prompt_for_ip, prompt_for_token  # Import prompt functions if needed
from devices import (
    RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice,
    BroadlinkDevice, ChromecastDevice, MQTTDevice, HomeAssistantDevice
)
from utils.discovery import discover_all_devices

def select_device(devices):
    """Prompt user to select a device from a list."""
    if not devices:
        print("No devices available.")
        return None

    print("\nSelect a Device to Control:")
    for idx, device in enumerate(devices, start=1):
        print(f"{idx}. {device.__class__.__name__} at {device.ip}")

    choice = input("Select a device by number: ").strip()
    try:
        choice_idx = int(choice) - 1
        if choice_idx < 0 or choice_idx >= len(devices):
            print("Invalid selection.")
            return None
        return devices[choice_idx]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def device_menu(device):
    """Display options for controlling the selected device."""
    while True:
        print("\nAvailable Commands:")
        print("1. Get Device Info")
        print("2. Send Command")
        print("q. Quit to Main Menu")
        option = input("Select an option: ").strip().lower()

        if option == '1':
            print("Device Info:", device.get_info())
        elif option == '2':
            print("Supported Commands:", device.get_supported_commands())
            command = input("Enter command: ").strip()
            device.send_command(command)
        elif option == 'q':
            break
        else:
            print("Invalid option. Please try again.")

def main():
    show_agreement()  # Display agreement before starting the main program

    while True:
        display_main_menu()
        option = input("Enter your choice: ").strip()
        if option == "0":
            print("Exiting... Goodbye!")
            sys.exit(0)
        elif option == "9":
            show_instructions()
        else:
            devices = scan_for_devices(option)
            if devices:
                selected_device = select_device(devices)
                if selected_device:
                    device_menu(selected_device)

if __name__ == "__main__":
    main()
