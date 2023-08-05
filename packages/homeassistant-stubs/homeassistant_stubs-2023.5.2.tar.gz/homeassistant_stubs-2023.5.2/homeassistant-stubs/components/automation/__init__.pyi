from .config import AutomationConfig as AutomationConfig
from .const import CONF_ACTION as CONF_ACTION, CONF_INITIAL_STATE as CONF_INITIAL_STATE, CONF_TRACE as CONF_TRACE, CONF_TRIGGER as CONF_TRIGGER, CONF_TRIGGER_VARIABLES as CONF_TRIGGER_VARIABLES, DEFAULT_INITIAL_STATE as DEFAULT_INITIAL_STATE, DOMAIN as DOMAIN, LOGGER as LOGGER
from .helpers import async_get_blueprints as async_get_blueprints
from .trace import trace_automation as trace_automation
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.blueprint import CONF_USE_BLUEPRINT as CONF_USE_BLUEPRINT
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_MODE as ATTR_MODE, ATTR_NAME as ATTR_NAME, CONF_ALIAS as CONF_ALIAS, CONF_CONDITION as CONF_CONDITION, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_EVENT_DATA as CONF_EVENT_DATA, CONF_ID as CONF_ID, CONF_MODE as CONF_MODE, CONF_PATH as CONF_PATH, CONF_PLATFORM as CONF_PLATFORM, CONF_VARIABLES as CONF_VARIABLES, CONF_ZONE as CONF_ZONE, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, SERVICE_RELOAD as SERVICE_RELOAD, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.exceptions import ConditionError as ConditionError, ConditionErrorContainer as ConditionErrorContainer, ConditionErrorIndex as ConditionErrorIndex, HomeAssistantError as HomeAssistantError, ServiceNotFound as ServiceNotFound, TemplateError as TemplateError
from homeassistant.helpers import condition as condition
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.integration_platform import async_process_integration_platform_for_component as async_process_integration_platform_for_component
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.script import ATTR_CUR as ATTR_CUR, ATTR_MAX as ATTR_MAX, CONF_MAX as CONF_MAX, CONF_MAX_EXCEEDED as CONF_MAX_EXCEEDED, Script as Script, script_stack_cv as script_stack_cv
from homeassistant.helpers.script_variables import ScriptVariables as ScriptVariables
from homeassistant.helpers.service import ReloadServiceHelper as ReloadServiceHelper, async_register_admin_service as async_register_admin_service
from homeassistant.helpers.trace import TraceElement as TraceElement, script_execution_set as script_execution_set, trace_append_element as trace_append_element, trace_get as trace_get, trace_path as trace_path
from homeassistant.helpers.trigger import TriggerActionType as TriggerActionType, TriggerData as TriggerData, TriggerInfo as TriggerInfo, async_initialize_triggers as async_initialize_triggers
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.dt import parse_datetime as parse_datetime
from typing import Any, Protocol

ENTITY_ID_FORMAT: Incomplete
CONF_SKIP_CONDITION: str
CONF_STOP_ACTIONS: str
DEFAULT_STOP_ACTIONS: bool
EVENT_AUTOMATION_RELOADED: str
EVENT_AUTOMATION_TRIGGERED: str
ATTR_LAST_TRIGGERED: str
ATTR_SOURCE: str
ATTR_VARIABLES: str
SERVICE_TRIGGER: str

class IfAction(Protocol):
    config: list[ConfigType]
    def __call__(self, variables: Mapping[str, Any] | None = ...) -> bool: ...
AutomationActionType = TriggerActionType
AutomationTriggerData = TriggerData
AutomationTriggerInfo = TriggerInfo

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
def _automations_with_x(hass: HomeAssistant, referenced_id: str, property_name: str) -> list[str]: ...
def _x_in_automation(hass: HomeAssistant, entity_id: str, property_name: str) -> list[str]: ...
def automations_with_entity(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def entities_in_automation(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def automations_with_device(hass: HomeAssistant, device_id: str) -> list[str]: ...
def devices_in_automation(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def automations_with_area(hass: HomeAssistant, area_id: str) -> list[str]: ...
def areas_in_automation(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def automations_with_blueprint(hass: HomeAssistant, blueprint_path: str) -> list[str]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class AutomationEntity(ToggleEntity, RestoreEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _trigger_config: Incomplete
    _async_detach_triggers: Incomplete
    _cond_func: Incomplete
    action_script: Incomplete
    _initial_state: Incomplete
    _is_enabled: bool
    _referenced_entities: Incomplete
    _referenced_devices: Incomplete
    _logger: Incomplete
    _variables: Incomplete
    _trigger_variables: Incomplete
    raw_config: Incomplete
    _blueprint_inputs: Incomplete
    _trace_config: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, automation_id: str | None, name: str, trigger_config: list[ConfigType], cond_func: IfAction | None, action_script: Script, initial_state: bool | None, variables: ScriptVariables | None, trigger_variables: ScriptVariables | None, raw_config: ConfigType | None, blueprint_inputs: ConfigType | None, trace_config: ConfigType) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def referenced_areas(self) -> set[str]: ...
    @property
    def referenced_blueprint(self) -> str | None: ...
    @property
    def referenced_devices(self) -> set[str]: ...
    @property
    def referenced_entities(self) -> set[str]: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_trigger(self, run_variables: dict[str, Any], context: Context | None = ..., skip_condition: bool = ...) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_enable(self) -> None: ...
    async def async_disable(self, stop_actions: bool = ...) -> None: ...
    async def _async_attach_triggers(self, home_assistant_start: bool) -> Callable[[], None] | None: ...

class AutomationEntityConfig:
    config_block: ConfigType
    list_no: int
    raw_blueprint_inputs: ConfigType | None
    raw_config: ConfigType | None
    def __init__(self, config_block, list_no, raw_blueprint_inputs, raw_config) -> None: ...

async def _prepare_automation_config(hass: HomeAssistant, config: ConfigType) -> list[AutomationEntityConfig]: ...
def _automation_name(automation_config: AutomationEntityConfig) -> str: ...
async def _create_automation_entities(hass: HomeAssistant, automation_configs: list[AutomationEntityConfig]) -> list[AutomationEntity]: ...
async def _async_process_config(hass: HomeAssistant, config: dict[str, Any], component: EntityComponent[AutomationEntity]) -> None: ...
async def _async_process_if(hass: HomeAssistant, name: str, config: dict[str, Any]) -> IfAction | None: ...
def _trigger_extract_devices(trigger_conf: dict) -> list[str]: ...
def _trigger_extract_entities(trigger_conf: dict) -> list[str]: ...
def websocket_config(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
