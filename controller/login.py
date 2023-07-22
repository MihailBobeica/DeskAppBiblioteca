from typing import Optional, Dict, Type

from abstract.controller import Controller
from abstract.model import Model
from database import ADMIN, OPERATORE, UTENTE
from utils import check_password, is_empty
from view.home_admin import HomeAdminView
from view.home_operatore import HomeOperatoreView
from view.home_utente import HomeUtenteView

# TODO put this in utils
ACCESS_DENIED_TITLE = "Accesso non riuscito"
BAD_CREDENTIALS_MESSAGE = "Credenziali di accesso errate"
NO_USERNAME_MESSAGE = "Non hai inserito l'username"
NO_PASSWORD_MESSAGE = "Non hai inserito la password"


class LoginController(Controller):
    def __init__(self, models: Optional[Dict[str, Type[Model]]] = None):
        super().__init__(models)
        self.logged = False

    def receive_message(self, message: str, data: Optional[dict] = None):
        if message == "login":
            self.login(data["username"], data["password"])

    def login(self, username: str, password: str) -> None:
        utente = self.models["utente"].by_username(username)
        if is_empty(username):
            self.no_username_popup()
            return
        if is_empty(password):
            self.no_password_popup()
            return
        if (utente is None) or (not check_password(password, utente.password)):
            self.bad_credentials_popup()
            return
        if utente.ruolo == ADMIN:
            self.redirect_home_admin()
            return
        if utente.ruolo == OPERATORE:
            self.redirect_home_operatore()
            return
        if utente.ruolo == UTENTE:
            self.redirect_home_utente()
            return

    def bad_credentials_popup(self):
        self.popup(ACCESS_DENIED_TITLE, BAD_CREDENTIALS_MESSAGE)

    def no_username_popup(self):
        self.popup(ACCESS_DENIED_TITLE, NO_USERNAME_MESSAGE)

    def no_password_popup(self):
        self.popup(ACCESS_DENIED_TITLE, NO_PASSWORD_MESSAGE)

    def redirect_home_admin(self):
        self.redirect(HomeAdminView())
        self.logged = True

    def redirect_home_operatore(self):
        self.redirect(HomeOperatoreView())
        self.logged = True

    def redirect_home_utente(self):
        self.redirect(HomeUtenteView())
        self.logged = True
