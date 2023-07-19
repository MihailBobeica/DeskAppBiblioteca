from typing import Dict, List

from abstract.model import Model
from database import Session
from database import Utente as DbUtente


class Utente(Model):
    def __init__(self):
        super().__init__()

    def inserisci(self, dati: Dict[str, str]):
        db_session = Session()
        utente = DbUtente(nome=dati["nome"],
                          cognome=dati["cognome"],
                          ruolo=dati["ruolo"],
                          username=dati["username"],
                          password=dati["password"])
        db_session.add(utente)
        db_session.commit()
        db_session.close()

    def by_username(self, username):
        db_session = Session()
        utente = db_session.query(DbUtente).filter_by(username=username).first()
        db_session.close()
        return utente

    def seed_db(self, lista_dati: List[Dict[str, str]]):
        for dati in lista_dati:
            self.inserisci(dati)
