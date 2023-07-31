from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from view.component import SidebarComponent
from view.component.catalogo import CatalogoComponent
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
                                    "Sanzioni",
                                    "Info",
                                    "Logout"),
                            style="button")
        catalogo = CatalogoComponent()

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(catalogo)

    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)
        self.get_button("Prenota posto").clicked.connect(self.show_prenota_schermata)
        self.get_button("Lista di prenotazioni").clicked.connect(self.show_lista_prenotazioni)


    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)

    def show_prenota_schermata(self):
        scegli_prenotazione_view = ScegliPrenotazione()
        self.main_window.set_view(scegli_prenotazione_view)

    def show_lista_prenotazioni(self):
            lista_prenotazioni_view = ListaPrenotazioniView()
            self.main_window.set_view(lista_prenotazioni_view)




    def __init__(self):
        super().__init__()
