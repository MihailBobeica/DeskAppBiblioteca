from PySide6.QtWidgets import QHBoxLayout
from typing import Optional
from abstract.view import View
from view.component import SidebarComponent


class HomeAdminView(View):
    def create_layout(self):
        sidebar = SidebarComponent()

        sidebar.set_button("Gestione operatori").clicked.connect(self.gestione_operatori)
        sidebar.set_button("Inserisci libro").clicked.connect(self.inserisci_libro)
        sidebar.set_button("Gestione libri").clicked.connect(self.ricerca_libro)
        sidebar.set_button("Gestione utenti").clicked.connect(self.gestione_utenti)
        sidebar.set_button("Logout").clicked.connect(self.logout)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)

    def attach_controllers(self) -> None:
        from app import controller_logout, controller_gestione_operatori
        self.attach(controller_logout)
        self.attach(controller_gestione_operatori)

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
