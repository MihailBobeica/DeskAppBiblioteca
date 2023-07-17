from abc import abstractmethod
from typing import Dict, Optional, Any

from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit

from protocol.observer import Observer
from utils import get_label


class View(QWidget):
    def attach(self, observer: Observer, label: Optional[str] = None) -> None:
        self.controllers[get_label(label)] = observer

    def detach(self, label: str) -> None:
        del self.controllers[label]

    def notify(self, message: str, data: dict) -> None:
        for controller in self.controllers.values():
            controller.receive_message(message, data)

    def receive_message(self, message: str, data: dict) -> None:
        pass

    @abstractmethod
    def create_layout(self) -> None:
        pass

    @abstractmethod
    def connect_buttons(self) -> None:
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

    def attach_controllers(self) -> None:
        pass

    def add_buttons(self, btn: Dict[str, QPushButton]) -> None:
        self.btn.update(btn)

    def redirect(self, view: Any) -> None:
        self.main_window.set_view(view)

    def send_logout_request(self):
        self.notify("logout", dict())
