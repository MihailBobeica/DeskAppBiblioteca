from typing import Protocol, Optional
from protocol.observer import Observer


class Observable(Protocol):
    def attach(self, observer: Observer):
        ...

    def detach(self, observer: Observer):
        ...

    def notify(self, message: str, data: Optional[dict] = None):
        ...
