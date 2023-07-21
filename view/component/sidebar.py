from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout

from abstract.view import View
from utils import get_style, SIDEBAR_WIDTH


class SidebarComponent(View):
    def create_layout(self) -> None:
        # content
        self.setFixedWidth(SIDEBAR_WIDTH)
        self.setStyleSheet(get_style("sidebar"))

        # layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

    def connect_buttons(self) -> None:
        pass

    def __init__(self):
        super().__init__()
