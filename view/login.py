from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QHBoxLayout, QVBoxLayout

from abstract.view import View
from utils.ui import get_style, INPUT_WIDTH, INPUT_HEIGHT


class LoginView(View):
    def create_layout(self):
        # content
        username_label = QLabel("Username")
        username_input = QLineEdit()
        username_input.setObjectName("username")
        username_input.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        username_input.setStyleSheet(get_style("input"))

        password_label = QLabel("Password")
        password_input = QLineEdit()
        password_input.setObjectName("password")
        password_input.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        password_input.setStyleSheet(get_style("input"))
        password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # layout
        h_layout = QHBoxLayout(self)
        v_layout = QVBoxLayout()
        h_layout.addLayout(v_layout)

        v_layout.addStretch()
        v_layout.addWidget(username_label)
        v_layout.addWidget(username_input)
        v_layout.addWidget(password_label)
        v_layout.addWidget(password_input)
        v_layout.addSpacing(48)
        self.add_buttons(labels=("Login",),
                         layout=v_layout, )
        v_layout.addStretch()

        h_layout.setAlignment(Qt.AlignCenter)

    def connect_buttons(self):
        button_submit = self.get_button("Login")
        button_submit.clicked.connect(self.send_login_data)

    def __init__(self):
        super().__init__()

    def attach_controllers(self):
        from app import controller_login
        self.attach(controller_login)

    def get_login_data(self):
        line_edit_username = self.get_line_edit("username")
        line_edit_password = self.get_line_edit("password")
        return {"username": line_edit_username.text(),
                "password": line_edit_password.text()}

    def send_login_data(self):
        self.notify("login", self.get_login_data())
