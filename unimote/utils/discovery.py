# utils/discovery.py

from devices import (
    RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice, BroadlinkDevice,
    ChromecastDevice, MQTTDevice, HomeAssistantDevice, SmartTVDevice,
    ComputerDevice, PhoneDevice, IPCameraDevice
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
