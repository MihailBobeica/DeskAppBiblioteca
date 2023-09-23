'''from abstract import Controller, BoundedModel
from typing import Optional
from view.CRUD_Operatore.gestione_operatore import GestioneOperatori
from view.inserisci_libro import InserisciView
#from view.gestione_libri_admin.catalogo_admin import CatalogoComponent
from view.Gestione_utente.gestione_utenti import GestioneUtentiView

class AdminController(Controller):
    def __init__(self):
        super().__init__()

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "gestione_operatori":
            self.redirect(GestioneOperatori())
        elif message == "inserisci_libro":
            self.redirect(InserisciView())
        elif message == "ricerca_libro":
            self.redirect(CatalogoComponent())
        elif message == "gestione_utenti":
            self.redirect(GestioneUtentiView())'''




