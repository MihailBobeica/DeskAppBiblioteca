from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QScrollArea, QFrame, QGridLayout

from abstract.view import View
from strategy.search import CercaLibriStrategy
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

    def __init__(self, cerca_libri_strategy: CercaLibriStrategy):
        self.grid_layout: Optional[QGridLayout] = None
        self.cerca_libri_strategy = cerca_libri_strategy

        super().__init__()

        self.search()

    def attach_controllers(self) -> None:
        from app import controller_catalogo
        self.attach(controller_catalogo)

    def search(self, text: Optional[str] = None) -> None:
        self.notify(message="search",
                    data={"catalogo": self,
                          "text": text})

    def load_grid(self, db_libri) -> None:
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for index, db_libro in enumerate(db_libri):
            row = index // CATALOG_COLUMNS
            col = index % CATALOG_COLUMNS
            libro = LibroComponent(db_libro)
            self.grid_layout.addWidget(libro, row, col)
