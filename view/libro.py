from utils.key import *
from utils.ui import font_16
from view.component.label import *
from view.scaffold import LibroViewScaffold


class LibroViewGuest(LibroViewScaffold):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(data=data)

        self.add_labels((KeyLabelComponent.TITOLO,
                         KeyLabelComponent.AUTORI,
                         KeyLabelComponent.ANNO_EDIZIONE,
                         KeyLabelComponent.ANNO_PUBBLICAZIONE,
                         KeyLabelComponent.EDITORE),
                        transform=font_16)


class LibroViewUtente(LibroViewScaffold):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(data=data)

        self.add_labels((KeyLabelComponent.TITOLO,
                         KeyLabelComponent.AUTORI,
                         KeyLabelComponent.ANNO_EDIZIONE,
                         KeyLabelComponent.ANNO_PUBBLICAZIONE,
                         KeyLabelComponent.EDITORE,
                         KeyLabelComponent.DISPONIBILI,
                         KeyLabelComponent.DATI,
                         KeyLabelComponent.ISBN),
                        transform=font_16)

        if self.libro.disponibili > 0:
            self.add_buttons((KeyButtonComponent.PRENOTA_LIBRO,))
        else:
            self.add_buttons((KeyButtonComponent.OSSERVA_LIBRO,))


class PrenotazioneLibroView(LibroViewScaffold):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(data=data)

        self.add_labels((KeyLabelComponent.TITOLO,
                         KeyLabelComponent.AUTORI,
                         KeyLabelComponent.DATA_PRENOTAZIONE_LIBRO,
                         KeyLabelComponent.SCADENZA_PRENOTAZIONE_LIBRO,
                         KeyLabelComponent.CODICE_PRENOTAZIONE_LIBRO),
                        transform=font_16)

        self.add_buttons((KeyButtonComponent.CANCELLA_PRENOTAZIONE_LIBRO,
                          KeyButtonComponent.GO_TO_LIBRI_PRENOTATI))
