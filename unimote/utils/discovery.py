from devices.roku_device import RokuDevice
from devices.tplink_device import TPLinkDevice
from devices.printer_device import PrinterDevice
from devices.rest_api_device import RESTAPIDevice
from devices.broadlink_device import BroadlinkDevice
from devices.chromecast_device import ChromecastDevice
from devices.mqtt_device import MQTTDevice
from devices.home_assistant_device import HomeAssistantDevice

def discover_all_devices():
    device_classes = [
        RokuDevice, TPLinkDevice, PrinterDevice, RESTAPIDevice,
        BroadlinkDevice, ChromecastDevice, MQTTDevice, HomeAssistantDevice
    ]
    all_devices = []
    for cls in device_classes:
        try:
            devices = cls.discover()
            all_devices.extend(devices)
        except Exception as e:
            print(f"Error discovering devices with {cls.__name__}: {e}")
    return all_devices
