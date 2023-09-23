from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from model.utente import Utente
from model.prestito import Prestito
from view.homepage import HomeOperatoreView


class PrenotazioniLibri(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "ricerca_prenotazioni":
            self.ricerca_prenotazioni(data)





    def ricerca_prenotazioni(self, data: Optional[dict] = None) -> None:
        if data["data"]:
            results = Utente.by_username(self, data["data"])
            if results:
                from model.prenotazione_libro import PrenotazioneLibro
                prenotazioni = PrenotazioneLibro.query_prenotazioni_valide(self, results)
                from view.lista_prenotazioni_utente import ListaPrenotazioniLibriUtente
                self.redirect(ListaPrenotazioniLibriUtente(results, prenotazioni))








