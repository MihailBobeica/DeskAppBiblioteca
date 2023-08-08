from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QScrollArea, QFrame, QGridLayout

from abstract.view import View
from factory import SearchStrategyFactory
from strategy.search import SearchStrategy
from utils.backend import OBJ_NAME_SEARCHBAR
from utils.ui import get_style, CATALOG_COLUMNS
from view.component.libro import LibroComponent


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
        search_strategy_factory = SearchStrategyFactory()
        self.search_strategy = search_strategy_factory.create_search_strategy(self.context)

        self.searchbar = QLineEdit()
        self.grid_layout: Optional[QGridLayout] = None

        super().__init__()

        self.search()

    def update(self):
        searchbar = self.get_line_edit(OBJ_NAME_SEARCHBAR)
        self.search(searchbar.text())

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
            libro = LibroComponent(data, self.context)  # TODO put a factory
            self.grid_layout.addWidget(libro, row, col)
