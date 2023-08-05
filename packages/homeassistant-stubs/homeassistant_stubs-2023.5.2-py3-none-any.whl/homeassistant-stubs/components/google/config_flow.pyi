import logging
from .api import AccessTokenAuthImpl as AccessTokenAuthImpl, DEVICE_AUTH_CREDS as DEVICE_AUTH_CREDS, DeviceAuth as DeviceAuth, DeviceFlow as DeviceFlow, OAuthError as OAuthError, async_create_device_flow as async_create_device_flow, get_feature_access as get_feature_access
from .const import CONF_CALENDAR_ACCESS as CONF_CALENDAR_ACCESS, DOMAIN as DOMAIN, FeatureAccess as FeatureAccess
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete

class OAuth2FlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler):
    DOMAIN = DOMAIN
    _reauth_config_entry: Incomplete
    _device_flow: Incomplete
    def __init__(self) -> None: ...
    @property
    def logger(self) -> logging.Logger: ...
    flow_impl: Incomplete
    external_data: Incomplete
    async def async_step_import(self, info: dict[str, Any]) -> FlowResult: ...
    async def async_step_auth(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_creation(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_oauth_create_entry(self, data: dict) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> config_entries.OptionsFlow: ...

class OptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
