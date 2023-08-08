from typing import Optional

from abstract.controller import Controller, BoundedModel
from utils.auth import Auth, check_password
from utils.backend import is_empty, REQUEST_GO_TO_LOGIN
from utils.strings import *
from view.auth import LoginView
from view.homepage.admin import HomeAdminView
from view.homepage.operatore import HomeOperatoreView
from view.homepage.utente import HomeUtenteView


class LoginController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models)

    def receive_message(self, message: str, data: Optional[dict] = None):
        if message == "login":
            self.login(data["username"], data["password"])
        elif message == REQUEST_GO_TO_LOGIN:
            self.go_to_login()

    def go_to_login(self):
        self.redirect(LoginView())

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
