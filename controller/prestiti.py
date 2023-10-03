from PySide6.QtWidgets import QMessageBox

from abstract import Controller
from model import ModelLibri, ModelPrenotazioniLibri, ModelSanzioni
from model.prestiti import ModelPrestiti
from model.utenti import ModelUtenti
from utils.auth import auth
from utils.strings import *
from view.common.cronologia_prestiti import CronologiaPrestitiView
from view.operatore.registra_prestito import RegistraPrestitoView
from view.operatore.registra_restituzione import RegistraRestituzioneView


class ControllerPrestiti(Controller):
    def __init__(self,
                 model_prestiti: ModelPrestiti,
                 model_libri: ModelLibri,
                 model_utenti: ModelUtenti,
                 model_prenotazioni_libri: ModelPrenotazioniLibri,
                 model_sanzioni: ModelSanzioni):
        self.model_prestiti = model_prestiti
        self.model_libri = model_libri
        self.model_utenti = model_utenti
        self.model_prenotazioni_libri = model_prenotazioni_libri
        self.model_sanzioni = model_sanzioni
        super().__init__()

    def registra_prestito(self, id_prenotazione: int, view: RegistraPrestitoView):
        # controllare che l'utente non abbia al momento raggiunto il numero massimo di libri presi in prestito
        prenotazione = self.model_prenotazioni_libri.by_id(id_prenotazione)
        utente = self.model_utenti.by_prenotazione(prenotazione)
        has_max_prestiti = self.model_prestiti.has_max(utente)
        if has_max_prestiti:
            self.alert(title=ALERT_TITLE_MAX_PRESTITI,
                       message=ALERT_MESSAGE_MAX_PRESTITI)
            return
        # chiedere all'operatore di confermare il prestito
        response = self.confirm(title=CONFIRM_TITLE_REGISTRA_PRESTITO,
                                message=CONFIRM_MESSAGE_REGISTRA_PERSTITO)
        if response == QMessageBox.StandardButton.Yes:
            libro = self.model_libri.by_prenotazione(prenotazione)
            # registrare il prestito
            self.model_prestiti.aggiungi(utente, libro)

            # cancellare la prenotazione
            self.model_prenotazioni_libri.cancella(prenotazione)

            view.search(view.searchbar.text())

    def registra_restituzione_prestito(self, id_prestito: int, view: RegistraRestituzioneView):
        # chiedi conferma all'operatore
        response = self.confirm(title=CONFIRM_TITLE_REGISTRA_RESTITUZIONE_PRESTITO,
                                message=CONFIRM_MESSAGE_REGISTRA_RESTITUZIONE_PRESTITO)
        if response == QMessageBox.StandardButton.Yes:
            prestito = self.model_prestiti.by_id(id_prestito)
            # registra restituzione
            self.model_prestiti.restituzione(prestito)
            # controlla se il prestito è scaduto
            prestito_scaduto = self.model_prestiti.is_scaduto(prestito)
            if prestito_scaduto:
                # emetti una sanzione
                self.model_sanzioni.restituzione_in_ritardo(prestito)

                # notifica dell'emissione di una sanzione
                self.alert(title="Sanzione emessa",
                           message="Libro restituito in ritardo!")

            view.search(view.searchbar.text())

    def _fill_table_cronologia_prestiti(self, view: CronologiaPrestitiView):
        id_utente = auth.user.id
        if view.id_utente:
            id_utente = view.id_utente
        prestiti = self.model_prestiti.passati(id_utente)
        for prestito in prestiti:
            libro_preso = self.model_libri.by_id_prestito(prestito.id)
            view.add_row(libro_preso.titolo,
                         libro_preso.autori,
                         libro_preso.isbn,
                         prestito.data_inizio,
                         prestito.data_restituzione)

    def _fill_view_registra_restituzione_prestito(self, view: RegistraRestituzioneView, text: str):
        utenti_con_prestiti = self.model_prestiti.get_utenti_con_prestiti(text)
        for utente in utenti_con_prestiti:
            prestiti = self.model_prestiti.validi_by_utente(utente)
            libri = [self.model_prestiti.get_libro(prestito) for prestito in prestiti]
            dati = [{"id_prestito": prestito.id,
                     "titolo": libro.titolo,
                     "autori": libro.autori,
                     "isbn": libro.isbn,
                     "codice": prestito.codice,
                     "data_scadenza": prestito.data_scadenza}
                    for prestito, libro in zip(prestiti, libri)]
            view.add_dati(utente.username, utente.nome, utente.cognome, dati)
