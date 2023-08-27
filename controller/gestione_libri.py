from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from model import Libro, PrenotazioneLibro
from utils.auth import Auth
from utils.strings import *
from view.component.catalogo import CatalogoComponent
from view.libri_prenotati import LibriPrenotatiView
from model.libro import Libro
from database import Libro as db_Libro

class GestioneLibriController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        self.inserisci_libro(message, data)

    def inserisci_libro(self, message: str, data: Optional[dict] = None):
        if message == "inserisci_libro":
            Libro.inserisci2(self,data)
