from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QLabel, QPushButton

from utils import get_style, create_buttons

from view.first import First
from view.login import Login


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_window()
        self.create_menu()

        first = First(self)
        login = Login(self)
        self.setCentralWidget(first)
        # self.init_layout()

    def init_window(self):
        self.setWindowTitle("Catalogo")
        width, height = 640, 480
        self.resize(width, height)
        self.setMinimumSize(width, height)

    def create_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu.addAction("Quit")

        help_menu = menu.addMenu("Help")
        help_menu.addAction("Docs")  # links to the docs

    def init_layout(self):
        # Create a central widget for the main window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create the layout
        layout = QHBoxLayout(central_widget)

        # Create the sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet(get_style("sidebar"))

        # create the sidebar layout
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setAlignment(Qt.AlignTop)
        sidebar_btn = create_buttons(labels=("Libri in prestito",
                                             "Libri prenotati",
                                             "Lista di osservazione",
                                             "Catalogo",
                                             "Sanzioni",
                                             "Info",
                                             "Logout"),
                                     layout=sidebar_layout,
                                     style="button")

        sidebar_btn["Libri in prestito"].clicked.connect(self.change_layout)

        # Create the content area
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_label = QLabel("Main Content")
        content_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(content_label)

        # Add the sidebar and content to the main layout
        layout.addWidget(sidebar)
        layout.addWidget(content)

    def change_layout(self):
        # Create a central widget for the main window
        central_widget = QWidget(self)

        # Create the layout
        layout = QHBoxLayout(central_widget)

        # Create the sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet(get_style("sidebar"))

        # create the sidebar layout
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setAlignment(Qt.AlignTop)
        sidebar_btn = create_buttons(labels=("Libri in prestito",
                                             "Libri prenotati"),
                                     layout=sidebar_layout,
                                     style="button")

        # Create the content area
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_label = QLabel("Main Content")
        content_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(content_label)

        # Add the sidebar and content to the main layout
        layout.addWidget(sidebar)
        layout.addWidget(content)

        self.setCentralWidget(central_widget)
