from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from utils.key import KeyContext
from utils.request import Request
from view.component import CatalogoComponent
from view.component import SidebarComponent


class HomeUtenteView(View):
    def create_layout(self):
        self.sidebar.set_button("Libri in prestito").clicked.connect(self.go_to_libri_in_prestito)
        self.sidebar.set_button("Libri prenotati").clicked.connect(self.go_to_libri_prenotati)
        self.sidebar.set_button("Lista di osservazione").clicked.connect(self.go_to_lista_di_osservazione)
        self.sidebar.set_button("Prenota posto").clicked.connect(self.go_to_prenota_posto)
        self.sidebar.set_button("Posti prenotati").clicked.connect(self.go_to_posti_prenotati)
        self.sidebar.set_button("Cronologia").clicked.connect(self.go_to_cronologia)
        self.sidebar.set_button("Sanzioni").clicked.connect(self.go_to_sanzioni)
        self.sidebar.set_button("Logout").clicked.connect(self.logout)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(self.sidebar)
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
        #self.notify(Request.GO_TO_CRONOLOGIA)
        self.notify("visualizza_mia_cronologia")

    def go_to_sanzioni(self):
        self.notify(Request.GO_TO_SANZIONI)

    def attach_controllers(self) -> None:
        from app import controller_logout
        from app import controller_catalogo
        from app import controller_router
        from app import controller_notifica
        from app import controller_gestione_utenti
        self.attach(controller_logout)
        self.attach(controller_catalogo)
        self.attach(controller_router)
        self.attach(controller_notifica)
        self.attach(controller_gestione_utenti)

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
        self.sidebar = SidebarComponent()
        self.catalogo = CatalogoComponent(context=KeyContext.CATALOGO_LIBRI_UTENTE)
        super().__init__()

        self.notify(Request.CHECK_LIBRI_OSSERVATI)
        self.notify(Request.CHECK_SCADENZA_PRENOTAZIONI)

    def refresh(self):
        self.catalogo.refresh()
