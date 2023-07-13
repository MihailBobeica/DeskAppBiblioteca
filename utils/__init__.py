from os import path
import traceback
from typing import TypedDict, Iterable

from PySide6.QtWidgets import QPushButton, QLayout

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
