from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from component import Sidebar, Placeholder


class HomeUtenteView(View):
    def create_layout(self):
        sidebar = Sidebar()
        self.add_buttons(sidebar.add_buttons(("Option 1",
                                              "Option 2",
                                              "Option 3",
                                              "Option 4",)))
        content = Placeholder("Home utente")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(content)

    def connect_buttons(self):
        pass

    def __init__(self):
        super().__init__()
