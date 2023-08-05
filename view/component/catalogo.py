from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QScrollArea, QFrame, QGridLayout

from abstract.view import View
from strategy.search import RicercaStrategy
from utils.ui import get_style, CATALOG_COLUMNS
from view.component.libro import LibroComponent


class CatalogoComponent(View):
    def create_layout(self) -> None:
        # content
        searchbar = QLineEdit()
        searchbar.textChanged.connect(self.search)
        searchbar.setPlaceholderText("Ricerca per titolo o autore")
        searchbar.setStyleSheet(get_style("input"))

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(searchbar)

        scroll_area = QScrollArea(self)
        scroll_area.setStyleSheet(get_style("catalogo"))
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the grid layout
        content_widget = QFrame(scroll_area)
        scroll_area.setWidget(content_widget)

        # Create a grid layout for the content widget
        self.grid_layout = QGridLayout(content_widget)

        layout.addWidget(scroll_area)

        layout.setAlignment(Qt.AlignTop)

    def __init__(self, search_strategy: RicercaStrategy, context: Optional[str] = None):
        self.search_strategy = search_strategy
        self.context = context
        self.grid_layout: Optional[QGridLayout] = None

        super().__init__()

        self.search()

    def attach_controllers(self) -> None:
        from app import controller_catalogo
        self.attach(controller_catalogo)

    def search(self, text: Optional[str] = None) -> None:
        self.notify(message="search",
                    data={"catalogo": self,
                          "text": text})

    def load_grid(self, data_list: list[dict[str, object]]) -> None:
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for index, data in enumerate(data_list):
            row = index // CATALOG_COLUMNS
            col = index % CATALOG_COLUMNS
            libro = LibroComponent(data, self.context)
            self.grid_layout.addWidget(libro, row, col)
