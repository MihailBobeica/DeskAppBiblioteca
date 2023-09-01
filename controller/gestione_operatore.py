from PySide6.QtWidgets import QMessageBox

from abstract import Controller
from typing import Optional
from view.CRUD_Operatore.crea_operatore import ProvaView
from view.CRUD_Operatore.ricerca_operatore import RicercaView
from view.CRUD_Operatore.modifica_operatore import ModificaView
from view.CRUD_Operatore.Visualizza_operatore import VisualizzaView
from model.utente import Utente
from view.homepage.admin import HomeAdminView
from view.component.view_errore import view_errore

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
            utente = Utente.by_username(self, data["input"])
            if utente and utente.ruolo == "operatore":
                if data["metodo"] == "elimina":
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Question)
                    msg_box.setText("Sei sicuro di voler eliminare l'operatore?")
                    msg_box.setWindowTitle("Conferma")
                    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg_box.setDefaultButton(QMessageBox.Ok)
                    response = msg_box.exec()
                    if response == QMessageBox.Ok:
                        Utente.elimina(self,utente)
                    self.redirect(HomeAdminView())

                elif data["metodo"] == "modifica":
                    self.redirect(ModificaView(utente))
                elif data["metodo"] == "visualizza":
                    self.redirect(VisualizzaView(utente))

            else:
                view_errore("Errore","L'operatore non è presente nel sistema")

        elif message == "salva_modifiche":
            Utente.modifica(self, data)
            self.redirect(HomeAdminView())
