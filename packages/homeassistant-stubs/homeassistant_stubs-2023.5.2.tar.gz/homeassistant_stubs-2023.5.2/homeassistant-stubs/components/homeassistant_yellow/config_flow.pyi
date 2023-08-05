from .const import DOMAIN as DOMAIN, ZHA_HW_DISCOVERY_DATA as ZHA_HW_DISCOVERY_DATA
from _typeshed import Incomplete
from homeassistant.components.hassio import HassioAPIError as HassioAPIError, async_get_yellow_settings as async_get_yellow_settings, async_reboot_host as async_reboot_host, async_set_yellow_settings as async_set_yellow_settings
from homeassistant.components.homeassistant_hardware import silabs_multiprotocol_addon as silabs_multiprotocol_addon
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import selector as selector
from typing import Any

_LOGGER: Incomplete
STEP_HW_SETTINGS_SCHEMA: Incomplete

class HomeAssistantYellowConfigFlow(ConfigFlow):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> HomeAssistantYellowOptionsFlow: ...
    async def async_step_system(self, data: dict[str, Any] | None = ...) -> FlowResult: ...

class HomeAssistantYellowOptionsFlow(silabs_multiprotocol_addon.OptionsFlowHandler):
    _hw_settings: dict[str, bool] | None
    async def async_step_on_supervisor(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_hardware_settings(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_confirm_reboot(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reboot_now(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reboot_later(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_multipan_settings(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def _async_serial_port_settings(self) -> silabs_multiprotocol_addon.SerialPortSettings: ...
    async def _async_zha_physical_discovery(self) -> dict[str, Any]: ...
    def _zha_name(self) -> str: ...
    def _hardware_name(self) -> str: ...
