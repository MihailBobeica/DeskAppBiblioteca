from datetime import datetime

from PySide6.QtWidgets import QLabel

from utils.backend import DATE_FORMAT, YEAR_FORMAT
from utils.ui import label_autori


class LabelTitle(QLabel):
    def __init__(self, title: str):
        super().__init__(f"Titolo: {title}")
        self.setWordWrap(True)


class LabelAutor(QLabel):
    def __init__(self, autori: str):
        super().__init__(label_autori(autori))
        self.setWordWrap(True)


class LabelDisponibili(QLabel):
    def __init__(self, disponibili: int):
        super().__init__(f"Copie disponibili: {disponibili}")


class LabelScadenzaPrenotazioneLibro(QLabel):
    def __init__(self, scadenza_prenotazione: datetime):
        super().__init__(f"Scadenza prenotazione:\n{scadenza_prenotazione.strftime(DATE_FORMAT)}")


class LabelAnnoEdizione(QLabel):
    def __init__(self, anno_edizione: datetime):
        super().__init__(f"Anno edizione: {anno_edizione.strftime(YEAR_FORMAT)}")
