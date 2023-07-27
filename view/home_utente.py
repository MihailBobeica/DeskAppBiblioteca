from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from component import Placeholder
from view.component import SidebarComponent
from view.scegli_prenotazione import ScegliPrenotazione


class HomeUtenteView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Prenota Posto",
                                    "Logout"),
                            style="button")
        content = Placeholder("Home utente")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(content)

    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)

    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)
      #  self.btn["Prenota Posto"].clicked.connect(self.show_prenota_schermata)

    def show_prenota_schermata(self):
        scegli_prenotazione_view = ScegliPrenotazione()
        self.main_window.set_view(scegli_prenotazione_view)

    def __init__(self):
        super().__init__()
