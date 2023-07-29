from typing import Optional, Dict, Type

from abstract.controller import Controller
from abstract.model import Model
from utils import check_password, is_empty, Auth
from view.homepage import HomePageView

# TODO put this in utils
ACCESS_DENIED_TITLE = "Accesso non riuscito"
BAD_CREDENTIALS_MESSAGE = "Credenziali di accesso errate."
NO_USERNAME_MESSAGE = "Non hai inserito l'username."
NO_PASSWORD_MESSAGE = "Non hai inserito la password."


class LoginController(Controller):
    def __init__(self, models: Optional[Dict[str, Type[Model]]] = None):
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
        self.redirect(HomePageView())

    def bad_credentials_popup(self):
        self.popup(ACCESS_DENIED_TITLE, BAD_CREDENTIALS_MESSAGE)

    def no_username_popup(self):
        self.popup(ACCESS_DENIED_TITLE, NO_USERNAME_MESSAGE)

    def no_password_popup(self):
        self.popup(ACCESS_DENIED_TITLE, NO_PASSWORD_MESSAGE)
