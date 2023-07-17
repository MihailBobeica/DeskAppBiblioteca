import uuid
from typing import Dict, Optional

from protocol.observer import Observer
from utils import get_label


class Model:
    def attach(self, observer: Observer, label: Optional[str] = None):
        self.views[get_label(label)] = observer

    def detach(self, label: str):
        del self.views[label]

    def notify(self, message: str, data: dict):
        for view in self.views.values():
            view.receive_message(message, data)

    def __init__(self):
        self.views: Dict[str, Observer] = dict()
