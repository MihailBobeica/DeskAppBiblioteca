from PySide6.QtWidgets import QVBoxLayout

from database import BoundedDbModel
from view.component.button import *
from view.component.label import *
from view.component.libro_scaffold import LibroScaffold, LibroPrenotatoScaffold


class LibroComponentGuest(LibroScaffold):
    def __init__(self, catalogo: BoundedView, data: dict[str, BoundedDbModel]):
        super().__init__(catalogo=catalogo, data=data)

    def set_labels(self, layout: QVBoxLayout) -> None:
        layout.addWidget(LabelTitle(self.libro.titolo))
        layout.addWidget(LabelAutor(self.libro.autori))

    def set_buttons(self, layout: QVBoxLayout) -> None:
        layout.addWidget(ButtonVisualizzaLibro(self))


class LibroComponentUtente(LibroScaffold):
    def __init__(self, catalogo: BoundedView, data: dict[str, BoundedDbModel]):
        super().__init__(catalogo=catalogo, data=data)

    def set_labels(self, layout: QVBoxLayout) -> None:
        layout.addWidget(LabelTitle(self.libro.titolo))
        layout.addWidget(LabelAutor(self.libro.autori))
        layout.addWidget(LabelAnnoEdizione(self.libro.anno_edizione))
        layout.addWidget(LabelDisponibili(self.libro.disponibili))

    def set_buttons(self, layout: QVBoxLayout) -> None:
        if self.libro.disponibili > 0:
            layout.addWidget(ButtonPrenotaLibro(self))
        else:
            layout.addWidget(ButtonOsservaLibro(self))
        layout.addWidget(ButtonVisualizzaLibro(self))


class LibroPrenotatoComponent(LibroPrenotatoScaffold):
    def __init__(self, catalogo: BoundedView, data: dict[str, BoundedDbModel]):
        super().__init__(catalogo=catalogo, data=data)

    def set_labels(self, layout: QVBoxLayout) -> None:
        layout.addWidget(LabelTitle(self.libro.titolo))
        layout.addWidget(LabelAutor(self.libro.autori))
        layout.addWidget(LabelScadenzaPrenotazioneLibro(self.prenotazione.data_scadenza))

    def set_buttons(self, layout: QVBoxLayout) -> None:
        layout.addWidget(ButtonDettagliPrenotazioneLibro(self))
        layout.addWidget(ButtonCancellaPrenotazioneLibro(self))
        layout.addWidget(ButtonVisualizzaLibro(self))
