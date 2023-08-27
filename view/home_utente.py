from PySide6.QtWidgets import QHBoxLayout

from controller.gestione_prenotazione_posto import PrenotazioneController
from strategy import CercaLibriCatalogo
from utils.auth import Auth
from abstract.view import View
from controller.gestione_prenotazione_posto import PrenotazioneController
from utils.backend import CONTEXT_CATALOGO
from view.component import SidebarComponent
from view.component.catalogo import CatalogoComponent
from view.libri_prenotati import LibriPrenotatiView
from view.lisat_prenotazioni import ListaPrenotazioniView
from view.scegli_prenotazione import ScegliPrenotazione
from model.prestito import Prestito


class HomeUtenteView(View):
    def create_layout(self):
        sidebar = SidebarComponent()

        sidebar.set_button("Libri in prestito").clicked.connect()
        sidebar.set_button("Libri prenotati").clicked.connect()
        sidebar.set_button("Lista di osservazione").clicked.connect()
        sidebar.set_button("Prenota posto").clicked.connect()
        sidebar.set_button("Posti prenotati").clicked.connect()
        sidebar.set_button("Cronologia").clicked.connect()
        # sidebar.set_button("Info").clicked.connect()
        sidebar.set_button("Logout").clicked.connect(self.logout)

        catalogo = CatalogoComponent(CercaLibriCatalogo(), context=CONTEXT_CATALOGO)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(catalogo)

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

        libri = Prestito.by_utente(self,Auth.user.username)
        from .libri_in_prestito import VisualizzaPrestiti
        self.redirect(VisualizzaPrestiti(libri))

    def visualizza_cronologia(self):
        libri = Prestito.by_utente(self,Auth.user.id)
        print(libri)
        from view.Gestione_utente.visualizza_cronologia import VisualizzaCronologia
        self.redirect(VisualizzaCronologia(libri))



    def __init__(self):
        super().__init__()

