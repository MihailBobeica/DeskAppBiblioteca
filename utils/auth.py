import bcrypt

from database import Utente as DbUtente


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
    user = None
    logged = ""

    @staticmethod
    def logged_as(user: DbUtente):
        Auth.user = user
        Auth.logged = user.ruolo

    @staticmethod
    def is_logged_as(ruolo: str):
        return Auth.logged == ruolo

    @staticmethod
    def is_logged() -> bool:
        return Auth.user is not None

    @staticmethod
    def logout():
        Auth.user = None
        Auth.logged = ""
