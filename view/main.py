from typing import Type

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QMessageBox

from abstract import BoundedView
from utils.backend import HISTORY_LIMIT
from utils.strings import *
from utils.ui import ARROW_BACK_ICON, HOME_ICON
from view.homepage import HomeGuestView


def quick_alert(parent, title: str, message: str, seconds: int = 3):
    alert = QMessageBox(parent)
    alert.setIcon(QMessageBox.Information)
    alert.setWindowTitle(title)
    alert.setText(message)

    timer = QTimer()
    timer.timeout.connect(alert.close)
    timer.start(int(seconds * 1000))

    alert.exec_()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cronologia: list[BoundedView] = list()
        self.index = 0
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

        icon_back = QIcon(ARROW_BACK_ICON)
        button_back = QPushButton()
        button_back.clicked.connect(self.go_back)
        button_back.setIcon(icon_back)

        icon_home = QIcon(HOME_ICON)
        button_home = QPushButton()
        button_home.clicked.connect(self.go_home)
        button_home.setIcon(icon_home)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 0)

        h_layout.addStretch()
        h_layout.addWidget(button_back)
        h_layout.addWidget(button_home)
        h_layout.addStretch()

        buttons_container.setLayout(h_layout)

        layout.addWidget(buttons_container)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def get_view_name(self, increment: int = 0) -> str:
        self.index += increment
        return f"{CONTENT}_{self.index}"

    def get_this_view(self) -> BoundedView:
        this_view_name = self.get_view_name()
        this_view: BoundedView = self.findChild(QFrame, this_view_name, Qt.FindChildrenRecursively)
        return this_view

    def set_view(self, view: BoundedView, navigate: bool = False) -> None:
        this_view = self.get_this_view()
        layout = self.centralWidget().layout()

        if this_view:
            if navigate:
                this_view.deleteLater()
            else:
                self.cronologia.append(this_view)
                if len(self.cronologia) > HISTORY_LIMIT:
                    lru_view: BoundedView = self.cronologia.pop(0)
                    lru_view.deleteLater()

            this_view.hide()
            layout.removeWidget(this_view)

        next_view_name = self.get_view_name(increment=1)
        view.setObjectName(next_view_name)
        layout.insertWidget(0, view)
        view.show()
        # self.update_view(type(view))

    def replace(self, view: BoundedView):
        self.set_view(view, navigate=True)

    def update_view(self, view: Type[BoundedView]):
        for index, v in enumerate(self.cronologia):
            if isinstance(v, view):
                self.cronologia[index] = view()

    def go_back(self) -> None:
        if self.cronologia:
            last_view: BoundedView = self.cronologia.pop()
            last_view.update()
            self.replace(last_view)
            return

        quick_alert(parent=self,
                    title=QUICK_ALERT_GO_BACK_TITLE,
                    message=QUICK_ALERT_GO_BACK_MESSAGE)

    def go_home(self) -> None:
        return
        # this_view = self.get_this_view()
        # not_on_home_page = not isinstance(this_view, HomePageView)
        # if not_on_home_page:
        #     self.set_view(HomePageView())
        #     return
        #
        # quick_alert(parent=self,
        #             title=QUICK_ALERT_GO_HOME_TITLE,
        #             message=QUICK_ALERT_GO_HOME_MESSAGE,
        #             seconds=2)

    def reset_history(self):
        self.cronologia = list()
