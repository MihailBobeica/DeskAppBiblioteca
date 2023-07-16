from typing import Dict

from protocol.observer import Observer


class Model:
    def __init__(self):
        self.views: Dict[str, Observer] = dict()

    def attach(self, label: str, observer: Observer):
        self.views[label] = observer

    def detach(self, label: str):
        del self.views[label]

    def notify(self, message: str, data: dict):
        for view in self.views.values():
            view.update()
