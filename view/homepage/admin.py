from PySide6.QtWidgets import QHBoxLayout
from typing import Optional
from abstract.view import View
from utils.request import Request
from view.component import SidebarComponent


class HomeAdminView(View):
    def create_layout(self):
        sidebar = SidebarComponent()

        sidebar.set_button("Gestione operatori").clicked.connect(self.go_to_gestione_operatori)
        sidebar.set_button("Inserisci libro").clicked.connect(self.go_to_inserisci_libro)
        sidebar.set_button("Gestione libri").clicked.connect(self.go_to_ricerca_libro)
        sidebar.set_button("Gestione utenti").clicked.connect(self.go_to_gestione_utenti)
        sidebar.set_button("Statistiche").clicked.connect(self.go_to_visualizza_statistiche)
        sidebar.set_button("Logout").clicked.connect(self.logout)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)

    def attach_controllers(self) -> None:
        from app import controller_logout, controller_crud_operatore, controller_gestione_libri, controller_gestione_utenti
        self.attach(controller_logout)
        self.attach(controller_crud_operatore)
        self.attach(controller_gestione_libri)
        self.attach(controller_gestione_utenti)
        from app import controller_statistiche
        self.attach(controller_statistiche)

    def __init__(self):
        super().__init__()

    def go_to_gestione_operatori(self, text: Optional[str] = None) -> None:
        self.notify(message="go_to_gestione_operatori")

    def go_to_inserisci_libro(self):
        self.notify(message="go_to_inserisci_libro")

    def go_to_ricerca_libro(self):
        self.notify(message="go_to_ricerca_libro")

    def go_to_gestione_utenti(self):
        self.notify(message="go_to_gestione_utenti")

    def go_to_visualizza_statistiche(self):
        self.notify(message=Request.GO_TO_STATISTICHE)

