from abstract.controller import Controller
from database import ADMIN, OPERATORE, UTENTE
from model.utente import Utente
from utils import check_password, is_empty
from view.home_admin import HomeAdminView
from view.home_operatore import HomeOperatoreView
from view.home_utente import HomeUtenteView

ACCESS_DENIED_TITLE = "Accesso non riuscito"
BAD_CREDENTIALS_MESSAGE = "Credenziali di accesso errate"
NO_USERNAME_MESSAGE = "Non hai inserito l'username"
NO_PASSWORD_MESSAGE = "Non hai inserito la password"


class LoginController(Controller):
    def __init__(self):
        super().__init__()

    def receive_message(self, message: str, data: dict):
        if message == "login":
            self.login(data["username"], data["password"])

    def login(self, username: str, password: str) -> None:
        utente = Utente.by_username(username)
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

    def redirect_home_operatore(self):
        self.redirect(HomeOperatoreView())

    def redirect_home_utente(self):
        self.redirect(HomeUtenteView())
