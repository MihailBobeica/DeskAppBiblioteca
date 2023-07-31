from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from view.component import SidebarComponent


class HomeOperatoreView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Registra prestito",
                                    "Logout"),
                            style="button")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)

    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)
        prestito_button = self.get_button("Registra prestito")
        prestito_button.clicked.connect(self.ricerca_prestito)


    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)

    def __init__(self):
        super().__init__()

    def ricerca_prestito(self):
        from view.registra_prestito import RegistraPrestito
        self.redirect(RegistraPrestito())