from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QScrollArea, QFrame, QGridLayout

from abstract.view import View
from utils.ui import get_style, CATALOG_COLUMNS
from utils.backend import is_empty
from view.gestione_libri_admin.libro_component_admin import LibroAdminView
from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QScrollArea, QFrame, QGridLayout, QLabel

from abstract.view import View
from database import BoundedDbModel
from factory.libro_component import LibroComponentFactory
from factory.search_strategy import SearchStrategyFactory
from utils.key import KeyContext, KeyDb
from utils.request import Request
from utils.ui import get_style, CATALOG_COLUMNS

GRID_LABEL = "grid"


class CatalogoAdminView(View):
    '''def create_layout(self) -> None:
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
            libro = LibroAdminView(db_libro)
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
                libro = LibroAdminView(db_libro)
                grid_layout.addWidget(libro, row, col)'''

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

    def __init__(self, context: KeyContext):
        self.context = context
        search_strategy_factory = SearchStrategyFactory()
        self.search_strategy = search_strategy_factory.create(self.context)

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
        self.notify(message=Request.SEARCH,
                    data={"catalogo": self,
                          "text": text})

    def load_grid(self, data_list: list[dict[KeyDb, BoundedDbModel]]) -> None:
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if t := child.widget():
                t.deleteLater()

        if not data_list:
            label_libri_non_trovati = QLabel("Non è stato trovato alcun libro.")
            self.grid_layout.addWidget(label_libri_non_trovati, 0, 0)

        for index, data in enumerate(data_list):
            row = index // CATALOG_COLUMNS
            col = index % CATALOG_COLUMNS
            libro_component_factory = LibroComponentFactory(catalogo=self, data=data)
            libro = libro_component_factory.create(self.context)
            self.grid_layout.addWidget(libro, row, col)

