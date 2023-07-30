from abc import abstractmethod
from typing import Optional

from protocol import Observer
from utils.backend import get_label


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
        self.views: dict[str, Observer] = dict()

    @abstractmethod
    def inserisci(self, dati: dict[str, str]):
        pass

    def seed_db(self, lista_dati: list[dict[str, str]]):
        for dati in lista_dati:
            self.inserisci(dati)
