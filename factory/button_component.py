from typing import Callable

from PySide6.QtWidgets import QPushButton

from abstract import BoundedView, Factory


class ButtonComponentFactory(Factory):
    def __init__(self, view: BoundedView):
        self.view = view

        super().__init__()

    def create(self, button: str) -> QPushButton:
        try:
            create_button_component: Callable[[], QPushButton] = self.__getattribute__(f"create_{button}")
            return create_button_component()
        except AttributeError as e:
            print(e)

    def create_go_to_dettagli_libro_guest(self) -> QPushButton:
        from view.component.button import ButtonGoToDettagliLibroGuest
        return ButtonGoToDettagliLibroGuest(self.view)

    def create_go_to_dettagli_libro_utente(self) -> QPushButton:
        from view.component.button import ButtonGoToDettagliLibroUtente
        return ButtonGoToDettagliLibroUtente(self.view)

    def create_prenota_libro(self) -> QPushButton:
        from view.component.button import ButtonPrenotaLibro
        return ButtonPrenotaLibro(self.view)

    def create_osserva_libro(self) -> QPushButton:
        from view.component.button import ButtonOsservaLibro
        return ButtonOsservaLibro(self.view)

    def create_go_to_dettagli_prenotazione_libro(self) -> QPushButton:
        from view.component.button import ButtonGoToDettagliPrenotazioneLibro
        return ButtonGoToDettagliPrenotazioneLibro(self.view)

    def create_cancella_prenotazione_libro(self) -> QPushButton:
        from view.component.button import ButtonCancellaPrenotazioneLibro
        return ButtonCancellaPrenotazioneLibro(self.view)

    def create_go_to_libri_prenotati(self) -> QPushButton:
        from view.component.button import ButtonGoToLibriPrenotati
        return ButtonGoToLibriPrenotati(self.view)

    def create_go_to_libri_in_prestito(self) -> QPushButton:
        from view.component.button import ButtonGoToLibriInPrestito
        return ButtonGoToLibriInPrestito(self.view)

    def create_rimuovi_libro_osservato(self) -> QPushButton:
        from view.component.button import ButtonRimuoviLibroOsservato
        return ButtonRimuoviLibroOsservato(self.view)

    def create_go_to_dettagli_prestito(self) -> QPushButton:
        from view.component.button import ButtonGoToDettagliPrestito
        return ButtonGoToDettagliPrestito(self.view)
