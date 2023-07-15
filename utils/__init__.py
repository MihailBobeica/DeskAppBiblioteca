from os import path
import traceback
from typing import TypedDict, Iterable, Tuple

from PySide6.QtWidgets import QPushButton, QLayout
import bcrypt

PATH_CSS = "src/css"


class LabeledButton(TypedDict):
    label: str
    button: QPushButton


def get_style(css_file: str) -> str:
    try:
        return open(path.join(PATH_CSS, f"{css_file}.css")).read().strip()
    except FileNotFoundError:
        traceback.print_exc()
        return ""


def create_buttons(labels: Iterable[str], layout: QLayout, style=None) -> LabeledButton:
    d: LabeledButton = {label: QPushButton(label) for label in labels}
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
