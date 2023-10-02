from abc import abstractmethod

from PySide6.QtWidgets import QPushButton

from abstract import BoundedView
from view.scaffold import DettagliScaffold


class RequestButton(QPushButton):
    def __init__(self, view: BoundedView):
        super().__init__()
        self.view: DettagliScaffold = view
        self.clicked.connect(self.send_request)

    @abstractmethod
    def send_request(self) -> None:
        ...


class ButtonGoToDettagliLibroGuest(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Visualizza")

    def send_request(self) -> None:
        self.view.notify(message="go_to_dettagli_libro_guest",
                         data={"libro": self.view.libro})


class ButtonGoToDettagliLibroUtente(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Visualizza")

    def send_request(self) -> None:
        self.view.notify(message="go_to_dettagli_libro_utente",
                         data={"libro": self.view.libro})


class ButtonPrenotaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Prenota libro")

    def send_request(self) -> None:
        self.view.notify(message="prenota_libro",
                         data={"libro": self.view.libro})


class ButtonOsservaLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Osserva libro")

    def send_request(self) -> None:
        self.view.notify(message="osserva_libro",
                         data={"libro": self.view.libro})


class ButtonGoToDettagliPrenotazioneLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Dettagli prenotazione")

    def send_request(self) -> None:
        self.view.notify(message="go_to_dettagli_prenotazione_libro",
                         data={"libro": self.view.libro,
                               "prenotazione_libro": self.view.prenotazione_libro})


class ButtonCancellaPrenotazioneLibro(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Cancella prenotazione")

    def send_request(self) -> None:
        self.view.notify(message="cancella_prenotazione_libro",
                         data={"catalogo": self.view.catalogo,
                               "prenotazione_libro": self.view.prenotazione_libro})


class ButtonGoToLibriPrenotati(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Indietro")

    def send_request(self) -> None:
        self.view.notify(message="go_to_libri_prenotati")


class ButtonGoToLibriInPrestito(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Indietro")

    def send_request(self) -> None:
        self.view.notify(message="go_to_libri_in_prestito")


class ButtonRimuoviLibroOsservato(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Rimuovi")

    def send_request(self) -> None:
        self.view.notify(message="rimuovi_libro_osservato",
                         data={"catalogo": self.view.catalogo,
                               "libro": self.view.libro})


class ButtonGoToDettagliPrestito(RequestButton):
    def __init__(self, view: BoundedView):
        super().__init__(view=view)
        self.setText("Dettagli prestito")

    def send_request(self) -> None:
        self.view.notify(message="go_to_dettagli_prestito",
                         data={"libro": self.view.libro,
                               "prestito": self.view.prestito}
                         )
