from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from utils.key import KeyContext
from view.component import CatalogoComponent
from view.component import SidebarComponent


class HomeUtenteView(View):
    def create_layout(self):
        self.sidebar.set_button("Libri in prestito").clicked.connect(self.go_to_libri_in_prestito)
        self.sidebar.set_button("Libri prenotati").clicked.connect(self.go_to_libri_prenotati)
        self.sidebar.set_button("Lista di osservazione").clicked.connect(self.go_to_lista_di_osservazione)
        self.sidebar.set_button("Prenota posto singolo").clicked.connect(self.go_to_prenota_posto_singolo)
        self.sidebar.set_button("Prenota aula").clicked.connect(self.go_to_prenota_aula)
        self.sidebar.set_button("Posti prenotati").clicked.connect(self.go_to_posti_prenotati)
        self.sidebar.set_button("Cronologia").clicked.connect(self.go_to_cronologia)
        self.sidebar.set_button("Sanzioni").clicked.connect(self.go_to_sanzioni)
        self.sidebar.set_button("Logout").clicked.connect(self.logout)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(self.sidebar)
        layout.addWidget(self.catalogo)

    def go_to_libri_in_prestito(self):
        self.notify("go_to_libri_in_prestito")

    def go_to_libri_prenotati(self):
        self.notify("go_to_libri_prenotati")

    def go_to_lista_di_osservazione(self):
        self.notify("go_to_lista_di_osservazione")

    def go_to_prenota_posto_singolo(self):
        self.notify("go_to_prenota_posto_singolo")

    def go_to_prenota_aula(self):
        self.notify("go_to_prenota_aula")

    def go_to_posti_prenotati(self):
        self.notify("go_to_posti_prenotati")

    def go_to_cronologia(self):
        self.notify("go_to_cronologia",
                    data={"id_utente": None})

    def go_to_sanzioni(self):
        self.notify("go_to_sanzioni",
                    data={"id_utente": None})

    def logout(self):
        self.notify("logout")

    def attach_controllers(self) -> None:
        from app import controller_router, controller_logout, controller_notifica
        self.attach(controller_router)
        self.attach(controller_logout)
        self.attach(controller_notifica)

    def __init__(self):
        self.sidebar = SidebarComponent()
        self.catalogo = CatalogoComponent(context=KeyContext.CATALOGO_LIBRI_UTENTE)
        super().__init__()

        self.notify("check_libri_osservati")
        self.notify("check_scadenza_prenotazioni")

    def refresh(self):
        self.catalogo.refresh()
