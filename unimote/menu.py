# menu.py

import sys
from devices import (
    RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice,
    BroadlinkDevice, ChromecastDevice, MQTTDevice, HomeAssistantDevice,
    SmartTVDevice, ComputerDevice, PhoneDevice, IPCameraDevice
)
from utils.discovery import discover_all_devices
from colorama import init

init(autoreset=True)

def show_agreement():
    """Display agreement and prompt the user to agree."""
    print("Welcome to Unimote - Network Device Control")
    print("This program is for home use only. By proceeding, you agree that:")
    print("- This software should only be used on networks you own or have explicit permission to access.")
    print("- Unauthorized network scanning or device control may violate laws or policies.")
    
    agreement = input("Do you agree to use this software responsibly? (y/n): ").strip().lower()
    if agreement != 'y':
        print("You did not agree to the terms. Exiting...")
        sys.exit(0)

def display_main_menu():
    """Display the main menu options to the user."""
    print("\nMain Menu - Please select an option:")
    print("1. Discover all devices on network")
    print("2. Scan for Smart Devices")
    print("3. Scan for Computers")
    print("4. Scan for Phones")
    print("9. Instructions")
    print("0. Quit")

def display_smart_devices_menu():
    """Display the smart devices submenu options."""
    print("\nSmart Devices - Please select a device type to scan:")
    print("1. Scan for Roku devices")
    print("2. Scan for TP-Link devices")
    print("3. Scan for Printers (SNMP)")
    print("4. Scan for Broadlink devices")
    print("5. Scan for Chromecast devices")
    print("6. Scan for MQTT devices")
    print("7. Scan for Home Assistant devices")
    print("8. Scan for Smart TVs")
    print("9. Return to Main Menu")

def show_instructions():
    """Display instructions for setting up the program."""
    print("\nInstructions:")
    print("1. Ensure you are connected to the network where devices are located.")
    print("2. When scanning for specific device types, be prepared to enter required information:")
    print("   - IP Address: Enter the IP address if prompted (e.g., for MQTT or Home Assistant).")
    print("   - API Token: For Home Assistant, you may need an API token. Generate this in Home Assistant settings.")
    print("3. Required Libraries:")
    print("   - Install all dependencies using 'pip install -r requirements.txt'.")
    print("4. Follow on-screen prompts to interact with devices.")
    input("\nPress Enter to return to the main menu.")

def prompt_for_ip():
    """Prompt the user for an IP address."""
    return input("Enter the IP address of the device: ").strip()

def prompt_for_token():
    """Prompt the user for an API token."""
    return input("Enter the API token: ").strip()

def scan_for_smart_devices(option):
    """Scan for specific smart devices based on user selection."""
    if option == "1":
        print("\nScanning for Roku devices...")
        devices = RokuDevice.discover()
    elif option == "2":
        print("\nScanning for TP-Link devices...")
        devices = TPLinkDevice.discover()
    elif option == "3":
        print("\nScanning for Printer devices...")
        devices = PrinterDevice.discover()
    elif option == "4":
        print("\nScanning for Broadlink devices...")
        devices = BroadlinkDevice.discover()
    elif option == "5":
        print("\nScanning for Chromecast devices...")
        devices = ChromecastDevice.discover()
    elif option == "6":
        print("\nScanning for MQTT devices...")
        broker_ip = prompt_for_ip()
        devices = MQTTDevice.discover(broker_ip)
    elif option == "7":
        print("\nScanning for Home Assistant devices...")
        hass_ip = prompt_for_ip()
        token = prompt_for_token()
        devices = HomeAssistantDevice.discover(hass_ip, token)
    elif option == "8":
        print("\nScanning for Smart TVs...")
        devices = SmartTVDevice.discover()
    else:
        print("Returning to main menu.")
        return []

    return devices

def scan_for_devices(option):
    """Scan for devices based on main menu selection."""
    if option == "1":
        return discover_all_devices()
    elif option == "2":
        while True:
            display_smart_devices_menu()
            sub_option = input("Enter your choice: ").strip()
            if sub_option == "9":
                break
            devices = scan_for_smart_devices(sub_option)
            if devices:
                return devices
    elif option == "3":
        print("\nScanning for Computers...")
        return ComputerDevice.discover()
    elif option == "4":
        print("\nScanning for Phones...")
        return PhoneDevice.discover()
    else:
        print("\nInvalid option. Please try again.")
        return []
