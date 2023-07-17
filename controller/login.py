from typing import Optional, Dict

from PySide6.QtWidgets import QMessageBox

from abstract.controller import Controller
from abstract.model import Model
from abstract.view import View
from database import ADMIN, OPERATORE, UTENTE
from model.utente import Utente
from utils import check_password
from view.home_admin import HomeAdminView
from view.home_operatore import HomeOperatoreView
from view.home_utente import HomeUtenteView

BAD_CREDENTIALS_TITLE = "Accesso non riuscito"
BAD_CREDENTIALS_MESSAGE = "Credenziali di accesso errate"


class LoginController(Controller):
    def __init__(self, models: Optional[Dict[str, Model]] = None, views: Optional[Dict[str, View]] = None):
        super().__init__(models, views)

    def update(self, message: str, data: dict):
        if message == "login":
            self.login(data["username"], data["password"])

    def login(self, username: str, password: str) -> None:
        utente = Utente.by_username(username)
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
        print(utente.password)
        print(utente.ruolo)

    def bad_credentials_popup(self):
        QMessageBox.information(self.main_window.centralWidget(),
                                BAD_CREDENTIALS_TITLE,
                                BAD_CREDENTIALS_MESSAGE)

    def redirect(self, view: View):
        self.main_window.set_view(view)

    def redirect_home_admin(self):
        self.redirect(HomeAdminView())

    def redirect_home_operatore(self):
        self.redirect(HomeOperatoreView())

    def redirect_home_utente(self):
        self.redirect(HomeUtenteView())

