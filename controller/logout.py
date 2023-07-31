from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract.controller import Controller
from utils.auth import Auth
from utils.strings import *
from view.homepage import HomePageView


class LogoutController(Controller):
    def __init__(self):
        super().__init__()

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "logout":
            self.confirm_logout()

    def confirm_logout(self) -> None:
        response = self.confirm(title=LOGOUT_TITLE,
                                message=LOGOUT_MESSAGE)
        if response == QMessageBox.StandardButton.Yes:
            Auth.logout()
            self.redirect(HomePageView())
