from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

from utils import get_style
from view import INPUT_WIDTH, INPUT_HEIGHT


class Login(QWidget):
    def __init__(self, parent_window: QWidget):
        super().__init__(parent_window)

        username_label = QLabel("Username")
        username_input = QLineEdit()
        username_input.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        username_input.setStyleSheet(get_style("input"))
        password_label = QLabel("Password")
        password_input = QLineEdit()
        password_input.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        password_input.setStyleSheet(get_style("input"))
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_submit = QPushButton("Login")
        self.btn_back = QPushButton("Indietro")

        h_layout = QHBoxLayout(self)
        v_layout = QVBoxLayout()
        h_layout.addLayout(v_layout)

        v_layout.addWidget(username_label)
        v_layout.addWidget(username_input)
        v_layout.addWidget(password_label)
        v_layout.addWidget(password_input)
        v_layout.addSpacing(40)
        v_layout.addWidget(self.btn_submit)
        v_layout.addWidget(self.btn_back)

        h_layout.setAlignment(Qt.AlignCenter)

        self.connect_buttons()

    def connect_buttons(self):
        from .first import First
        self.btn_back.clicked.connect(lambda: self.parent().change_view(First(self.parent())))
