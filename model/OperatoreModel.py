from typing import Dict, Type

from PySide6.QtWidgets import QMessageBox
from sqlalchemy import or_,and_
from abstract.model import Model
from database import Session
from database import Operatore as DbOp
from database import Prestito
from model.utente import Utente


class OperatoreModel(Model):

    def by_username(self, username):
        db_session = Session()
        utente = db_session.query(DbOp).filter_by(username=username).first()
        db_session.close()
        return utente

    def inserisci(self, dati: Dict[str, str]):
        db_session = Session()
        utente = DbOp(nome=dati["nome"],
                          cognome=dati["cognome"],
                          ruolo=dati["ruolo"],
                          username=dati["username"],
                          password=dati["password"])
        if OperatoreModel().by_username(utente.username):
            from view.component.view_errore import view_errore
            view_errore.create_layout(self, "Errore", "L'operatore è già presente nel sistema")
        else:
            db_session.add(utente)
            db_session.commit()
            db_session.close()

    def elimina(self, utente:DbOp):
        db_session = Session()
        db_session.delete(utente)
        db_session.commit()
        db_session.close()

    def modifica(self, dati: Dict[str, str]):
        db_session = Session()
        utente = OperatoreModel().by_username(dati['username'])
        utente.nome = dati['nome']
        utente.cognome = dati['cognome']
        db_session.merge(utente)
        db_session.commit()
        db_session.close()