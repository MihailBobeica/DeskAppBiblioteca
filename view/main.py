from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFrame

from abstract import BoundedView
from factory import HomepageFactory
from utils.strings import *
from utils.ui import HOME_ICON, quick_alert


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.displayed_view: Optional[BoundedView] = None
        self.initialize()
        self.create_menu()
        self.create_layout()

    def initialize(self) -> None:
        self.setWindowTitle(APP_NAME)
        width, height = 800, 600
        self.resize(width, height)
        self.setMinimumSize(width, height)

    def create_menu(self) -> None:
        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu.addAction("Quit")

        help_menu = menu.addMenu("Help")
        help_menu.addAction("Docs")

    def create_layout(self) -> None:
        main_widget = QFrame()

        buttons_container = QFrame()

        icon_home = QIcon(HOME_ICON)
        button_home = QPushButton()
        button_home.clicked.connect(self.go_home)
        button_home.setIcon(icon_home)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 0)

        h_layout.addStretch()
        h_layout.addWidget(button_home)
        h_layout.addStretch()

        buttons_container.setLayout(h_layout)

        layout.addWidget(buttons_container)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def set_view(self, view: BoundedView) -> None:
        layout = self.centralWidget().layout()

        if self.displayed_view:
            self.displayed_view: BoundedView
            self.displayed_view.deleteLater()

        self.displayed_view = view
        layout.insertWidget(0, self.displayed_view)

    def go_home(self) -> None:
        homepage = HomepageFactory.create_homepage(self.displayed_view)
        if homepage:
            self.set_view(homepage)
        else:
            quick_alert(parent=self,
                        title=QUICK_ALERT_GO_HOME_TITLE,
                        message=QUICK_ALERT_GO_HOME_MESSAGE)
