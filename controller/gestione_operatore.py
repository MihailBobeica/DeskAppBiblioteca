from abstract import Controller, BoundedModel
from typing import Optional
from view.CRUD_Operatore.gestione_operatore import GestioneOperatori
from view.CRUD_Operatore.crea_operatore import ProvaView
from view.CRUD_Operatore.ricerca_operatore import RicercaView
from view.CRUD_Operatore.modifica_operatore import ModificaView
from view.CRUD_Operatore.Visualizza_operatore import VisualizzaView

class CRUD_operatore(Controller):
    def __init__(self):
        super().__init__()

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "crea_operatore":
            self.redirect(ProvaView())
        elif message == "elimina_operatore":
            self.redirect(RicercaView({"metodo" : "elimina"}))
        elif message == "modifica_operatore":
            self.redirect(RicercaView({"metodo" : "modifica"}))
        elif message == "visualizza_operatore":
            self.redirect(RicercaView({"metodo" : "visualizza"}))
        elif message == "trova_operatore":
            pass

