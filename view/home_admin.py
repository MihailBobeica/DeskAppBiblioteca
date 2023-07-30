from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from view.component import SidebarComponent


class HomeAdminView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Gestione operatori",
                                    "Inserisci libro",
                                    "Gestione libri",
                                    "Gestione utenti",
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

    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)

    def __init__(self):
        super().__init__()

    def gestione_operatori(self):
        from view.gestione_operatore import GestioneOperatori
        self.redirect(GestioneOperatori())

    def inserisci_libro(self):
        from view.inserisci_libro import InserisciView
        self.redirect(InserisciView())

    def ricerca_libro(self):
        from view.gestione_libri_admin.catalogo_admin import CatalogoComponent
        self.redirect(CatalogoComponent())

    def gestione_utenti(self):
        from view.gestione_utenti import GestioneUtentiView
        self.redirect(GestioneUtentiView())
