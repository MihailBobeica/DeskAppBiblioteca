from typing import Optional

from abstract import Controller, BoundedModel
from utils.request import Request
from view.libri_in_prestito import LibriInPrestitoView
from view.libri_osservati import LibriOsservatiView
from view.lista_prenotazioni import ListaPrenotazioniView
from view.scegli_prenotazione import ScegliPrenotazione


class RouterController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: Request, data: Optional[dict] = None) -> None:
        if message == Request.GO_TO_PRENOTA_POSTO:
            self.redirect(ScegliPrenotazione())
        elif message == Request.GO_TO_POSTI_PRENOTATI:
            self.redirect(ListaPrenotazioniView())
        elif message == Request.GO_TO_LISTA_DI_OSSERVAZIONE:
            self.redirect(LibriOsservatiView())
        elif message == Request.GO_TO_LIBRI_IN_PRESTITO:
            self.redirect(LibriInPrestitoView())

