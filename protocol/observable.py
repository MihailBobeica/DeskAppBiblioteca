from typing import Protocol
from .observer import Observer


class Observable(Protocol):
    def attach(self, observer: Observer):
        ...

    def detach(self, observer: Observer):
        ...

    def notify(self, message: str, data: dict):
        ...
