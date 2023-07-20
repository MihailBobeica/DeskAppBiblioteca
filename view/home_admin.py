from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from component import Sidebar, Placeholder


class HomeAdminView(View):
    def create_layout(self):
        sidebar = Sidebar(self)
        self.add_buttons(sidebar.add_buttons(("Option 1",
                                              "Option 2",
                                              "Option 3",
                                              "Logout",)))
        content = Placeholder("Home admin")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(content)

    def connect_buttons(self):
        self.btn["Logout"].clicked.connect(self.send_logout_request)

    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)

    def __init__(self):
        super().__init__()
