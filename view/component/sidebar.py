from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton

from abstract.view import View
from utils.ui import get_style, SIDEBAR_WIDTH


class SidebarComponent(View):
    def create_layout(self) -> None:
        # content
        self.setFixedWidth(SIDEBAR_WIDTH)
        self.setStyleSheet(get_style("sidebar"))

        # layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

    def __init__(self):
        self.button: dict[str, QPushButton] = dict()
        super().__init__()

    def set_buttons(self, labels: tuple[str, ...]):
        layout = self.layout()
        for label in labels:
            button = self.button[label] = QPushButton(label)
            button.setStyleSheet(get_style("button"))
            layout.addWidget(button)
