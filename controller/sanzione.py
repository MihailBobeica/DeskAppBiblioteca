from typing import Optional

from abstract import Controller, BoundedModel
from model.prestito import Prestito
from model.sanzione import Sanzione
from model.utente import Utente


class SanzioneController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models)

        self.libro_non_restituito()

    def libro_non_restituito(self):
        model_utente: Utente = self.models["utenti"]
        model_prestito: Prestito = self.models["prestiti"]
        model_sanzione: Sanzione = self.models["sanzioni"]
        utenti = model_utente.all()
        for utente in utenti:
            prestiti_scaduti = model_prestito.scaduti(utente)
            for prestito_scaduto in prestiti_scaduti:
                is_registered = model_sanzione.is_registered(utente, prestito_scaduto)
                if not is_registered:
                    model_sanzione.from_libro_non_restituito(utente, prestito_scaduto)

