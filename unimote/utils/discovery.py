# utils/discovery.py

from devices import (
    RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice,
    BroadlinkDevice, ChromecastDevice, MQTTDevice, HomeAssistantDevice,
    SmartTVDevice, ComputerDevice, PhoneDevice, IPCameraDevice
)

def discover_all_devices():
    """Discover all device types available on the network."""
    devices = []
    devices.extend(RokuDevice.discover())
    devices.extend(TPLinkDevice.discover())
    devices.extend(PrinterDevice.discover())
    devices.extend(RESTAPIDevice.discover())
    devices.extend(BroadlinkDevice.discover())
    devices.extend(ChromecastDevice.discover())
    devices.extend(MQTTDevice.discover())
    devices.extend(HomeAssistantDevice.discover())
    devices.extend(SmartTVDevice.discover())
    devices.extend(ComputerDevice.discover())
    devices.extend(PhoneDevice.discover())
    devices.extend(IPCameraDevice.discover())
    return devices

def discover_device_by_type(device_type):
    """Discover devices of a specific type."""
    if device_type == "roku":
        return RokuDevice.discover()
    elif device_type == "tplink":
        return TPLinkDevice.discover()
    elif device_type == "printer":
        return PrinterDevice.discover()
    elif device_type == "broadlink":
        return BroadlinkDevice.discover()
    elif device_type == "chromecast":
        return ChromecastDevice.discover()
    elif device_type == "mqtt":
        return MQTTDevice.discover()
    elif device_type == "home_assistant":
        return HomeAssistantDevice.discover()
    elif device_type == "smart_tv":
        return SmartTVDevice.discover()
    elif device_type == "computer":
        return ComputerDevice.discover()
    elif device_type == "phone":
        return PhoneDevice.discover()
    elif device_type == "ip_camera":
        return IPCameraDevice.discover()
    else:
        print(f"Unknown device type: {device_type}")
        return []
