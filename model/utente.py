from abstract.model import Model
from database import Session
from database import Utente as DbUtente

db_session = Session()


class Utente(Model):
    @staticmethod
    def by_username(username):
        utente = db_session.query(DbUtente).filter(DbUtente.username == username).first()
        return utente
