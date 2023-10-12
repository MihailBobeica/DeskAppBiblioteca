from abstract import Controller
from model import ModelUtenti
from view.admin import GestioneUtentiView


class ControllerUtenti(Controller):
    def __init__(self,
                 model_utenti: ModelUtenti):
        self.model_utenti = model_utenti
        super().__init__()

    def _fill_table_gestione_utenti(self, view: GestioneUtentiView, text: str):
        utenti = self.model_utenti.by_text(text)
        for utente in utenti:
            view.add_row_table(id_utente=utente.id,
                               username=utente.username,
                               nome=utente.nome,
                               cognome=utente.cognome)
