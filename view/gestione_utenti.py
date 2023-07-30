from PySide6.QtWidgets import QHBoxLayout
from view.ricerca_operatore import RicercaView
from abstract.view import View
from component import Placeholder
from view.component import SidebarComponent


class GestioneUtentiView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Visualizza utente",
                                    "Visualizza cronologia",
                                    "Logout",),
                            style="button")
        content = Placeholder("Gestione utenti")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(content)




    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)
        visualizza_utente_button = self.get_button("Visualizza utente")
        visualizza_utente_button.clicked.connect(self.visualizza_utente)
        visualizza_cronologia_button = self.get_button("Visualizza cronologia")
        visualizza_cronologia_button.clicked.connect(self.visualizza_cronologia)



    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)

    def __init__(self):
        super().__init__()

    def visualizza_utente(self):
        from .visualizza_utente import VisualizzaUtente
        self.redirect(VisualizzaUtente())

    def visualizza_cronologia(self):
        pass