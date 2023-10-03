from PySide6.QtWidgets import QMessageBox

from abstract import Controller
from model import ModelUsers
from model.operatori import ModelOperatori
from utils.strings import *
from view.admin.aggiungi_modifica_operatore import AggiungiModificaOperatoreView
from view.admin.gestione_operatori import GestioneOperatoriView


class ControllerOperatori(Controller):
    def __init__(self,
                 model_operatori: ModelOperatori,
                 model_users: ModelUsers):
        self.model_operatori = model_operatori
        self.model_utenti = model_users
        super().__init__()

    def modifica_operatore(self, id_operatore: int):
        operatore = self.model_operatori.by_id(id_operatore)
        self.redirect(AggiungiModificaOperatoreView(metodo="modifica", operatore=operatore))

    def elimina_operatore(self, id_operatore: int, view: GestioneOperatoriView):
        response = self.confirm(title=CONFIRM_TITLE_ELIMINA_OPERATORE,
                                message=CONFIRM_MESSAGE_ELIMINA_OPERATORE)
        if response == QMessageBox.StandardButton.Yes:
            self.model_operatori.elimina(id_operatore)
            view.search(view.searchbar.text())

    def aggiungi_modifica_operatore(self,
                                    metodo: str,
                                    id_operatore: int,
                                    username: str,
                                    nome: str,
                                    cognome: str,
                                    password: str):
        if metodo == "aggiungi":
            # controllo che lo username sia univoco
            is_username_univoco = self.model_utenti.is_username_univoco(username)
            if is_username_univoco:
                self.model_operatori.aggiungi(username=username,
                                              nome=nome,
                                              cognome=cognome,
                                              password=password)
                self.redirect(GestioneOperatoriView())
            else:
                self.alert(title=ALERT_TITLE_AGGIUNGI_OPERATORE,
                           message=ALERT_MESSAGE_USERNAME_NON_UNIVOCO)
        elif metodo == "modifica":
            self.model_operatori.modifica(id_operatore=id_operatore,
                                          nome=nome,
                                          cognome=cognome,
                                          password=password)
            self.redirect(GestioneOperatoriView())
        else:
            raise ValueError("metodo aggiungi/modifica operatore controller errato!")

    def _fill_table_gestione_operatori(self, view: GestioneOperatoriView, text: str):
        operatori = self.model_operatori.by_text(text)
        for operatore in operatori:
            view.add_row_table(id_operatore=operatore.id,
                               username=operatore.username,
                               nome=operatore.nome,
                               cognome=operatore.cognome)
