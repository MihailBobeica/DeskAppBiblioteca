from abc import abstractmethod

from PySide6.QtWidgets import QPushButton

from abstract import BoundedView
from utils.request import *


class RequestButton(QPushButton):
    def __init__(self, label: str, view: BoundedView):
        super().__init__(label)
        self.view = view
        self.clicked.connect(self.send_request)

    @abstractmethod
    def send_request(self) -> None:
        ...


class ButtonVisualizzaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(label="Visualizza",
                         view=view)

    def send_request(self) -> None:
        self.view: LibroComponent
        self.view.notify(message="visualizza_libro",
                         data={"libro": self.view.libro,
                               "context": self.view.context})


class ButtonPrenotaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(label="Prenota libro",
                         view=view)

    def send_request(self) -> None:
        self.view: LibroComponent
        self.view.notify(message="prenota_libro",
                         data={"libro": self.view.libro})


class ButtonOsservaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(label="Osserva libro",
                         view=view)

    def send_request(self) -> None:
        self.view: LibroComponent
        self.view.notify(message="osserva_libro",
                         data={"libro": self.view.libro})


class ButtonDettagliPrenotazioneLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(label="Dettagli prenotazione",
                         view=view)

    def send_request(self) -> None:
        self.view: LibroComponentPrenotazione  # TODO: make a generic class
        self.view.notify(message="visualizza_dettagli_prenotazione",
                         data={"libro": self.view.libro,
                               "prenotazione": self.view.prenotazione})


class ButtonCancellaPrenotazioneLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(label="Cancella prenotazione",
                         view=view)

    def send_request(self) -> None:
        self.view: LibroComponentPrenotazione  # TODO: make a generic class
        self.view.notify(message="cancella_prenotazione",
                         data={"catalogo": self.view.catalogo,
                               "libro": self.view.libro,
                               "prenotazione": self.view.prenotazione,
                               "contesto": self.view.context})


class ButtonGoToLibriPrenotati(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(label="Indietro",
                         view=view)

    def send_request(self) -> None:
        self.view: LibroComponentPrenotazione
        self.view.notify(message=REQUEST_GO_TO_LIBRI_PRENOTATI)
