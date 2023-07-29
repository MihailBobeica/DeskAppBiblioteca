import traceback
import uuid
from datetime import datetime
from os import path
from typing import Iterable, Dict

import bcrypt
from PySide6.QtWidgets import QPushButton, QLayout

PATH_CSS = "src/css"
ADMIN = "admin"
OPERATORE = "operatore"
UTENTE = "utente"
SIDEBAR_WIDTH = 200
PATH_IMAGE = "src/img"
CATALOG_COLUMNS = 2
RESULTS_LIMIT = 15
POSTI = 20

BUTTON_BACK = "indietro"
BUTTON_FORWARD = "avanti"


def get_style(css_file: str) -> str:
    try:
        return open(path.join(PATH_CSS, f"{css_file}.css")).read().strip()
    except FileNotFoundError:
        traceback.print_exc()
        return ""


def create_buttons(labels: Iterable[str], layout: QLayout, style=None) -> Dict[str, QPushButton]:
    d: Dict[str, QPushButton] = {label: QPushButton(label) for label in labels}
    if (style is not None) and (isinstance(style, str)):
        for btn in d.values():
            btn.setStyleSheet(get_style(style))
            layout.addWidget(btn)
    return d


def hash_password(password: str) -> str:
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password.decode()


def check_password(password: str, stored_password: str) -> bool:
    password = password.encode("utf-8")
    is_matched = bcrypt.checkpw(password, stored_password.encode("utf-8"))
    return is_matched


def get_label(label: str):
    if (label is None) or (len(label) == 0):
        return uuid.uuid4()
    return label


def is_empty(string: str) -> bool:
    return (string is None) or (len(string) == 0)


def to_year(year: str) -> datetime:
    datetime_format = "%Y"
    datetime_year = datetime.strptime(year, datetime_format)
    return datetime_year


def get_image_path(image: str) -> str:
    return path.join(path.join(PATH_IMAGE, "copertina"), image)


def get_ui_image(image_name: str) -> str:
    return path.join(path.join(PATH_IMAGE, "ui"), image_name)


def label_autori(autori: str) -> str:
    if "," in autori:
        return f"Autori: {autori}"
    return f"Autore: {autori}"


class Auth:
    user = None
    logged = ""

    @staticmethod
    def logged_as(user):  # TODO: add type hint
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


ARROW_BACK_ICON: str = get_ui_image("arrow_back_icon.png")
ARROW_FORWARD_ICON: str = get_ui_image("arrow_forward_icon.png")
HOME_ICON: str = get_ui_image("home_icon.png")

HISTORY_LIMIT = 5

CONTENT = "main_content"

APP_NAME = "App Gestione Biblioteca"

QUICK_ALERT_GO_HOME_TITLE = "Home page"
QUICK_ALERT_GO_HOME_MESSAGE = "Sei già nella schermata principale."
QUICK_ALERT_GO_BACK_TITLE = "Cronologia vuota"
QUICK_ALERT_GO_BACK_MESSAGE = "La tua cronologia di navigazione" \
                              "\nè attualmente vuota."


