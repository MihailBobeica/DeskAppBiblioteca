from abstract import Controller
from model import ModelPrenotazioniLibri, ModelLibriOsservati
from utils.auth import auth
from utils.backend import MINIMO_COPIE_DISPONIBILI
from utils.strings import *


class ControllerNotifiche(Controller):
    def __init__(self,
                 model_libri_osservati: ModelLibriOsservati,
                 model_prenotazioni_libri: ModelPrenotazioniLibri):
        self.model_libri_osservati = model_libri_osservati
        self.model_prenotazioni_libri = model_prenotazioni_libri
        super().__init__()

    def check_libri_osservati(self):
        libri_osservati = self.model_libri_osservati.by_utente(auth.user)
        for libro_osservato in libri_osservati:
            if libro_osservato.disponibili > MINIMO_COPIE_DISPONIBILI:
                self.model_libri_osservati.rimuovi(auth.user, libro_osservato)
                self.alert(title=ALERT_LIBRO_ORA_DISPONIBILE_TITLE,
                           message=ALERT_LIBRO_ORA_DISPONIBILE_MESSAGE.format(libro_osservato.titolo))

    def check_scadenza_prenotazioni(self):
        prenotazioni_quasi_scadute = self.model_prenotazioni_libri.quasi_scadute(auth.user)
        for p in prenotazioni_quasi_scadute:
            self.alert(title="Prenotazione quasi scaduta",
                       message=f"Hai una prenotazione che sta"
                               f"\nper scadere il:"
                               f"\n{p.data_scadenza}")
