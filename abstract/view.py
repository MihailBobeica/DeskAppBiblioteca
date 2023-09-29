from abc import abstractmethod
from typing import Optional

from PySide6.QtWidgets import QFrame

from protocol import Observer
from utils.backend import get_label
from utils.request import Request


class View(QFrame):
    # protocol methods
    def attach(self, observer: Observer, label: Optional[str] = None) -> None:
        self.controllers[get_label(label)] = observer

    def detach(self, label: str) -> None:
        del self.controllers[label]

    def notify(self, message: Request, data: Optional[dict] = None) -> None:
        for controller in self.controllers.values():
            controller.receive_message(message, data)

    def receive_message(self, message: Request, data: Optional[dict] = None) -> None:
        pass

    @abstractmethod
    def create_layout(self) -> None:
        pass

    def __init__(self):
        from app import main_window
        self.main_window = main_window

        super().__init__()
        self.controllers: dict[str, Observer] = dict()
        self.attach_controllers()

        self.create_layout()

    def refresh(self):
        pass

    def attach_controllers(self) -> None:
        pass

    def redirect(self, view) -> None:
        self.main_window.set_view(view)

    def logout(self):
        self.notify(Request.LOGOUT)
