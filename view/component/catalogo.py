from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout

from abstract.view import View
from utils import get_style


class CatalogoComponent(View):
    def create_layout(self) -> None:
        # content
        self.qle["searchbar"] = searchbar = QLineEdit()
        searchbar.setPlaceholderText("Ricerca")
        searchbar.setStyleSheet(get_style("input"))

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(searchbar)

        layout.setAlignment(Qt.AlignTop)

    def connect_buttons(self) -> None:
        pass

    def __init__(self):
        super().__init__()
