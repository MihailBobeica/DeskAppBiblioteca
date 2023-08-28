from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from utils.key import KeyContext
from utils.request import Request
from view.component import CatalogoComponent
from view.component import SidebarComponent


class HomeUtenteView(View):
    def create_layout(self):
        sidebar = SidebarComponent()

        sidebar.set_button("Libri in prestito").clicked.connect(self.go_to_libri_in_prestito)
        sidebar.set_button("Libri prenotati").clicked.connect(self.go_to_libri_prenotati)
        sidebar.set_button("Lista di osservazione").clicked.connect(self.go_to_lista_di_osservazione)
        sidebar.set_button("Prenota posto").clicked.connect(self.go_to_prenota_posto)
        sidebar.set_button("Posti prenotati").clicked.connect(self.go_to_posti_prenotati)
        sidebar.set_button("Cronologia").clicked.connect(self.go_to_cronologia)
        sidebar.set_button("Sanzioni").clicked.connect(self.go_to_sanzioni)
        sidebar.set_button("Logout").clicked.connect(self.logout)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(self.catalogo)

    def go_to_libri_in_prestito(self):
        self.notify(Request.GO_TO_LIBRI_IN_PRESTITO)

    def go_to_libri_prenotati(self):
        self.notify(Request.GO_TO_LIBRI_PRENOTATI)

    def go_to_lista_di_osservazione(self):
        self.notify(Request.GO_TO_LISTA_DI_OSSERVAZIONE)

    def go_to_prenota_posto(self):
        self.notify(Request.GO_TO_PRENOTA_POSTO)

    def go_to_posti_prenotati(self):
        self.notify(Request.GO_TO_POSTI_PRENOTATI)

    def go_to_cronologia(self):
        self.notify(Request.GO_TO_CRONOLOGIA)

    def go_to_sanzioni(self):
        self.notify(Request.GO_TO_SANZIONI)

    def attach_controllers(self) -> None:
        from app import controller_logout
        from app import controller_catalogo
        from app import controller_router
        self.attach(controller_logout)
        self.attach(controller_catalogo)
        self.attach(controller_router)
        # self.prenotazione_controller = PrenotazioneController()  # CAUSA UN BUG PER CUI LAPP NON SI CHIUDE

    # def show_prenota_schermata(self):
    #     scegli_prenotazione_view = ScegliPrenotazione()
    #     self.main_window.set_view(scegli_prenotazione_view)
    #
    # def show_lista_prenotazioni(self):
    #     lista_prenotazioni_view = ListaPrenotazioniView(self.prenotazione_controller, self.main_window)
    #     self.main_window.set_view(lista_prenotazioni_view)
    #
    # def libri_prenotati(self):
    #     self.redirect(LibriPrenotatiView())
    #     # from model.prenotazione_libro import PrenotazioneLibro
    #     # prenotazioni = PrenotazioneLibro.ricerca(self)
    #     # from .libri_prenotati import VisualizzaPrenotazioni
    #     # self.redirect(VisualizzaPrenotazioni(prenotazioni))
    #
    # def libri_in_prestito(self):
    #     libri = Prestito.by_utente(self, Auth.user.username)
    #     from .libri_in_prestito import VisualizzaPrestiti
    #     self.redirect(VisualizzaPrestiti(libri))
    #
    # def visualizza_cronologia(self):
    #     libri = Prestito.by_utente(self, Auth.user.username)
    #     from view.Gestione_utente.visualizza_cronologia import VisualizzaCronologia
    #     self.redirect(VisualizzaCronologia(libri))

    def __init__(self):
        self.catalogo = CatalogoComponent(context=KeyContext.CATALOGO_LIBRI_UTENTE)
        super().__init__()

    def update(self):
        self.catalogo.update()
