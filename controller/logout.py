from PySide6.QtWidgets import QMessageBox

from abstract import Controller
from utils.auth import auth
from utils.strings import *
from view.homepage import HomeGuestView


class ControllerLogout(Controller):
    def __init__(self):
        super().__init__()

    def logout(self) -> None:
        response = self.confirm(title=BOX_TITLE_LOGOUT,
                                message=BOX_MESSAGE_LOGOUT)
        if response == QMessageBox.StandardButton.Yes:
            auth.logout()
            self.redirect(HomeGuestView())
