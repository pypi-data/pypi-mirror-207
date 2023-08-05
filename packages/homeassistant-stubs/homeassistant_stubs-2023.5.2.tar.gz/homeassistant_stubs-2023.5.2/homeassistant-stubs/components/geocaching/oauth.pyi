from .const import ENVIRONMENT as ENVIRONMENT, ENVIRONMENT_URLS as ENVIRONMENT_URLS
from homeassistant.components.application_credentials import AuthImplementation as AuthImplementation, AuthorizationServer as AuthorizationServer, ClientCredential as ClientCredential
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

class GeocachingOAuth2Implementation(AuthImplementation):
    def __init__(self, hass: HomeAssistant, auth_domain: str, credential: ClientCredential) -> None: ...
    @property
    def extra_authorize_data(self) -> dict: ...
    async def async_resolve_external_data(self, external_data: Any) -> dict: ...
    async def _async_refresh_token(self, token: dict) -> dict: ...
