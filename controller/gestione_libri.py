from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from model import ModelLibri, ModelPrenotazioniLibri
from utils.auth import Auth
from utils.strings import *
from view.gestione_libri_admin.catalogo_admin import CatalogoAdminView
from model.libri import ModelLibri
from database import Libro as db_Libro

class GestioneLibriController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        self.models = models
        super().__init__()

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "inserisci_libro":
            self.inserisci_libro( data)
        elif message == "modifica_libro":
            self.modifica_libro(data)
        elif message == "elimina_libro":
            pass
            # self.elimina_libro(data)
        elif message == "go_to_inserisci_libro":
            pass
        elif message == "go_to_ricerca_libro":
            self.redirect(CatalogoAdminView())

    def inserisci_libro(self, data: Optional[dict] = None):
        # ModelLibri.aggiungi(self, data)
        from view.homepage.admin import HomeAdminView
        self.redirect(HomeAdminView())

    def modifica_libro(self, data: dict):
        ModelLibri.modifica(self, data, data["isbn"])
        from view.homepage.admin import HomeAdminView
        self.redirect(HomeAdminView())
        '''ModelLibro().modifica(dati, self.info.isbn)
        self.main_window.set_view(HomeAdminView())'''

    def elimina_libro(self, libro):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText("Conferma")
        msg_box.setWindowTitle("Sei sicuro di voler rimuovere il libro?")
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Ok)
        response = msg_box.exec()
        if response == QMessageBox.Ok:
            ModelLibri.elimina(self, libro)

        from view.homepage.admin import HomeAdminView
        self.redirect(HomeAdminView())