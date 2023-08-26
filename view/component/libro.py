from database import BoundedDbModel
from utils.key import KeyButtonComponent, KeyDb
from utils.key import KeyLabelComponent
from view.component.button import *
from view.scaffold import LibroComponentScaffold


class LibroComponentGuest(LibroComponentScaffold):
    def __init__(self, catalogo: BoundedView, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(catalogo=catalogo, data=data)

        self.add_labels((KeyLabelComponent.TITOLO,
                         KeyLabelComponent.AUTORI))

        self.add_buttons((KeyButtonComponent.VISUALIZZA_LIBRO,))


class LibroComponentUtente(LibroComponentScaffold):
    def __init__(self, catalogo: BoundedView, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(catalogo=catalogo, data=data)

        self.add_labels((KeyLabelComponent.TITOLO,
                         KeyLabelComponent.AUTORI,
                         KeyLabelComponent.ANNO_EDIZIONE,
                         KeyLabelComponent.DISPONIBILI))

        if self.libro.disponibili > 0:
            self.add_buttons((KeyButtonComponent.PRENOTA_LIBRO,))
        else:
            self.add_buttons((KeyButtonComponent.OSSERVA_LIBRO,))
        self.add_buttons((KeyButtonComponent.VISUALIZZA_LIBRO,))


class LibroPrenotatoComponent(LibroComponentScaffold):
    def __init__(self, catalogo: BoundedView, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(catalogo=catalogo, data=data)

        self.add_labels((KeyLabelComponent.TITOLO,
                         KeyLabelComponent.AUTORI,
                         KeyLabelComponent.SCADENZA_PRENOTAZIONE_LIBRO))

        self.add_buttons((KeyButtonComponent.DETTAGLI_PRENOTAZIONE_LIBRO,
                          KeyButtonComponent.CANCELLA_PRENOTAZIONE_LIBRO,
                          KeyButtonComponent.VISUALIZZA_LIBRO))
