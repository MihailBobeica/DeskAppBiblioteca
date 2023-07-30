from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from view.component import SidebarComponent


class HomeOperatoreView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Option 1",
                                    "Logout"),
                            style="button")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)

    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)

    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)

    def __init__(self):
        super().__init__()
