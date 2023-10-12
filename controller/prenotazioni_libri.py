from datetime import datetime

from PySide6.QtWidgets import QMessageBox

from abstract import Controller
from database import Libro, PrenotazioneLibro
from model import ModelPrenotazioniLibri, ModelSanzioni, ModelPrestiti
from utils.auth import auth
from utils.strings import *
from view.component import CatalogoComponent
from view.component.catalogo import LibriPrenotatiView
from view.operatore import RegistraPrestitoView


class ControllerPrenotazioniLibri(Controller):
    def __init__(self,
                 model_prenotazioni_libri: ModelPrenotazioniLibri,
                 model_sanzioni: ModelSanzioni,
                 model_prestiti: ModelPrestiti):
        self.model_prenotazioni_libri = model_prenotazioni_libri
        self.model_sanzioni = model_sanzioni
        self.model_prestiti = model_prestiti
        super().__init__()

    def prenota_libro(self, libro: Libro):
        # check se l'utente non è sanzionato
        is_sanzionato = self.model_sanzioni.is_sanzionato(auth.user)
        if is_sanzionato:
            self.alert(title=ALERT_TITLE_PRENOTAZIONE_NEGATA,
                       message=ALERT_MESSAGE_UTENTE_SANZIONATO)
            return
        # check se l'utente ha già preso in prestito questo libro
        has_already_this_prestito = self.model_prestiti.gia_in_prestito(auth.user, libro)
        if has_already_this_prestito:
            self.alert(title=ALERT_TITLE_PRENOTAZIONE_NEGATA,
                       message=ALERT_MESSAGE_LIBRO_IN_PRESTITO)
            return

        # check se l'utente ha già prenotato questo libro
        has_already_this_prenotazione = self.model_prenotazioni_libri.gia_prenotato(utente=auth.user, libro=libro)
        if has_already_this_prenotazione:
            self.alert(title=ALERT_TITLE_PRENOTAZIONE_NEGATA,
                       message=ALERT_MESSAGE_LIBRO_GIA_PRENOTATO)
            return
        # check se l'utente non ha fatto il numero massimo di prenotazioni
        has_max_prenotazioni = self.model_prenotazioni_libri.limite_raggiunto(utente=auth.user)
        if has_max_prenotazioni:
            self.alert(title=ALERT_TITLE_PRENOTAZIONE_NEGATA,
                       message=ALERT_MAX_PRENOTAZIONI_MESSAGE)
            return
        # il controllo della disponibilità del libro è stato già fatto

        # aggiungi prenotazione
        response = self.confirm(title=CONFIRM_PRENOTAZIONE_LIBRO_TITLE,
                                message=CONFIRM_PRENOTAZIONE_LIBRO_MESSAGE.format(libro.titolo))
        if response == QMessageBox.StandardButton.Yes:
            self.model_prenotazioni_libri.aggiungi(auth.user, libro)
            self.redirect(LibriPrenotatiView())

    def cancella_prenotazione_libro(self, prenotazione_libro: PrenotazioneLibro, catalogo: CatalogoComponent):
        libro = self.model_prenotazioni_libri.get_libro(prenotazione_libro)
        response = self.confirm(title=CANCELLA_PRENOTAZIONE_TITLE,
                                message=CONFIRM_CANCELLA_PRENOTAZIONE_MESSAGE.format(libro.titolo))
        if response == QMessageBox.StandardButton.Yes:
            response = self.confirm(title=CANCELLA_PRENOTAZIONE_TITLE,
                                    message="Verrai temporaneamente sospeso"
                                            "\ndal servizio di prenotazione libri.")
            if response == QMessageBox.StandardButton.Yes:
                self.model_prenotazioni_libri.cancella(prenotazione_libro)

                data_fine = datetime.now() + (datetime.now() - prenotazione_libro.data_prenotazione)
                self.model_sanzioni.da_cancella_prenotazione(auth.user, data_fine)

                if catalogo:
                    catalogo.refresh()
                else:
                    self.redirect(LibriPrenotatiView())

    def _fill_view_registra_prestito(self, view: RegistraPrestitoView, text: str):
        utenti_con_prenotazioni = self.model_prenotazioni_libri.get_utenti_con_prenotazioni_by_text(text)
        for utente in utenti_con_prenotazioni:
            prenotazioni = self.model_prenotazioni_libri.valide_by_utente(utente)
            libri = [self.model_prenotazioni_libri.get_libro(prenotazione) for prenotazione in prenotazioni]
            dati = [{"id_prenotazione": prenotazione.id,
                     "titolo": libro.titolo,
                     "autori": libro.autori,
                     "isbn": libro.isbn,
                     "codice": prenotazione.codice}
                    for prenotazione, libro in zip(prenotazioni, libri)]
            view.add_dati(utente.username, utente.nome, utente.cognome, dati)
