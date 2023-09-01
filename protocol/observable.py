from typing import Protocol, Optional
from protocol.observer import Observer
from utils.request import Request


class Observable(Protocol):
    def attach(self, observer: Observer):
        ...

    def detach(self, observer: Observer):
        ...

    def notify(self, message: Request, data: Optional[dict] = None):
        ...
