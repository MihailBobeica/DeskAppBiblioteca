from datetime import datetime

from PySide6.QtWidgets import QLabel

from utils.backend import DATE_FORMAT, YEAR_FORMAT
from utils.ui import label_autori


class LabelTitolo(QLabel):
    def __init__(self, titolo: str):
        super().__init__(f"Titolo: {titolo}")
        self.setWordWrap(True)


class LabelAutori(QLabel):
    def __init__(self, autori: str):
        super().__init__(label_autori(autori))
        self.setWordWrap(True)


class LabelDisponibili(QLabel):
    def __init__(self, disponibili: int):
        super().__init__(f"Copie disponibili: {disponibili}")


class LabelScadenzaPrenotazioneLibro(QLabel):
    def __init__(self, data_scadenza: datetime):
        super().__init__(f"Scadenza prenotazione:\n{data_scadenza.strftime(DATE_FORMAT)}")


class LabelAnnoEdizione(QLabel):
    def __init__(self, anno_edizione: datetime):
        super().__init__(f"Anno edizione: {anno_edizione.strftime(YEAR_FORMAT)}")


class LabelAnnoPubblicazione(QLabel):
    def __init__(self, anno_pubblicazione: datetime):
        super().__init__(f"Anno pubblicazione: {anno_pubblicazione.strftime(YEAR_FORMAT)}")


class LabelEditore(QLabel):
    def __init__(self, editore: str):
        super().__init__(f"Editore: {editore}")


class LabelDati(QLabel):
    def __init__(self, dati: str):
        super().__init__(f"Dati: {dati}")


class LabelIsbn(QLabel):
    def __init__(self, isbn):
        super().__init__(f"ISBN: {isbn}")


class LabelDataPrenotazioneLibro(QLabel):
    def __init__(self, data_prenotazione_libro: datetime):
        super().__init__(f"Data prenotazione:\n{data_prenotazione_libro.strftime(DATE_FORMAT)}")


class LabelCodicePrenotazioneLibro(QLabel):
    def __init__(self, codice_prenotazione_libro: str):
        super().__init__(f"Codice prenotazione:\n{codice_prenotazione_libro}")


class LabelInizioPrestito(QLabel):
    def __init__(self, inizio_prestito: datetime):
        super().__init__(f"Inizio prestito:\n{inizio_prestito.strftime(DATE_FORMAT)}")


class LabelScadenzaPrestito(QLabel):
    def __init__(self, scadenza_prestito: datetime):
        super().__init__(f"Fine prestito:\n{scadenza_prestito.strftime(DATE_FORMAT)}")
