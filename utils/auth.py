from typing import Optional

import bcrypt

from database import Utente as DbUtente
from utils.key import KeyAuth
from utils.role import *


def hash_password(password: str) -> str:
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password.decode()


def check_password(password: str, stored_password: str) -> bool:
    password = password.encode("utf-8")
    is_matched = bcrypt.checkpw(password, stored_password.encode("utf-8"))
    return is_matched


class Auth:
    def __init__(self):
        self.user: Optional[DbUtente] = None

        self.key: dict[str, KeyAuth] = dict()

        self.key[ADMIN] = KeyAuth.ADMIN
        self.key[OPERATORE] = KeyAuth.OPERATORE
        self.key[UTENTE] = KeyAuth.UTENTE

    def login_as(self, user: DbUtente) -> None:
        self.user = user

    def is_logged_as(self, ruolo: str) -> bool:
        if self.user:
            return self.user.ruolo == ruolo
        return False

    def logout(self):
        self.user = None

    def get_key(self) -> KeyAuth:
        if self.user:
            return self.key.get(self.user.ruolo)
        else:
            return KeyAuth.GUEST


auth = Auth()
