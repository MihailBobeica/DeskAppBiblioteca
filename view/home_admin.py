from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from view.component import SidebarComponent
from view.ricerca_operatore import RicercaView


class HomeAdminView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Crea operatore",
                                    "Elimina operatore",
                                    "Modifica operatore",
                                    "Visualizza operatore",
                                    "Inserisci libro",
                                    "Gestione libri",
                                    "Logout",),
                            style="button")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)

    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)
        inserisci_button = self.get_button("Crea operatore")
        inserisci_button.clicked.connect(self.crea_operatore)
        elimina_button = self.get_button("Elimina operatore")
        elimina_button.clicked.connect(self.elimina_operatore)
        modifica_button = self.get_button("Modifica operatore")
        modifica_button.clicked.connect(self.modifica_operatore)
        visualizza_button = self.get_button("Visualizza operatore")
        visualizza_button.clicked.connect(self.visualizza_operatore)
        inserisci_libro_button = self.get_button("Inserisci libro")
        inserisci_libro_button.clicked.connect(self.inserisci_libro)
        ricerca_libro_button = self.get_button("Gestione libri")
        ricerca_libro_button.clicked.connect(self.ricerca_libro)

    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)

    def __init__(self):
        super().__init__()

    def crea_operatore(self):
        from view.crea_operatore import ProvaView
        self.redirect(ProvaView())

    def elimina_operatore(self):
        self.redirect(RicercaView(metodo="elimina"))

    def modifica_operatore(self):
        self.redirect(RicercaView(metodo="modifica"))

    def visualizza_operatore(self):
        self.redirect(RicercaView(metodo="visualizza"))

    def inserisci_libro(self):
        from view.inserisci_libro import InserisciView
        self.redirect(InserisciView())

    def ricerca_libro(self):
        from view.gestione_libri_admin.catalogo_admin import CatalogoComponent
        self.redirect(CatalogoComponent())
