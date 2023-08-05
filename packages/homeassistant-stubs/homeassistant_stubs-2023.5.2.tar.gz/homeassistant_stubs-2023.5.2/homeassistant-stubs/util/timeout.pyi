import asyncio
import enum
from .async_ import run_callback_threadsafe as run_callback_threadsafe
from _typeshed import Incomplete
from types import TracebackType
from typing import Any
from typing_extensions import Self

ZONE_GLOBAL: str

class _State(str, enum.Enum):
    INIT: str
    ACTIVE: str
    TIMEOUT: str
    EXIT: str

class _GlobalFreezeContext:
    _loop: Incomplete
    _manager: Incomplete
    def __init__(self, manager: TimeoutManager) -> None: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(self, exc_type: type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> bool | None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> bool | None: ...
    def _enter(self) -> None: ...
    def _exit(self) -> None: ...

class _ZoneFreezeContext:
    _loop: Incomplete
    _zone: Incomplete
    def __init__(self, zone: _ZoneTimeoutManager) -> None: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(self, exc_type: type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> bool | None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> bool | None: ...
    def _enter(self) -> None: ...
    def _exit(self) -> None: ...

class _GlobalTaskContext:
    _loop: Incomplete
    _manager: Incomplete
    _task: Incomplete
    _time_left: Incomplete
    _expiration_time: Incomplete
    _timeout_handler: Incomplete
    _on_wait_task: Incomplete
    _wait_zone: Incomplete
    _state: Incomplete
    _cool_down: Incomplete
    def __init__(self, manager: TimeoutManager, task: asyncio.Task[Any], timeout: float, cool_down: float) -> None: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(self, exc_type: type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> bool | None: ...
    @property
    def state(self) -> _State: ...
    def zones_done_signal(self) -> None: ...
    def _start_timer(self) -> None: ...
    def _stop_timer(self) -> None: ...
    def _on_timeout(self) -> None: ...
    def _cancel_task(self) -> None: ...
    def pause(self) -> None: ...
    def reset(self) -> None: ...
    async def _on_wait(self) -> None: ...

class _ZoneTaskContext:
    _loop: Incomplete
    _zone: Incomplete
    _task: Incomplete
    _state: Incomplete
    _time_left: Incomplete
    _expiration_time: Incomplete
    _timeout_handler: Incomplete
    def __init__(self, zone: _ZoneTimeoutManager, task: asyncio.Task[Any], timeout: float) -> None: ...
    @property
    def state(self) -> _State: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(self, exc_type: type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> bool | None: ...
    def _start_timer(self) -> None: ...
    def _stop_timer(self) -> None: ...
    def _on_timeout(self) -> None: ...
    def pause(self) -> None: ...
    def reset(self) -> None: ...

class _ZoneTimeoutManager:
    _manager: Incomplete
    _zone: Incomplete
    _tasks: Incomplete
    _freezes: Incomplete
    def __init__(self, manager: TimeoutManager, zone: str) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def active(self) -> bool: ...
    @property
    def freezes_done(self) -> bool: ...
    def enter_task(self, task: _ZoneTaskContext) -> None: ...
    def exit_task(self, task: _ZoneTaskContext) -> None: ...
    def enter_freeze(self, freeze: _ZoneFreezeContext) -> None: ...
    def exit_freeze(self, freeze: _ZoneFreezeContext) -> None: ...
    def pause(self) -> None: ...
    def reset(self) -> None: ...

class TimeoutManager:
    _loop: Incomplete
    _zones: Incomplete
    _globals: Incomplete
    _freezes: Incomplete
    def __init__(self) -> None: ...
    @property
    def zones_done(self) -> bool: ...
    @property
    def freezes_done(self) -> bool: ...
    @property
    def zones(self) -> dict[str, _ZoneTimeoutManager]: ...
    @property
    def global_tasks(self) -> list[_GlobalTaskContext]: ...
    @property
    def global_freezes(self) -> list[_GlobalFreezeContext]: ...
    def drop_zone(self, zone_name: str) -> None: ...
    def async_timeout(self, timeout: float, zone_name: str = ..., cool_down: float = ...) -> _ZoneTaskContext | _GlobalTaskContext: ...
    def async_freeze(self, zone_name: str = ...) -> _ZoneFreezeContext | _GlobalFreezeContext: ...
    def freeze(self, zone_name: str = ...) -> _ZoneFreezeContext | _GlobalFreezeContext: ...
