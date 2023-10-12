from abstract import Controller
from factory import HomepageFactory
from model import ModelUsers
from utils.auth import auth, check_password
from utils.backend import is_empty
from utils.strings import *


class LoginController(Controller):
    def __init__(self, model_users: ModelUsers):
        self.model_users = model_users
        super().__init__()

    def login(self, username: str, password: str) -> None:
        user = self.model_users.by_username(username)
        if is_empty(username):
            self._no_username_popup()
            return
        if is_empty(password):
            self._no_password_popup()
            return
        if (user is None) or (not check_password(password, user.password)):
            self._bad_credentials_popup()
            return
        auth.login_as(user)
        homepage_factory = HomepageFactory()
        self.main_window.set_view(homepage_factory.create(auth.get_key()))

    def _bad_credentials_popup(self):
        self.alert(ACCESS_DENIED_TITLE, BAD_CREDENTIALS_MESSAGE)

    def _no_username_popup(self):
        self.alert(ACCESS_DENIED_TITLE, NO_USERNAME_MESSAGE)

    def _no_password_popup(self):
        self.alert(ACCESS_DENIED_TITLE, NO_PASSWORD_MESSAGE)
