from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QScrollArea, QFrame, QGridLayout

from abstract.view import View
from factory import SearchStrategyFactory, LibroComponentFactory
from utils.ui import get_style, CATALOG_COLUMNS


class CatalogoComponent(View):
    def create_layout(self) -> None:
        # content
        self.searchbar.textChanged.connect(self.search)
        self.searchbar.setPlaceholderText("Ricerca per titolo o autore")
        self.searchbar.setStyleSheet(get_style("input"))

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.searchbar)

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

    def __init__(self, context: str):
        self.context = context
        self.search_strategy = SearchStrategyFactory.create_search_strategy(self.context)

        self.searchbar = QLineEdit()
        self.grid_layout: Optional[QGridLayout] = None

        super().__init__()

        self.search()

    def update(self):
        self.search(self.searchbar.text())

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
            if t := child.widget():
                t.deleteLater()

        for index, data in enumerate(data_list):
            row = index // CATALOG_COLUMNS
            col = index % CATALOG_COLUMNS
            libro = LibroComponentFactory.create_libro_component(self, self.context, data)
            self.grid_layout.addWidget(libro, row, col)
