from typing import Optional, TypeVar, Type

from PySide6.QtWidgets import QMessageBox

from abstract.model import Model
from abstract.view import View

BoundedModel = TypeVar("BoundedModel", bound=Model)
BoundedView = TypeVar("BoundedView", bound=View)


class Controller:
    # protocol methods
    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        pass

    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        self.models = models
        from app import main_window
        self.main_window = main_window

    def redirect(self, view: BoundedView) -> None:
        self.main_window.set_view(view)

    def replace(self, view: BoundedView) -> None:
        self.main_window.replace(view)

    def go_back(self) -> None:
        self.main_window.go_back()

    def update_view(self, view: Type[BoundedView]) -> None:
        self.main_window.update_view(view)

    def alert(self, title: str, message: str) -> QMessageBox:
        return QMessageBox.information(self.main_window,
                                       title,
                                       message)

    def confirm(self, title: str, message: str) -> QMessageBox:
        return QMessageBox.question(self.main_window,
                                    title,
                                    message,
                                    QMessageBox.StandardButton.Yes,
                                    QMessageBox.StandardButton.No)
