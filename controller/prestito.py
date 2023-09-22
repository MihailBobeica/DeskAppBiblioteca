from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from model.utente import Utente
from model.prestito import Prestito
from view.homepage import HomeOperatoreView


class PrestitoController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "ricerca_prestito":
            self.ricerca_prestito(data)
        elif message == "registra_prestito":
            self.registra_prestito(data)
        elif message == "restituito":
            self.restituito(data)



    def ricerca_prestito(self, data: Optional[dict] = None) -> None:
        if data["data"]:
            results = Utente.by_username(self, data["data"])
            if results:
                prestiti = Prestito.da_restituire(self,results.id)
                from view.restituzione.libro_restituzione import Restituzione
                self.redirect(Restituzione(results,prestiti))


    def restituito(self, data: Optional[dict] = None) -> None:
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Conferma")
        confirm_dialog.setText("Vuoi confermare l'avvenuta restituzione del prestito del libro?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        result = confirm_dialog.exec_()
        if result == QMessageBox.Yes:
            from model.prestito import Prestito
            Prestito.restituzione(self, data["prestito"])
            self.redirect(HomeOperatoreView)
        else:
            pass


    def registra_prestito(self, data: Optional[dict] = None) -> None:
        if(Prestito.check_max(self,data["utente"])):
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
        else:
            pass