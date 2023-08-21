from typing import Type, TypedDict

from abstract import BoundedView, Factory
from utils import KeyButtonComponent
from view.component.button import ButtonCancellaPrenotazioneLibro
from view.component.button import ButtonDettagliPrenotazioneLibro
from view.component.button import ButtonGoToLibriPrenotati
from view.component.button import ButtonOsservaLibro
from view.component.button import ButtonPrenotaLibro
from view.component.button import ButtonVisualizzaLibro
from view.component.button import RequestButton


class KwargsDict(TypedDict):
    view: BoundedView


class ButtonComponentFactory(Factory):
    def __init__(self):
        super().__init__()

        self.type: dict[KeyButtonComponent, Type[RequestButton]] = dict()

        self.type[KeyButtonComponent.VISUALIZZA_LIBRO] = ButtonVisualizzaLibro
        self.type[KeyButtonComponent.PRENOTA_LIBRO] = ButtonPrenotaLibro
        self.type[KeyButtonComponent.OSSERVA_LIBRO] = ButtonOsservaLibro
        self.type[KeyButtonComponent.DETTAGLI_PRENOTAZIONE_LIBRO] = ButtonDettagliPrenotazioneLibro
        self.type[KeyButtonComponent.CANCELLA_PRENOTAZIONE_LIBRO] = ButtonCancellaPrenotazioneLibro
        self.type[KeyButtonComponent.GO_TO_LIBRI_PRENOTATI] = ButtonGoToLibriPrenotati

    def create(self, key: KeyButtonComponent, **kwargs) -> RequestButton:
        kwargs: KwargsDict
        view = kwargs.get("view")
        button_component = self.type.get(key)
        if button_component:
            return button_component(view=view)
        raise ValueError("Invalid button component type")


button_component_factory = ButtonComponentFactory()
