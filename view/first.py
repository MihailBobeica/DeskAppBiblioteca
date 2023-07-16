from abc import ABC
from typing import Dict, Optional, Type

from PySide6.QtWidgets import QHBoxLayout, QMainWindow

from abstract.model import Model
from abstract.view import View
from component import Sidebar, Placeholder


class FirstView(View):
    def __init__(self, models: Optional[Dict[str, Type[Model]]] = None):
        super().__init__(models)

    def create_layout(self):
        # content
        sidebar = Sidebar()
        self.add_buttons(sidebar.add_buttons(("Login",)))
        content = Placeholder("Catalogo")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(content)

    def connect_buttons(self):
        from .login import LoginView
        self.btn["Login"].clicked.connect(lambda: self.main_window.set_view(LoginView()))
