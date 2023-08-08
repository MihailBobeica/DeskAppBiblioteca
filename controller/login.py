from typing import Optional

from abstract.controller import Controller, BoundedModel
from utils.auth import Auth, check_password
from utils.backend import is_empty
from utils.strings import *
from view.home_admin import HomeAdminView
from view.home_operatore import HomeOperatoreView
from view.home_utente import HomeUtenteView


class LoginController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models)

    def receive_message(self, message: str, data: Optional[dict] = None):
        if message == "login":
            self.login(data["username"], data["password"])

    def login(self, username: str, password: str) -> None:
        user = self.models["utente"].by_username(username)
        if is_empty(username):
            self.no_username_popup()
            return
        if is_empty(password):
            self.no_password_popup()
            return
        if (user is None) or (not check_password(password, user.password)):
            self.bad_credentials_popup()
            return
        Auth.logged_as(user)
        if Auth.is_logged_as(UTENTE):
            self.redirect(HomeUtenteView())
        elif Auth.is_logged_as(OPERATORE):
            self.redirect(HomeOperatoreView())
        elif Auth.is_logged_as(ADMIN):
            self.redirect(HomeAdminView())
        self.main_window.reset_history()

    def bad_credentials_popup(self):
        self.alert(ACCESS_DENIED_TITLE, BAD_CREDENTIALS_MESSAGE)

    def no_username_popup(self):
        self.alert(ACCESS_DENIED_TITLE, NO_USERNAME_MESSAGE)

    def no_password_popup(self):
        self.alert(ACCESS_DENIED_TITLE, NO_PASSWORD_MESSAGE)
