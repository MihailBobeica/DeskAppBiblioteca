from database import BoundedDbModel
from utils.backend import MINIMO_COPIE_DISPONIBILI
from view.component.button import *
from view.scaffold import LibroComponentScaffold


class LibroComponentGuest(LibroComponentScaffold):
    def __init__(self, catalogo: BoundedView, dati: dict[str, BoundedDbModel]):
        super().__init__(catalogo, dati=dati)

        self.add_labels(("titolo",
                         "autori"))

        self.add_buttons(("go_to_dettagli_libro_guest",))


class LibroComponentUtente(LibroComponentScaffold):
    def __init__(self, catalogo: BoundedView, dati: dict[str, BoundedDbModel]):
        super().__init__(catalogo=catalogo, dati=dati)

        self.add_labels(("titolo",
                         "autori",
                         "anno_edizione",
                         "disponibili"))

        if self.libro.disponibili > MINIMO_COPIE_DISPONIBILI:
            self.add_buttons(("prenota_libro",))
        else:
            self.add_buttons(("osserva_libro",))
        self.add_buttons(("go_to_dettagli_libro_utente",))


class LibroPrenotatoComponent(LibroComponentScaffold):
    def __init__(self, catalogo: BoundedView, dati: dict[str, BoundedDbModel]):
        super().__init__(catalogo=catalogo, dati=dati)

        self.add_labels(("titolo",
                         "autori",
                         "scadenza_prenotazione_libro"))

        self.add_buttons(("go_to_dettagli_prenotazione_libro",
                          "cancella_prenotazione_libro"))


class LibroOsservatoComponent(LibroComponentScaffold):
    def __init__(self, catalogo: BoundedView, dati: dict[str, BoundedDbModel]):
        super().__init__(catalogo=catalogo, dati=dati)

        self.add_labels(("titolo",
                         "autori"))

        self.add_buttons(("rimuovi_libro_osservato",))


class LibroInPrestitoComponent(LibroComponentScaffold):
    def __init__(self, catalogo: BoundedView, dati: dict[str, BoundedDbModel]):
        super().__init__(catalogo=catalogo, dati=dati)

        self.add_labels(("titolo",
                         "autori"))

        self.add_buttons(("go_to_dettagli_prestito",))
