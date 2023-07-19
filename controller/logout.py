from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract.controller import Controller

LOGOUT_TITLE = "Logout"
LOGOUT_MESSAGE = "Sei sicuro di voler uscire?"


class LogoutController(Controller):
    def __init__(self):
        super().__init__()

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "logout":
            self.confirm_logout()

    def confirm_logout(self) -> None:
        # TODO fix this
        response = self.confirm(LOGOUT_TITLE,
                                LOGOUT_MESSAGE)
        if response == QMessageBox.StandardButton.Yes:
            self.logout()
