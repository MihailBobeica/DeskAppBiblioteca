from PySide6.QtWidgets import QLabel

from database import BoundedDbModel
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from utils.backend import DATE_FORMAT, YEAR_FORMAT
from utils.key import KeyDb
from utils.ui import label_autori


class LabelTitolo(QLabel):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        libro: DbLibro = data[KeyDb.LIBRO]
        super().__init__(f"Titolo: {libro.titolo}")
        self.setWordWrap(True)


class LabelAutori(QLabel):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        libro: DbLibro = data[KeyDb.LIBRO]
        super().__init__(label_autori(libro.autori))
        self.setWordWrap(True)


class LabelDisponibili(QLabel):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        libro: DbLibro = data[KeyDb.LIBRO]
        super().__init__(f"Copie disponibili: {libro.disponibili}")


class LabelScadenzaPrenotazioneLibro(QLabel):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        prenotazione_libro: DbPrenotazioneLibro = data[KeyDb.PRENOTAZIONE_LIBRO]
        super().__init__(f"Scadenza prenotazione:\n{prenotazione_libro.data_scadenza.strftime(DATE_FORMAT)}")


class LabelAnnoEdizione(QLabel):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        libro: DbLibro = data[KeyDb.LIBRO]
        super().__init__(f"Anno edizione: {libro.anno_edizione.strftime(YEAR_FORMAT)}")


class LabelAnnoPubblicazione(QLabel):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        libro: DbLibro = data[KeyDb.LIBRO]
        super().__init__(f"Anno pubblicazione: {libro.anno_pubblicazione.strftime(YEAR_FORMAT)}")


class LabelEditore(QLabel):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        libro: DbLibro = data[KeyDb.LIBRO]
        super().__init__(f"Editore: {libro.editore}")
