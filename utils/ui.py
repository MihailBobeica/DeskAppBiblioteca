import traceback
from os import path
from typing import Iterable

from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLayout, QPushButton, QMessageBox, QLabel

INPUT_WIDTH = 320
INPUT_HEIGHT = 32
SIDEBAR_WIDTH = 200
BOX_WIDTH = 180
CATALOG_COLUMNS = 2
RESULTS_LIMIT = 15
LIBRO_VIEW_WIDTH = 320
LIBRO_VIEW_HEIGHT = 480

PATH_CSS = "src/css"
PATH_IMAGE = "src/img"
FOLDER_COVER = "copertina"
FOLDER_UI = "ui"


def get_style(css_file: str) -> str:
    try:
        return open(path.join(PATH_CSS, f"{css_file}.css")).read().strip()
    except FileNotFoundError:
        traceback.print_exc()
        return ""


def create_buttons(labels: Iterable[str], layout: QLayout, style=None) -> dict[str, QPushButton]:
    d: dict[str, QPushButton] = {label: QPushButton(label) for label in labels}
    if (style is not None) and (isinstance(style, str)):
        for btn in d.values():
            btn.setStyleSheet(get_style(style))
            layout.addWidget(btn)
    return d


def get_cover_image(image: str) -> str:
    return path.join(path.join(PATH_IMAGE, FOLDER_COVER), image)


def get_ui_image(image_name: str) -> str:
    return path.join(path.join(PATH_IMAGE, FOLDER_UI), image_name)


ARROW_BACK_ICON: str = get_ui_image("arrow_back_icon.png")
# ARROW_FORWARD_ICON: str = get_ui_image("arrow_forward_icon.png")
HOME_ICON: str = get_ui_image("home_icon.png")


def label_autori(autori: str) -> str:
    if "," in autori:
        return f"Autori: {autori}"
    return f"Autore: {autori}"


def quick_alert(parent, title: str, message: str, seconds: int = 3):
    alert = QMessageBox(parent)
    alert.setIcon(QMessageBox.Information)
    alert.setWindowTitle(title)
    alert.setText(message)

    timer = QTimer()
    timer.timeout.connect(alert.close)
    timer.start(int(seconds * 1000))

    alert.exec_()


def font_16(label: QLabel):
    font = QFont()
    font.setPointSize(16)
    label.setFont(font)
    return label
