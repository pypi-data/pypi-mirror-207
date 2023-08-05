from .models import USBDevice
from _typeshed import Incomplete
from homeassistant.core import CALLBACK_TYPE, Event, HomeAssistant
from homeassistant.data_entry_flow import BaseServiceInfo
from homeassistant.loader import USBMatcher
from pyudev import Device
from serial.tools.list_ports_common import ListPortInfo

class USBCallbackMatcher(USBMatcher): ...

def async_register_scan_request_callback(hass: HomeAssistant, callback: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
def async_is_plugged_in(hass: HomeAssistant, matcher: USBCallbackMatcher) -> bool: ...

class UsbServiceInfo(BaseServiceInfo):
    device: str
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None
    def __init__(self, device, vid, pid, serial_number, manufacturer, description) -> None: ...

class USBDiscovery:
    hass: Incomplete
    usb: Incomplete
    seen: Incomplete
    observer_active: bool
    _request_debouncer: Incomplete
    _request_callbacks: Incomplete
    initial_scan_done: bool
    _initial_scan_callbacks: Incomplete
    def __init__(self, hass: HomeAssistant, usb: list[USBMatcher]) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_start(self, event: Event) -> None: ...
    async def async_stop(self, event: Event) -> None: ...
    async def _async_start_monitor(self) -> None: ...
    def _device_discovered(self, device: Device) -> None: ...
    def async_register_scan_request_callback(self, _callback: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
    def async_register_initial_scan_callback(self, callback: CALLBACK_TYPE) -> CALLBACK_TYPE: ...
    def _async_process_discovered_usb_device(self, device: USBDevice) -> None: ...
    def _async_process_ports(self, ports: list[ListPortInfo]) -> None: ...
    async def _async_scan_serial(self) -> None: ...
    async def _async_scan(self) -> None: ...
    async def async_request_scan(self) -> None: ...
