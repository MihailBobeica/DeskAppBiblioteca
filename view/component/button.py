from abc import abstractmethod

from PySide6.QtWidgets import QPushButton

from abstract import BoundedView
from utils.key import KeyDb
from utils.request import Request
from view.scaffold import LibroScaffold


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
        self.view: LibroScaffold
        self.view.notify(message=Request.GO_TO_VISUALIZZA_LIBRO,
                         data=self.view.data)


class ButtonPrenotaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Prenota libro")

    def send_request(self) -> None:
        self.view: LibroScaffold
        self.view.notify(message=Request.PRENOTA_LIBRO,
                         data={KeyDb.LIBRO: self.view.libro})


class ButtonOsservaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Osserva libro")

    def send_request(self) -> None:
        self.view: LibroScaffold
        self.view.notify(message=Request.OSSERVA_LIBRO,
                         data={KeyDb.LIBRO: self.view.libro})


class ButtonDettagliPrenotazioneLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Dettagli prenotazione")

    def send_request(self) -> None:
        self.view: LibroScaffold
        self.view.notify(message=Request.GO_TO_DETTAGLI_PRENOTAZIONE_LIBRO,
                         data={KeyDb.LIBRO: self.view.libro,
                               KeyDb.PRENOTAZIONE_LIBRO: self.view.prenotazione})


class ButtonCancellaPrenotazioneLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Cancella prenotazione")

    def send_request(self) -> None:
        self.view: LibroScaffold
        self.view.notify(message=Request.CANCELLA_PRENOTAZIONE_LIBRO,
                         data={"catalogo": self.view.catalogo,
                               KeyDb.LIBRO: self.view.libro,
                               KeyDb.PRENOTAZIONE_LIBRO: self.view.prenotazione})


class ButtonGoToLibriPrenotati(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Indietro")

    def send_request(self) -> None:
        self.view: LibroScaffold
        self.view.notify(message=Request.GO_TO_LIBRI_PRENOTATI)
