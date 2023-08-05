import asyncio
from .const import EVENT_COALESCE_TIME as EVENT_COALESCE_TIME, MAX_PENDING_HISTORY_STATES as MAX_PENDING_HISTORY_STATES
from .helpers import entities_may_have_state_changes_after as entities_may_have_state_changes_after
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable, MutableMapping
from datetime import datetime as dt
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.recorder import get_instance as get_instance, history as history
from homeassistant.components.websocket_api import messages as messages
from homeassistant.components.websocket_api.connection import ActiveConnection as ActiveConnection
from homeassistant.const import COMPRESSED_STATE_ATTRIBUTES as COMPRESSED_STATE_ATTRIBUTES, COMPRESSED_STATE_LAST_CHANGED as COMPRESSED_STATE_LAST_CHANGED, COMPRESSED_STATE_LAST_UPDATED as COMPRESSED_STATE_LAST_UPDATED, COMPRESSED_STATE_STATE as COMPRESSED_STATE_STATE
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback, is_callback as is_callback, valid_entity_id as valid_entity_id
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.json import JSON_DUMP as JSON_DUMP
from typing import Any

_LOGGER: Incomplete

class HistoryLiveStream:
    stream_queue: asyncio.Queue[Event]
    subscriptions: list[CALLBACK_TYPE]
    end_time_unsub: CALLBACK_TYPE | None
    task: asyncio.Task | None
    wait_sync_task: asyncio.Task | None
    def __init__(self, stream_queue, subscriptions, end_time_unsub, task, wait_sync_task) -> None: ...

def async_setup(hass: HomeAssistant) -> None: ...
def _ws_get_significant_states(hass: HomeAssistant, msg_id: int, start_time: dt, end_time: dt | None, entity_ids: list[str] | None, include_start_time_state: bool, significant_changes_only: bool, minimal_response: bool, no_attributes: bool) -> str: ...
async def ws_get_history_during_period(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
def _generate_stream_message(states: MutableMapping[str, list[dict[str, Any]]], start_day: dt, end_day: dt) -> dict[str, Any]: ...
def _async_send_empty_response(connection: ActiveConnection, msg_id: int, start_time: dt, end_time: dt | None) -> None: ...
def _generate_websocket_response(msg_id: int, start_time: dt, end_time: dt, states: MutableMapping[str, list[dict[str, Any]]]) -> str: ...
def _generate_historical_response(hass: HomeAssistant, msg_id: int, start_time: dt, end_time: dt, entity_ids: list[str] | None, include_start_time_state: bool, significant_changes_only: bool, minimal_response: bool, no_attributes: bool, send_empty: bool) -> tuple[float, dt | None, str | None]: ...
async def _async_send_historical_states(hass: HomeAssistant, connection: ActiveConnection, msg_id: int, start_time: dt, end_time: dt, entity_ids: list[str] | None, include_start_time_state: bool, significant_changes_only: bool, minimal_response: bool, no_attributes: bool, send_empty: bool) -> dt | None: ...
def _history_compressed_state(state: State, no_attributes: bool) -> dict[str, Any]: ...
def _events_to_compressed_states(events: Iterable[Event], no_attributes: bool) -> MutableMapping[str, list[dict[str, Any]]]: ...
async def _async_events_consumer(subscriptions_setup_complete_time: dt, connection: ActiveConnection, msg_id: int, stream_queue: asyncio.Queue[Event], no_attributes: bool) -> None: ...
def _async_subscribe_events(hass: HomeAssistant, subscriptions: list[CALLBACK_TYPE], target: Callable[[Event], None], entity_ids: list[str], significant_changes_only: bool, minimal_response: bool) -> None: ...
async def ws_stream(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
