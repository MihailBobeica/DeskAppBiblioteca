from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QMessageBox

from abstract import BoundedView
from utils import ARROW_BACK_ICON, HISTORY_LIMIT, CONTENT, APP_NAME


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

        # icon_forward = QIcon(ARROW_FORWARD_ICON)
        # button_forward = QPushButton()
        # button_forward.setObjectName(BUTTON_FORWARD)
        # button_forward.setIcon(icon_forward)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 0)

        h_layout.addStretch()
        h_layout.addWidget(button_back)
        # h_layout.addWidget(button_forward)
        h_layout.addStretch()

        buttons_container.setLayout(h_layout)

        layout.addWidget(buttons_container)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def get_content_name(self, increment: int = 0) -> str:
        self.index += increment
        return f"{CONTENT}_{self.index}"

    def set_view(self, view: BoundedView, navigate: bool = False) -> None:
        content_name = self.get_content_name()
        content: BoundedView = self.findChild(QFrame, content_name, Qt.FindChildrenRecursively)
        layout = self.centralWidget().layout()

        if content:
            if not navigate:
                self.cronologia.append(content)
                if len(self.cronologia) > HISTORY_LIMIT:
                    least_recently_used: BoundedView = self.cronologia.pop(0)
                    least_recently_used.deleteLater()
            content.hide()
            layout.removeWidget(content)

        content_name = self.get_content_name(increment=1)
        view.setObjectName(content_name)
        layout.insertWidget(0, view)
        view.show()

    def go_back(self) -> None:
        if self.cronologia:
            last_view: BoundedView = self.cronologia.pop()
            self.set_view(last_view, navigate=True)
            return

        alert = QMessageBox()
        alert.setIcon(QMessageBox.Information)
        alert.setWindowTitle("Cronologia vuota")
        alert.setText("La tua cronologia di navigazione\nè attualmente vuota")

        timer = QTimer()
        timer.timeout.connect(alert.close)
        timer.start(3000)

        alert.exec_()
