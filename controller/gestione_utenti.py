from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from view.Gestione_utente.visualizza_utente import VisualizzaUtente
from view.Gestione_utente.ricerca_utente import RicercaView
from model.utente import Utente
from view.component.view_errore import view_errore
from view.Gestione_utente.visualizza_cronologia import VisualizzaCronologia


class GestioneUtentiController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "visualizza_utente":
            self.redirect(VisualizzaUtente())
        elif message == "ricerca_utente":
            self.redirect(RicercaView())
        elif message == "trova_utente":
            utente = Utente.by_username(self,data["username"])
            if utente and utente.ruolo=="utente":
                prestiti = Utente.visualizza_cronologia(self,utente)
                self.redirect(VisualizzaCronologia(prestiti))
            else:
                view_errore("Errore","L'utente non è presente nel sistema")



