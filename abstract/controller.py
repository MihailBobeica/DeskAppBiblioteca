from typing import Optional, TypeVar

from PySide6.QtWidgets import QMessageBox

from abstract.model import Model
from abstract.view import View

BoundedModel = TypeVar("BoundedModel", bound=Model)
BoundedView = TypeVar("BoundedView", bound=View)


class Controller:
    # protocol methods
    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        from datetime import datetime
        print(datetime.now(), message)
        try:
            f = self.__getattribute__(message)
            if data is None:
                data = dict()
            f(**data)
        except AttributeError:
            pass

    def __init__(self):
        from app import main_window
        self.main_window = main_window

    def redirect(self, view: BoundedView) -> None:
        self.main_window.set_view(view)

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
