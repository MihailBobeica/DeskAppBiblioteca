from PySide6.QtWidgets import QHBoxLayout
from typing import Optional
from abstract.view import View
from view.component import SidebarComponent


class HomeAdminView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Gestione operatori",
                                    "Inserisci libro",
                                    "Gestione libri",
                                    "Gestione utenti",
                                    "Visualizza statistiche",
                                    "Logout",),
                            style="button")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)

    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)
        gestione_operatori_button = self.get_button("Gestione operatori")
        gestione_operatori_button.clicked.connect(self.gestione_operatori)
        inserisci_libro_button = self.get_button("Inserisci libro")
        inserisci_libro_button.clicked.connect(self.inserisci_libro)
        ricerca_libro_button = self.get_button("Gestione libri")
        ricerca_libro_button.clicked.connect(self.ricerca_libro)
        gestione_utenti_button = self.get_button("Gestione utenti")
        gestione_utenti_button.clicked.connect(self.gestione_utenti)
        statistiche_button = self.get_button("Visualizza statistiche")
        statistiche_button.clicked.connect(self.statistiche)

    def attach_controllers(self) -> None:
        from app import controller_logout,controller_gestione_operatori, controller_statistiche
        self.attach(controller_logout)
        self.attach(controller_gestione_operatori)
        self.attach(controller_statistiche)

    def __init__(self):
        super().__init__()

    def gestione_operatori(self, text: Optional[str] = None) -> None:
        self.notify(message="gestione_operatori")


    def inserisci_libro(self):
        self.notify(message="inserisci_libro")

    def ricerca_libro(self):
        self.notify(message="ricerca_libro")

    def gestione_utenti(self):
        self.notify(message="gestione_utenti")

    def statistiche(self):
        self.notify(message="visualizza_statistiche")
