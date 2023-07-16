from typing import Iterable, Dict

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QFrame, QLabel, QPushButton

from utils import get_style, create_buttons


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(200)
        self.setStyleSheet(get_style("sidebar"))

        self.lyt = QVBoxLayout(self)
        self.lyt.setAlignment(Qt.AlignTop)

    def add_buttons(self, labels: Iterable[str]) -> Dict[str, QPushButton]:
        return create_buttons(labels=labels, layout=self.lyt, style="button")


class Placeholder(QFrame):
    def __init__(self, placeholder):
        super().__init__()

        label = QLabel(placeholder)
        label.setAlignment(Qt.AlignCenter)
        self.lyt = QVBoxLayout(self)
        self.lyt.addWidget(label)
