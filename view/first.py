from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from component import Sidebar
from view.component.catalogo import CatalogoComponent


class FirstView(View):
    def __init__(self):
        super().__init__()

    def create_layout(self):
        # content
        sidebar = Sidebar()
        self.add_buttons(sidebar.add_buttons(("Login",)))
        catalogo = CatalogoComponent()

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(catalogo)

    def connect_buttons(self):
        from .login import LoginView
        self.btn["Login"].clicked.connect(lambda: self.main_window.set_view(LoginView()))
