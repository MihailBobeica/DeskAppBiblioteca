from abstract import Controller
from database import Libro
from model import ModelLibriOsservati, ModelPrenotazioniLibri
from model.prestiti import ModelPrestiti
from utils.auth import auth
from utils.strings import *
from view.catalogo import ListaDiOsservazioneView
from view.component import CatalogoComponent


class ControllerLibriOsservati(Controller):
    def __init__(self,
                 model_libri_osservati: ModelLibriOsservati,
                 model_prenotazioni_libri: ModelPrenotazioniLibri,
                 model_prestiti: ModelPrestiti):
        self.model_libri_osservati = model_libri_osservati
        self.model_prenotazioni_libri = model_prenotazioni_libri
        self.model_prestiti = model_prestiti
        super().__init__()

    def osserva_libro(self, libro: Libro):
        # check se l'utente sta già osservando questo libro
        gia_osservato = self.model_libri_osservati.gia_osservato(auth.user, libro)
        if gia_osservato:
            self.alert(title=ALERT_TITLE_OSSERVA_LIBRO,
                       message=ALERT_MESSAGE_LIBRO_GIA_OSSERVATO)
            return

        # check se l'utente ha già preso in prestito questo libro
        has_already_this_prestito = self.model_prestiti.gia_in_prestito(auth.user, libro)
        if has_already_this_prestito:
            self.alert(title=ALERT_TITLE_PRENOTAZIONE_NEGATA,
                       message=ALERT_MESSAGE_LIBRO_IN_PRESTITO)
            return

        # check se l'utente ha già prenotato questo libro
        has_already_this_prenotazione = self.model_prenotazioni_libri.gia_prenotato(utente=auth.user,
                                                                                    libro=libro)
        if has_already_this_prenotazione:
            self.alert(title=ALERT_TITLE_OSSERVA_LIBRO,
                       message=ALERT_MESSAGE_LIBRO_GIA_PRENOTATO)
            return

        # check se l'utente non ha fatto il numero massimo di prenotazioni
        has_max_osservazioni = self.model_libri_osservati.limite_raggiunto(utente=auth.user)
        if has_max_osservazioni:
            self.alert(title=ALERT_TITLE_OSSERVA_LIBRO,
                       message=ALERT_MAX_OSSERVAZIONI_MESSAGE)
            return

        self.model_libri_osservati.aggiungi(utente=auth.user,
                                            libro=libro)

        self.redirect(ListaDiOsservazioneView())

    def rimuovi_libro_osservato(self, libro: Libro, catalogo: CatalogoComponent):
        self.model_libri_osservati.rimuovi(auth.user, libro)
        catalogo.refresh()
