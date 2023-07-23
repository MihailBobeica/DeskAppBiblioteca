from typing import Dict
from abstract.model import Model
from database import Session
from database import Utente as DbUtente


class Utente(Model):

    def by_username(self, username):
        db_session = Session()
        utente = db_session.query(DbUtente).filter_by(username=username).first()
        db_session.close()
        return utente

    def inserisci(self, dati: Dict[str, str]):
        db_session = Session()
        utente = DbUtente(nome=dati["nome"],
                          cognome=dati["cognome"],
                          ruolo=dati["ruolo"],
                          username=dati["username"],
                          password=dati["password"])
        if Utente.by_username(self,utente.username):
            from view.component.view_errore import view_errore
            view_errore.create_layout(self,"Errore","L'operatore è già presente nel sistema")
        else:
            db_session.add(utente)
            db_session.commit()
            db_session.close()

    def __init__(self):
        super().__init__()


