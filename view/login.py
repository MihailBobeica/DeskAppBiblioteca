from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

from abstract.view import View
from utils import get_style
from view import INPUT_WIDTH, INPUT_HEIGHT


class LoginView(View):
    def create_layout(self):
        # content
        username_label = QLabel("Username")
        username_input = self.qle["username"] = QLineEdit()
        username_input.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        username_input.setStyleSheet(get_style("input"))

        password_label = QLabel("Password")
        password_input = self.qle["password"] = QLineEdit()
        password_input.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        password_input.setStyleSheet(get_style("input"))
        password_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn_submit = self.btn["submit"] = QPushButton("Login")
        btn_back = self.btn["back"] = QPushButton("Indietro")

        # layout
        h_layout = QHBoxLayout(self)
        v_layout = QVBoxLayout()
        h_layout.addLayout(v_layout)

        v_layout.addWidget(username_label)
        v_layout.addWidget(username_input)
        v_layout.addWidget(password_label)
        v_layout.addWidget(password_input)
        v_layout.addSpacing(40)
        v_layout.addWidget(btn_submit)
        v_layout.addWidget(btn_back)

        h_layout.setAlignment(Qt.AlignCenter)

    def connect_buttons(self):
        self.btn["back"].clicked.connect(self.go_back)
        self.btn["submit"].clicked.connect(self.send_login_data)

    def __init__(self):
        super().__init__()

    def attach_controllers(self):
        from app import controller_login
        self.attach(controller_login)

    def go_back(self):
        from .first import FirstView
        self.redirect(FirstView())

    def get_login_data(self):
        return {"username": self.qle["username"].text(),
                "password": self.qle["password"].text()}

    def send_login_data(self):
        self.notify("login", self.get_login_data())
