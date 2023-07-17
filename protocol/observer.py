from typing import Protocol


class Observer(Protocol):
    def receive_message(self, message: str, data: dict):
        ...
