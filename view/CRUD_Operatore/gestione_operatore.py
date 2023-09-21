
from PySide6.QtWidgets import QHBoxLayout
from .ricerca_operatore import RicercaView
from abstract.view import View
from view.component import SidebarComponent

class GestioneOperatori(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        '''sidebar.add_buttons_rm(labels=("Crea operatore",
                                    "Elimina operatore",
                                    "Modifica operatore",
                                    "Visualizza operatore",
                                    "Logout",),
                               style="button")'''

        sidebar.set_button("Crea operatore").clicked.connect(self.crea_operatore)
        sidebar.set_button("Elimina operatore").clicked.connect(self.elimina_operatore)
        sidebar.set_button("Modifica operatore").clicked.connect(self.modifica_operatore)
        sidebar.set_button("Visualizza operatore").clicked.connect(self.visualizza_operatore)
        sidebar.set_button("Logout").clicked.connect(self.logout)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)

    '''def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)
        inserisci_button = self.get_button("Crea operatore")
        inserisci_button.clicked.connect(self.crea_operatore)
        elimina_button = self.get_button("Elimina operatore")
        elimina_button.clicked.connect(self.elimina_operatore)
        modifica_button = self.get_button("Modifica operatore")
        modifica_button.clicked.connect(self.modifica_operatore)
        visualizza_button = self.get_button("Visualizza operatore")
        visualizza_button.clicked.connect(self.visualizza_operatore)'''


    def attach_controllers(self) -> None:
        from app import controller_logout,controller_crud_operatore
        self.attach(controller_logout)
        self.attach(controller_crud_operatore)

    def __init__(self):
        super().__init__()

    def crea_operatore(self):
        self.notify(message="crea_operatore")


    def elimina_operatore(self):
        #self.redirect(RicercaView(metodo="elimina"))
        self.notify(message="elimina_operatore", data={"metodo" : "elimina"})

    def modifica_operatore(self):
        self.notify(message="modifica_operatore", data={"metodo" : "modifica"})

    def visualizza_operatore(self):
        self.notify(message="visualizza_operatore", data={"metodo" : "visualizza"})


