from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout

from abstract.view import View


class SidebarComponent(View):
    def create_layout(self) -> None:
        # content

        # layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

    def connect_buttons(self) -> None:
        pass

    def __init__(self):
        super().__init__()
