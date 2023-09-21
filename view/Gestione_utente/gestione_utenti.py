from PySide6.QtWidgets import QHBoxLayout
from abstract.view import View
from view.component import SidebarComponent


class GestioneUtentiView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        '''sidebar.add_buttons_rm(labels=("Visualizza utente",
                                    "Visualizza cronologia",
                                    "Logout",),
                               style="button")'''

        sidebar.set_button("Visualizza utente").clicked.connect(self.visualizza_utente)
        sidebar.set_button("Visualizza cronologia").clicked.connect(self.visualizza_cronologia)
        sidebar.set_button("Logout").clicked.connect(self.logout)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)




    '''def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)
        visualizza_utente_button = self.get_button("Visualizza utente")
        visualizza_utente_button.clicked.connect(self.visualizza_utente)
        visualizza_cronologia_button = self.get_button("Visualizza cronologia")
        visualizza_cronologia_button.clicked.connect(self.visualizza_cronologia)'''



    def attach_controllers(self) -> None:
        from app import controller_logout, controller_gestione_utenti
        self.attach(controller_logout)
        self.attach(controller_gestione_utenti)

    def __init__(self):
        super().__init__()

    def visualizza_utente(self):
        self.notify(message = "visualizza_utente")

    def visualizza_cronologia(self):
        self.notify(message="ricerca_utente")