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
        elif message == "registra_prestito":
            self.registra_prestito(data)




    def ricerca_prenotazioni(self, data: Optional[dict] = None) -> None:
        if data["data"]:
            results = Utente.by_username(self, data["data"])
            if results:
                from model.prenotazione_libro import PrenotazioneLibro
                prenotazioni = PrenotazioneLibro.query_prenotazioni_valide(self, results)
                from view.lista_prenotazioni_utente import ListaPrenotazioniUtente
                self.redirect(ListaPrenotazioniUtente(results, prenotazioni))




    def registra_prestito(self, data: Optional[dict] = None) -> None:
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Conferma")
        confirm_dialog.setText("Vuoi confermare l'avvenuto prestito del libro?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        result = confirm_dialog.exec_()
        if result == QMessageBox.Yes:
            dati = {
                "libro": data["libro"],
                "utente": data["utente"]
            }
            Prestito.inserisci(self, dati)
            from model.prenotazione_libro import PrenotazioneLibro
            PrenotazioneLibro.cancella(self, data["prenotazione"])
            self.redirect(HomeOperatoreView())
        else:
            pass



