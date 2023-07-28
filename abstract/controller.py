from typing import Optional, Dict, TypeVar

from PySide6.QtWidgets import QMessageBox

from abstract.model import Model
from abstract.view import View

BoundedModel = TypeVar("BoundedModel", bound=Model)
BoundedView = TypeVar("BoundedView", bound=View)


class Controller:
    # protocol methods
    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        pass

    def __init__(self, models: Optional[Dict[str, BoundedModel]] = None):
        self.models = models
        from app import main_window
        self.main_window = main_window

    def redirect(self, view: BoundedView) -> None:
        self.main_window.set_view(view)

    def popup(self, title: str, message: str) -> QMessageBox:  # TODO: put this in a view
        return QMessageBox.information(self.main_window.centralWidget(),
                                       title,
                                       message)

    def confirm(self, title: str, message: str) -> QMessageBox:  # TODO: put this in a view
        return QMessageBox.question(self.main_window,
                                    title,
                                    message,
                                    QMessageBox.StandardButton.Yes,
                                    QMessageBox.StandardButton.No)

    def logout(self) -> None:
        from view.first import FirstView
        self.redirect(FirstView())
