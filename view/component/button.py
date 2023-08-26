from abc import abstractmethod

from PySide6.QtWidgets import QPushButton

from abstract import BoundedView
from utils.request import *


class RequestButton(QPushButton):
    def __init__(self, view: BoundedView):
        super().__init__()
        self.view = view
        self.clicked.connect(self.send_request)

    @abstractmethod
    def send_request(self) -> None:
        ...


class ButtonVisualizzaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Visualizza")

    def send_request(self) -> None:
        self.view: LibroComponent
        self.view.notify(message="visualizza_libro",
                         data={"libro": self.view.libro,
                               "context": self.view.context})


class ButtonPrenotaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Prenota libro")

    def send_request(self) -> None:
        self.view: LibroComponent
        self.view.notify(message="prenota_libro",
                         data={"libro": self.view.libro})


class ButtonOsservaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Osserva libro")

    def send_request(self) -> None:
        self.view: LibroComponent
        self.view.notify(message="osserva_libro",
                         data={"libro": self.view.libro})


class ButtonDettagliPrenotazioneLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Dettagli prenotazione")

    def send_request(self) -> None:
        self.view: LibroComponentPrenotazione  # TODO: make a generic class
        self.view.notify(message="visualizza_dettagli_prenotazione",
                         data={"libro": self.view.libro,
                               "prenotazione": self.view.prenotazione})


class ButtonCancellaPrenotazioneLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Cancella prenotazione")

    def send_request(self) -> None:
        self.view: LibroComponentPrenotazione  # TODO: make a generic class
        self.view.notify(message="cancella_prenotazione",
                         data={"catalogo": self.view.catalogo,
                               "libro": self.view.libro,
                               "prenotazione": self.view.prenotazione,
                               "contesto": self.view.context})


class ButtonGoToLibriPrenotati(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Indietro")

    def send_request(self) -> None:
        self.view: LibroComponentPrenotazione
        self.view.notify(message=REQUEST_GO_TO_LIBRI_PRENOTATI)
