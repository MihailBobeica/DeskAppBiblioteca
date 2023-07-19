from typing import Protocol, Optional


class Observer(Protocol):
    def receive_message(self, message: str, data: Optional[dict] = None):
        ...
