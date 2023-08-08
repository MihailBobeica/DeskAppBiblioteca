from abc import abstractmethod
from typing import Optional, Any, Iterable

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QLineEdit, QFrame, QLayout

from protocol import Observer
from utils.backend import get_label
from utils.ui import get_style


class View(QFrame):
    # protocol methods
    def attach(self, observer: Observer, label: Optional[str] = None) -> None:
        self.controllers[get_label(label)] = observer

    def detach(self, label: str) -> None:
        del self.controllers[label]

    def notify(self, message: str, data: Optional[dict] = None) -> None:
        for controller in self.controllers.values():
            controller.receive_message(message, data)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        pass

    @abstractmethod
    def create_layout(self) -> None:
        pass

    def connect_buttons(self):
        pass

    def __init__(self):
        super().__init__()
        from app import main_window
        self.main_window = main_window

        self.controllers: dict[str, Observer] = dict()
        self.attach_controllers()

        self.create_layout()
        self.connect_buttons()

    def update(self):
        pass

    def attach_controllers(self) -> None:
        pass

    def redirect(self, view: Any) -> None:
        self.main_window.set_view(view)

    def send_logout_request(self):
        self.notify("logout")

    def send_option_1(self):
        self.notify("Option1")

    def get_button(self, label) -> QPushButton:
        button: QPushButton = self.findChild(QPushButton, label, Qt.FindChildrenRecursively)
        return button

    def get_line_edit(self, label) -> QLineEdit:
        line_edit: QLineEdit = self.findChild(QLineEdit, label, Qt.FindChildrenRecursively)
        return line_edit

    def add_buttons(self, labels: Iterable[str], layout: Optional[QLayout] = None, style: Optional[str] = None):
        if not layout:
            layout = self.layout()
        for label in labels:
            button = QPushButton(label)
            button.setObjectName(label)
            if style:
                button.setStyleSheet(get_style(style))
            layout.addWidget(button)
