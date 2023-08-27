from typing import Type

from PySide6.QtWidgets import QLabel

from abstract import Factory
from database import BoundedDbModel
from utils.key import KeyDb
from utils.key import KeyLabelComponent


class LabelComponentFactory(Factory):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        self.data = data

        super().__init__()

        from view.component.label import LabelAnnoEdizione
        from view.component.label import LabelAnnoPubblicazione
        from view.component.label import LabelAutori
        from view.component.label import LabelDisponibili
        from view.component.label import LabelEditore
        from view.component.label import LabelScadenzaPrenotazioneLibro
        from view.component.label import LabelTitolo
        from view.component.label import LabelDati
        from view.component.label import LabelIsbn
        from view.component.label import LabelDataPrenotazioneLibro
        from view.component.label import LabelCodicePrenotazioneLibro

        self.type: dict[KeyLabelComponent, Type[QLabel]] = dict()

        self.type[KeyLabelComponent.TITOLO] = LabelTitolo
        self.type[KeyLabelComponent.AUTORI] = LabelAutori
        self.type[KeyLabelComponent.DISPONIBILI] = LabelDisponibili
        self.type[KeyLabelComponent.ANNO_EDIZIONE] = LabelAnnoEdizione
        self.type[KeyLabelComponent.ANNO_PUBBLICAZIONE] = LabelAnnoPubblicazione
        self.type[KeyLabelComponent.EDITORE] = LabelEditore
        self.type[KeyLabelComponent.SCADENZA_PRENOTAZIONE_LIBRO] = LabelScadenzaPrenotazioneLibro
        self.type[KeyLabelComponent.DATI] = LabelDati
        self.type[KeyLabelComponent.ISBN] = LabelIsbn
        self.type[KeyLabelComponent.DATA_PRENOTAZIONE_LIBRO] = LabelDataPrenotazioneLibro
        self.type[KeyLabelComponent.CODICE_PRENOTAZIONE_LIBRO] = LabelCodicePrenotazioneLibro

    def create(self, key: KeyLabelComponent) -> QLabel:
        label_component = self.type.get(key)
        if label_component:
            return label_component(data=self.data)
        raise ValueError("Invalid label component type")
