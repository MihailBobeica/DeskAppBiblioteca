from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QScrollArea, QFrame, QGridLayout

from abstract.view import View
from utils import get_style, CATALOG_COLUMNS, is_empty
from view.gestione_libri_admin.libri_admin import LibroComponent

GRID_LABEL = "grid"


class CatalogoComponent(View):
    def create_layout(self) -> None:
        # content
        searchbar = QLineEdit()
        searchbar.textChanged.connect(self.update_grid)
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
        grid_layout = QGridLayout(content_widget)
        grid_layout.setObjectName(GRID_LABEL)

        self.default_grid()

        layout.addWidget(scroll_area)

        layout.setAlignment(Qt.AlignTop)

    def connect_buttons(self) -> None:
        pass

    def __init__(self):
        super().__init__()

    def default_grid(self):
        grid_layout: QGridLayout = self.findChild(QGridLayout, GRID_LABEL)

        from app import model_libro
        db_libri = model_libro.get()

        for index, db_libro in enumerate(db_libri):
            row = index // CATALOG_COLUMNS
            col = index % CATALOG_COLUMNS
            libro = LibroComponent(db_libro)
            grid_layout.addWidget(libro, row, col)

    def update_grid(self, text) -> None:
        grid_layout: QGridLayout = self.findChild(QGridLayout, GRID_LABEL)
        while grid_layout.count():
            child = grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        if is_empty(text):
            self.default_grid()
        else:
            from app import model_libro
            db_libri = model_libro.search(text)

            for index, db_libro in enumerate(db_libri):
                row = index // CATALOG_COLUMNS
                col = index % CATALOG_COLUMNS
                libro = LibroComponent(db_libro)
                grid_layout.addWidget(libro, row, col)
