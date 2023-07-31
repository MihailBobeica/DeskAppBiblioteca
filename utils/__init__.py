import uuid
from os import path
import traceback
from typing import Iterable, Dict

from PySide6.QtWidgets import QPushButton, QLayout
import bcrypt

PATH_CSS = "src/css"
ADMIN = "admin"
OPERATORE = "operatore"
UTENTE = "utente"
Posti = 20


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
