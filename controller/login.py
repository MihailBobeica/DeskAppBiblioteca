from typing import Optional, Dict

from abstract.controller import Controller
from abstract.model import Model
from abstract.view import View
from database import ADMIN, OPERATORE, UTENTE
from utils import check_password


class LoginController(Controller):
    def __init__(self, models: Optional[Dict[str, Model]] = None, views: Optional[Dict[str, View]] = None):
        super().__init__(models, views)

    def login(self, username, password):
        utente = self.models["utente"].get_utente_by_username(username)
        if utente is None:
            return 0  # TODO: Make a notification that the user does not exist
        if not check_password(password, utente.password):
            return 0  # TODO: make a notification that the credentials are incorrect
        if utente.ruolo == ADMIN:
            return 0  # TODO: redirect to home admin
        if utente.ruolo == OPERATORE:
            return 1  # TODO: redirect to home operatore
        if utente.ruolo == UTENTE:
            return 2  # TODO: redirect to home utente
        print(utente.password)
        print(utente.ruolo)

    def update(self, message: str, data: dict):
        if message == "login":
            self.login(data["username"], data["password"])
