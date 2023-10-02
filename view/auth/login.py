from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame, QPushButton

from abstract.view import View
from utils.ui import get_style, INPUT_WIDTH, INPUT_HEIGHT


class LoginView(View):
    def create_layout(self):
        # content
        username_label = QLabel("Username")
        self.username.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        self.username.setStyleSheet(get_style("input"))

        password_label = QLabel("Password")
        self.password.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        self.password.setStyleSheet(get_style("input"))
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        button_submit = QPushButton("Login")
        button_submit.clicked.connect(self.send_login_data)

        # layout
        h_layout = QHBoxLayout(self)
        h_layout.setAlignment(Qt.AlignCenter)
        v_layout = QVBoxLayout()
        h_layout.addLayout(v_layout)

        v_layout.addStretch()
        v_layout.addWidget(username_label)
        v_layout.addWidget(self.username)
        v_layout.addWidget(password_label)
        v_layout.addWidget(self.password)

        button_container = QFrame()
        c_layout = QHBoxLayout()
        c_layout.setAlignment(Qt.AlignCenter)

        c_layout.addWidget(button_submit)

        button_container.setLayout(c_layout)

        v_layout.addWidget(button_container)

        v_layout.addStretch()

    def __init__(self):
        self.username = QLineEdit()
        self.password = QLineEdit()
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_login
        self.attach(controller_login)

    def get_login_data(self) -> dict:
        login_data = {"username": self.username.text(),
                      "password": self.password.text()}
        return login_data

    def send_login_data(self) -> None:
        self.notify("login", self.get_login_data())
