from typing import Callable

from PySide6.QtWidgets import QLabel

from abstract import Factory
from database import BoundedDbModel, Libro, PrenotazioneLibro, Prestito


class LabelComponentFactory(Factory):
    def __init__(self, dati: dict[str, BoundedDbModel]):
        self.libro: Libro = dati.get("libro")
        self.prestito: Prestito = dati.get("prestito")
        self.prenotazione_libro: PrenotazioneLibro = dati.get("prenotazione_libro")

        super().__init__()

    def create(self, label: str) -> QLabel:
        try:
            create_label_component: Callable[[], QLabel] = self.__getattribute__(f"create_{label}")
            return create_label_component()
        except AttributeError as e:
            print(e)

    def create_titolo(self) -> QLabel:
        from view.component.label import LabelTitolo
        return LabelTitolo(self.libro.titolo)

    def create_autori(self) -> QLabel:
        from view.component.label import LabelAutori
        return LabelAutori(self.libro.autori)

    def create_disponibili(self) -> QLabel:
        from view.component.label import LabelDisponibili
        return LabelDisponibili(self.libro.disponibili)

    def create_anno_edizione(self) -> QLabel:
        from view.component.label import LabelAnnoEdizione
        return LabelAnnoEdizione(self.libro.anno_edizione)

    def create_anno_pubblicazione(self) -> QLabel:
        from view.component.label import LabelAnnoPubblicazione
        return LabelAnnoPubblicazione(self.libro.anno_pubblicazione)

    def create_editore(self) -> QLabel:
        from view.component.label import LabelEditore
        return LabelEditore(self.libro.editore)

    def create_dati(self) -> QLabel:
        from view.component.label import LabelDati
        return LabelDati(self.libro.dati)

    def create_scadenza_prenotazione_libro(self) -> QLabel:
        from view.component.label import LabelScadenzaPrenotazioneLibro
        return LabelScadenzaPrenotazioneLibro(self.prenotazione_libro.data_scadenza)

    def create_isbn(self) -> QLabel:
        from view.component.label import LabelIsbn
        return LabelIsbn(self.libro.isbn)

    def create_data_prenotazione_libro(self) -> QLabel:
        from view.component.label import LabelDataPrenotazioneLibro
        return LabelDataPrenotazioneLibro(self.prenotazione_libro.data_prenotazione)

    def create_codice_prenotazione_libro(self) -> QLabel:
        from view.component.label import LabelCodicePrenotazioneLibro
        return LabelCodicePrenotazioneLibro(self.prenotazione_libro.codice)

    def create_inizio_prestito(self) -> QLabel:
        from view.component.label import LabelInizioPrestito
        return LabelInizioPrestito(self.prestito.data_inizio)

    def create_fine_prestito(self) -> QLabel:
        from view.component.label import LabelScadenzaPrestito
        return LabelScadenzaPrestito(self.prestito.data_scadenza)
