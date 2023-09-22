from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from view.Gestione_utente.gestione_utenti import GestioneUtentiView
from view.Gestione_utente.visualizza_utente import VisualizzaUtente
from view.Gestione_utente.ricerca_utente import RicercaUtenteView
from model.utente import Utente
from view.component.view_errore import view_errore
from view.Gestione_utente.visualizza_cronologia import VisualizzaCronologia
from model.prestito import Prestito


class GestioneUtentiController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "visualizza_utente":
            self.redirect(VisualizzaUtente())
        elif message == "ricerca_utente":
            self.redirect(RicercaUtenteView())
        elif message == "trova_utente":
            utente = Utente.by_username(self,data["username"])
            if utente and utente.ruolo=="utente":
                self.visualizza_cronologia(utente)
            else:
                view_errore("Errore","L'utente non è presente nel sistema")
        elif message == "mia_cronologia":
            pass
        elif message == "go_to_gestione_utenti":
            self.redirect(GestioneUtentiView())

    def visualizza_cronologia(self, utente):
        prestiti = Prestito.by_utente(self, utente.id)
        self.redirect(VisualizzaCronologia(prestiti))
