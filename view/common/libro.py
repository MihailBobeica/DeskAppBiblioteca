from database import Libro, PrenotazioneLibro, Prestito
from utils.backend import MINIMO_COPIE_DISPONIBILI
from utils.ui import font_16
from view.scaffold import DettagliViewScaffold


class DettagliLibroGuestView(DettagliViewScaffold):
    def __init__(self, libro: Libro):
        super().__init__(libro=libro)

        self.add_labels(("titolo",
                         "autori",
                         "anno_edizione",
                         "anno_pubblicazione",
                         "editore"),
                        transform=font_16)


class DettagliLibroUtenteView(DettagliViewScaffold):
    def __init__(self, libro: Libro):
        super().__init__(libro=libro)

        self.add_labels(("titolo",
                         "autori",
                         "anno_edizione",
                         "anno_pubblicazione",
                         "editore",
                         "disponibili",
                         "dati",
                         "isbn"),
                        transform=font_16)

        if self.libro.disponibili > MINIMO_COPIE_DISPONIBILI:
            self.add_buttons(("prenota_libro",))
        else:
            self.add_buttons(("osserva_libro",))


class DettagliPrenotazioneLibroView(DettagliViewScaffold):
    def __init__(self, libro: Libro, prenotazione_libro: PrenotazioneLibro):
        super().__init__(libro=libro,
                         prenotazione_libro=prenotazione_libro)

        self.add_labels(("titolo",
                         "autori",
                         "data_prenotazione_libro",
                         "scadenza_prenotazione_libro",
                         "codice_prenotazione_libro"),
                        transform=font_16)

        self.add_buttons(("cancella_prenotazione_libro",
                          "go_to_libri_prenotati"))


class DettagliPrestitoView(DettagliViewScaffold):
    def __init__(self, libro: Libro, prestito: Prestito):
        super().__init__(libro=libro,
                         prestito=prestito)

        self.add_labels(("titolo",
                         "autori",
                         "inizio_prestito",
                         "fine_prestito"),
                        transform=font_16)

        self.add_buttons(("go_to_libri_in_prestito",))
