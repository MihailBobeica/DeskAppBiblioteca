from typing import Protocol, Optional
from .observer import Observer


class Observable(Protocol):
    def attach(self, observer: Observer):
        ...

    def detach(self, observer: Observer):
        ...

    def notify(self, message: str, data: Optional[dict] = None):
        ...
