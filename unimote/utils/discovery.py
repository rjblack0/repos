# utils/discovery.py

from devices import (
    RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice, BroadlinkDevice,
    ChromecastDevice, MQTTDevice, HomeAssistantDevice, SmartTVDevice,
    ComputerDevice, PhoneDevice, IPCameraDevice
)

def discover_all_devices():
    """Discover all device types available on the network and summarize results."""
    devices = []
    found_device_types = []  # Track what types of devices were found
    device_types = {
        "Roku Devices": RokuDevice,
        "TP-Link Devices": TPLinkDevice,
        "Printers": PrinterDevice,
        "REST API Devices": RESTAPIDevice,
        "Broadlink Devices": BroadlinkDevice,
        "Chromecast Devices": ChromecastDevice,
        "MQTT Devices": MQTTDevice,
        "Home Assistant Devices": HomeAssistantDevice,
        "Smart TVs": SmartTVDevice,
        "Computers": ComputerDevice,
        "Phones": PhoneDevice,
        "IP Cameras": IPCameraDevice
    }

    for device_name, device_class in device_types.items():
        found_devices = device_class.discover()
        if found_devices:
            found_device_types.append(device_name)  # Only log the type if devices are found
            devices.extend(found_devices)

    # Display a summary of device types found
    if found_device_types:
        print("\nSummary of Devices Found:")
        for device_type in found_device_types:
            print(f"- {device_type}")
    else:
        print("\nNo devices found on the network.")

    return devices
