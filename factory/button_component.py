from typing import Type

from abstract import BoundedView, Factory
from utils.key import KeyButtonComponent


class ButtonComponentFactory(Factory):
    def __init__(self, view: BoundedView):
        self.view = view

        super().__init__()

        from view.component.button import ButtonCancellaPrenotazioneLibro
        from view.component.button import ButtonDettagliPrenotazioneLibro
        from view.component.button import ButtonGoToLibriPrenotati
        from view.component.button import ButtonOsservaLibro
        from view.component.button import ButtonPrenotaLibro
        from view.component.button import ButtonVisualizzaLibro
        from view.component.button import RequestButton

        self.type: dict[KeyButtonComponent, Type[RequestButton]] = dict()

        self.type[KeyButtonComponent.VISUALIZZA_LIBRO] = ButtonVisualizzaLibro
        self.type[KeyButtonComponent.PRENOTA_LIBRO] = ButtonPrenotaLibro
        self.type[KeyButtonComponent.OSSERVA_LIBRO] = ButtonOsservaLibro
        self.type[KeyButtonComponent.DETTAGLI_PRENOTAZIONE_LIBRO] = ButtonDettagliPrenotazioneLibro
        self.type[KeyButtonComponent.CANCELLA_PRENOTAZIONE_LIBRO] = ButtonCancellaPrenotazioneLibro
        self.type[KeyButtonComponent.GO_TO_LIBRI_PRENOTATI] = ButtonGoToLibriPrenotati

    def create(self, key: KeyButtonComponent):
        button_component = self.type.get(key)
        if button_component:
            return button_component(view=self.view)
        raise ValueError("Invalid button component type")
