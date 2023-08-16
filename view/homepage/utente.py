from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from model.prestito import Prestito
from controller.gestione_prenotazione_posto import PrenotazioneController
from strategy import CercaLibriCatalogo
from utils.auth import Auth
from abstract.view import View
from controller.gestione_prenotazione_posto import PrenotazioneController
from utils.context import CONTEXT_CATALOGO_LIBRI_UTENTE
from view.component import SidebarComponent
from view.component.catalogo import CatalogoComponent
from view.libri_prenotati import LibriPrenotatiView
from view.lisat_prenotazioni import ListaPrenotazioniView
from view.scegli_prenotazione import ScegliPrenotazione


class HomeUtenteView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Catalogo",
                                    "Libri in prestito",
                                    "Libri prenotati",
                                    "Lista di osservazione",
                                    "Prenota posto",
                                    "Lista di prenotazioni",
                                    "Visualizza cronologia",
                                    "Sanzioni",
                                    "Info",
                                    "Logout"),
                            style="button")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(self.catalogo)

    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)
        self.get_button("Prenota posto").clicked.connect(self.show_prenota_schermata)
        self.get_button("Lista di prenotazioni").clicked.connect(self.show_lista_prenotazioni)
        self.get_button("Libri prenotati").clicked.connect(self.libri_prenotati)
        self.get_button("Libri in prestito").clicked.connect(self.libri_in_prestito)
        self.get_button("Visualizza cronologia").clicked.connect(self.visualizza_cronologia)

    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)
        self.prenotazione_controller = PrenotazioneController() # CAUSA UN BUG PER CUI LAPP NON SI CHIUDE

    def show_prenota_schermata(self):
        scegli_prenotazione_view = ScegliPrenotazione()
        self.main_window.set_view(scegli_prenotazione_view)

    def show_lista_prenotazioni(self):
        lista_prenotazioni_view = ListaPrenotazioniView(self.prenotazione_controller, self.main_window)
        self.main_window.set_view(lista_prenotazioni_view)

    def libri_prenotati(self):
        self.redirect(LibriPrenotatiView())
        # from model.prenotazione_libro import PrenotazioneLibro
        # prenotazioni = PrenotazioneLibro.ricerca(self)
        # from .libri_prenotati import VisualizzaPrenotazioni
        # self.redirect(VisualizzaPrenotazioni(prenotazioni))

    def libri_in_prestito(self):
        libri = Prestito.by_utente(self, Auth.user.username)
        from .libri_in_prestito import VisualizzaPrestiti
        self.redirect(VisualizzaPrestiti(libri))

    def visualizza_cronologia(self):
        libri = Prestito.by_utente(self, Auth.user.username)
        from view.Gestione_utente.visualizza_cronologia import VisualizzaCronologia
        self.redirect(VisualizzaCronologia(libri))

    def __init__(self):
        self.catalogo = CatalogoComponent(context=CONTEXT_CATALOGO_LIBRI_UTENTE)
        super().__init__()

    def update(self):
        self.catalogo.update()
