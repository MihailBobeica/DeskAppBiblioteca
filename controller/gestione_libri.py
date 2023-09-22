from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from model import Libro, PrenotazioneLibro
from utils.auth import Auth
from utils.strings import *
from view.gestione_libri_admin.catalogo_admin import CatalogoComponent
from view.inserisci_libro import InserisciView
from view.libri_prenotati import LibriPrenotatiView
from model.libro import Libro
from database import Libro as db_Libro

class GestioneLibriController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "inserisci_libro":
            self.inserisci_libro( data)
        elif message == "modifica_libro":
            self.modifica_libro(data)
        elif message == "elimina_libro":
            self.elimina_libro(data)
        elif message == "go_to_inserisci_libro":
            self.redirect(InserisciView())
        elif message == "go_to_ricerca_libro":
            self.redirect(CatalogoComponent())

    def inserisci_libro(self, data: Optional[dict] = None):
        Libro.inserisci2(self,data)

    def modifica_libro(self, data: dict):
        Libro.modifica(self,data, data["isbn"])
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
            Libro.elimina(self,libro)

        from view.homepage.admin import HomeAdminView
        self.redirect(HomeAdminView())