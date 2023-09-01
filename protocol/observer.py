from typing import Protocol, Optional

from utils.request import Request


class Observer(Protocol):
    def receive_message(self, message: Request, data: Optional[dict] = None):
        ...
