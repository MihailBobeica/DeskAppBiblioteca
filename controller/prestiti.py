from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from model import ModelLibri
from model.utenti import ModelUtenti
from model.prestiti import ModelPrestiti
from utils.auth import auth
from view.common.cronologia_prestiti import CronologiaPrestitiView
from view.homepage import HomeOperatoreView


class ControllerPrestiti(Controller):
    def __init__(self,
                 model_prestiti: ModelPrestiti,
                 model_libri: ModelLibri):
        self.model_prestiti = model_prestiti
        self.model_libri = model_libri
        super().__init__()

    def _fill_table_cronologia_prestiti(self, view: CronologiaPrestitiView):
        id_utente = auth.user.id
        if view.id_utente:
            id_utente = view.id_utente
        prestiti = self.model_prestiti.passati(id_utente)
        print(prestiti)
        for prestito in prestiti:
            libro_preso = self.model_libri.by_prestito(prestito.id)
            view.add_row(libro_preso.titolo,
                         libro_preso.autori,
                         libro_preso.isbn,
                         prestito.data_inizio,
                         prestito.data_restituzione)

    def ricerca_prestito(self, data: Optional[dict] = None) -> None:
        if data["data"]:
            results = ModelUtenti.by_username(self, data["data"])
            if results:
                prestiti = ModelPrestiti.da_restituire(self, results.id)
                from view.restituzione.libro_restituzione import ConfermaRestituzioneView
                self.redirect(ConfermaRestituzioneView(results, prestiti))


    def registra_restituzione(self, data: Optional[dict] = None) -> None:  # TODO cambia il nome
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Conferma")
        confirm_dialog.setText("Vuoi confermare l'avvenuta restituzione del prestito del libro?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        result = confirm_dialog.exec_()
        if result == QMessageBox.Yes:
            from model.prestiti import ModelPrestiti
            ModelPrestiti.restituzione(self, data["prestito"])
            self.redirect(HomeOperatoreView())
        else:
            pass


    def registra_prestito(self, data: Optional[dict] = None) -> None:
        if(ModelPrestiti.check_max(self, data["utente"])):
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
                ModelPrestiti().inserisci(dati)
                from model.prenotazioni_libri import ModelPrenotazioniLibri
                ModelPrenotazioniLibri().cancella(data["prenotazione"])
                self.redirect(HomeOperatoreView())
            else:
                pass
        else:
            pass