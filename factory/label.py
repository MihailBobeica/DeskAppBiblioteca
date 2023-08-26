from typing import Type, TypedDict

from PySide6.QtWidgets import QLabel

from abstract import Factory
from database import BoundedDbModel
from utils import KeyLabelComponent
from view.component.label import LabelAnnoEdizione
from view.component.label import LabelAnnoPubblicazione
from view.component.label import LabelAutori
from view.component.label import LabelDisponibili
from view.component.label import LabelEditore
from view.component.label import LabelScadenzaPrenotazioneLibro
from view.component.label import LabelTitolo


class KwargsDict(TypedDict):
    data: dict[str, BoundedDbModel]


class LabelComponentFactory(Factory):
    def __init__(self):
        super().__init__()

        self.type: dict[KeyLabelComponent, Type[QLabel]] = dict()

        self.type[KeyLabelComponent.TITOLO] = LabelTitolo
        self.type[KeyLabelComponent.AUTORI] = LabelAutori
        self.type[KeyLabelComponent.DISPONIBILI] = LabelDisponibili
        self.type[KeyLabelComponent.ANNO_EDIZIONE] = LabelAnnoEdizione
        self.type[KeyLabelComponent.ANNO_PUBBLICAZIONE] = LabelAnnoPubblicazione
        self.type[KeyLabelComponent.EDITORE] = LabelEditore
        self.type[KeyLabelComponent.SCADENZA_PRENOTAZIONE_LIBRO] = LabelScadenzaPrenotazioneLibro

    def create(self, key: KeyLabelComponent, **kwargs) -> QLabel:
        kwargs: KwargsDict
        data = kwargs.get("data")
        label_component = self.type.get(key)
        if label_component:
            return label_component(data=data)
        raise ValueError("Invalid label component type")


label_component_factory = LabelComponentFactory()
