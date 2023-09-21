from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from model.utente import Utente



class PrenotazioniLibri(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "ricerca_prenotazioni":
            if data["data"]:
                results = Utente.by_username(self, data["data"])
                if results:
                    from view.lista_prenotazioni_utente import ListaPrenotazioniUtente
                    print(results)
                    self.redirect(ListaPrenotazioniUtente(results))

