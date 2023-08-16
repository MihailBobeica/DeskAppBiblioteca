from typing import Optional

from abstract.controller import Controller, BoundedModel
from factory import HomepageFactory
from utils.auth import Auth, check_password
from utils.backend import is_empty
from utils.request import *
from utils.strings import *
from view.auth import LoginView


class LoginController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models)

    def receive_message(self, message: str, data: Optional[dict] = None):
        if message == REQUEST_LOGIN:
            username: str = data["username"]
            password: str = data["password"]
            self.login(username, password)
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
        self.redirect(HomepageFactory.create_homepage())

    def bad_credentials_popup(self):
        self.alert(ACCESS_DENIED_TITLE, BAD_CREDENTIALS_MESSAGE)

    def no_username_popup(self):
        self.alert(ACCESS_DENIED_TITLE, NO_USERNAME_MESSAGE)

    def no_password_popup(self):
        self.alert(ACCESS_DENIED_TITLE, NO_PASSWORD_MESSAGE)
