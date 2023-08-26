from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from controller.gestione_prenotazione_posto import PrenotazioneController
from view.component import SidebarComponent
from view.conferma_prenotazioni import ListaTuttePrenotazioniView


class HomeOperatoreView(View):
    def create_layout(self):
        sidebar = SidebarComponent()

        sidebar.set_button("Registra prestito").clicked.connect(self.ricerca_prestito)
        sidebar.set_button("Registra restituzione").clicked.connect(self.ricerca_utente)
        sidebar.set_button("Conferma Prenotazioni").clicked.connect(self.show_conferma_prenotazioni)
        sidebar.set_button("Logout").clicked.connect(self.logout)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)

    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)
        self.prenotazione_controller = PrenotazioneController()  # CAUSA UN BUG PER CUI LAPP NON SI CHIUDE

    def __init__(self):
        super().__init__()

    def ricerca_prestito(self):
        from view.registra_prestito import RegistraPrestito
        self.redirect(RegistraPrestito())

    def ricerca_utente(self):
        from view.restituzione.ricerca_utente_restituzione import Prova
        self.redirect(Prova())

    def show_conferma_prenotazioni(self):
        lista_prenotazioni_view = ListaTuttePrenotazioniView(self.prenotazione_controller, self.main_window)
        self.main_window.set_view(lista_prenotazioni_view)
