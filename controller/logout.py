from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract.controller import Controller
from utils.auth import auth
from utils.request import *
from utils.strings import *
from view.homepage.guest import HomeGuestView


class LogoutController(Controller):
    def __init__(self):
        super().__init__()

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == REQUEST_LOGOUT:
            self.confirm_logout()

    def confirm_logout(self) -> None:
        response = self.confirm(title=LOGOUT_TITLE,
                                message=LOGOUT_MESSAGE)
        if response == QMessageBox.StandardButton.Yes:
            auth.logout()
            self.main_window.set_view(HomeGuestView())
