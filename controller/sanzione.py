from typing import Optional

from abstract import Controller, BoundedModel
from model import PrenotazioneLibro
from model.prestito import Prestito
from model.sanzione import Sanzione
from model.utente import Utente


class SanzioneController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models)

        self.libro_non_restituito()
        self.libro_prenotato_ma_non_ritirato()

    def libro_non_restituito(self):
        model_utente: Utente = self.models["utenti"]
        model_prestito: Prestito = self.models["prestiti"]
        model_sanzione: Sanzione = self.models["sanzioni"]

        utenti = model_utente.all()
        for utente in utenti:
            prestiti_scaduti = model_prestito.scaduti(utente)
            for prestito_scaduto in prestiti_scaduti:
                is_registered = model_sanzione.prestito_is_registered(utente, prestito_scaduto)
                if not is_registered:
                    model_sanzione.from_libro_non_restituito(utente, prestito_scaduto)

    def libro_prenotato_ma_non_ritirato(self):
        model_utente: Utente = self.models["utenti"]
        model_prenotazione: PrenotazioneLibro = self.models["prenotazioni_libri"]
        model_sanzione: Sanzione = self.models["sanzioni"]

        utenti = model_utente.all()
        for utente in utenti:
            prenotazioni_scadute = model_prenotazione.scadute(utente)
            for prenotazione_scaduta in prenotazioni_scadute:
                is_registered = model_sanzione.prenotazione_is_registered(utente, prenotazione_scaduta)
                if not is_registered:
                    model_sanzione.from_libro_non_ritirato(utente, prenotazione_scaduta)
