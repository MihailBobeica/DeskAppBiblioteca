from abc import abstractmethod
from typing import Dict, Optional

from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit

from protocol.observer import Observer
from .model import Model


class View(QWidget):
    def __init__(self, models: Optional[Dict[str, Model]] = None):
        super().__init__()
        self.models = models
        self.controllers: Dict[str: Observer] = dict()
        self.btn: Dict[str, QPushButton] = dict()
        self.qle: Dict[str, QLineEdit] = dict()

        from app import main_window
        self.main_window = main_window

        self.create_layout()
        self.connect_buttons()
        self.attach_controllers()

    def attach(self, label: str, observer: Observer):
        self.controllers[label] = observer

    def detach(self, label: str):
        del self.controllers[label]

    def notify(self, message: str, data: dict):
        for controller in self.controllers.values():
            controller.update(message, data)

    def add_buttons(self, btn: Dict[str, QPushButton]):
        self.btn.update(btn)

    def attach_controllers(self):
        pass

    @abstractmethod
    def create_layout(self):
        pass

    @abstractmethod
    def connect_buttons(self):
        pass
