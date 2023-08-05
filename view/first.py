from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from strategy import CercaLibriCatalogo
from utils.backend import CONTEXT_CATALOGO
from view.component import SidebarComponent
from view.component.catalogo import CatalogoComponent


class FirstView(View):
    def __init__(self):
        super().__init__()

    def create_layout(self):
        # content
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Login",),
                            style="button")
        catalogo = CatalogoComponent(CercaLibriCatalogo(), context=CONTEXT_CATALOGO)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(catalogo)

    def connect_buttons(self):
        login_button = self.get_button("Login")
        login_button.clicked.connect(self.go_to_login)

    def go_to_login(self):
        from .login import LoginView
        self.redirect(LoginView())
