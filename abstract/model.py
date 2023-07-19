from abc import abstractmethod
from typing import Dict, Optional

from protocol.observer import Observer
from utils import get_label


class Model:
    # protocol methods
    def attach(self, observer: Observer, label: Optional[str] = None) -> None:
        self.views[get_label(label)] = observer

    def detach(self, label: str) -> None:
        del self.views[label]

    def notify(self, message: str, data: Optional[dict] = None) -> None:
        for view in self.views.values():
            view.receive_message(message, data)

    def __init__(self):
        self.views: Dict[str, Observer] = dict()

    @abstractmethod
    def inserisci(self, dati: Dict[str, str]):
        pass
