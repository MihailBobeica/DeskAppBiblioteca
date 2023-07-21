from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QScrollArea, QFrame, QGridLayout

from abstract.view import View
from utils import get_style, CATALOG_COLUMNS
from view.component.libro import LibroComponent


class CatalogoComponent(View):
    def create_layout(self) -> None:
        # content
        searchbar = QLineEdit()
        searchbar.setPlaceholderText("Ricerca")
        searchbar.setStyleSheet(get_style("input"))


        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(searchbar)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the grid layout
        content_widget = QFrame(scroll_area)
        scroll_area.setWidget(content_widget)

        # Create a grid layout for the content widget
        grid_layout = QGridLayout(content_widget)

        from app import model_libro
        db_libri = model_libro.get(15)

        for index, db_libro in enumerate(db_libri):
            row = index // CATALOG_COLUMNS
            col = index % CATALOG_COLUMNS
            libro = LibroComponent(db_libro)
            grid_layout.addWidget(libro, row, col)

        # Set the content widget as the central widget
        layout.addWidget(scroll_area)

        layout.setAlignment(Qt.AlignTop)

    def connect_buttons(self) -> None:
        pass

    def __init__(self):
        super().__init__()
