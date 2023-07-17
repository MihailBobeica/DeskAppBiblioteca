from abc import abstractmethod
from typing import Dict, Optional

from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit

from protocol.observer import Observer
from utils import get_label


class View(QWidget):
    def attach(self, observer: Observer, label: Optional[str] = None):
        self.controllers[get_label(label)] = observer

    def detach(self, label: str):
        del self.controllers[label]

    def notify(self, message: str, data: dict):
        for controller in self.controllers.values():
            controller.receive_message(message, data)

    def receive_message(self, message: str, data: dict):
        pass

    @abstractmethod
    def create_layout(self):
        pass

    @abstractmethod
    def connect_buttons(self):
        pass

    def __init__(self):
        super().__init__()
        from app import main_window
        self.main_window = main_window

        self.btn: Dict[str, QPushButton] = dict()
        self.qle: Dict[str, QLineEdit] = dict()
        self.controllers: Dict[str: Observer] = dict()

        self.create_layout()
        self.connect_buttons()
        self.attach_controllers()

    def attach_controllers(self):
        pass

    def add_buttons(self, btn: Dict[str, QPushButton]):
        self.btn.update(btn)
