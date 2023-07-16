from abstract.model import Model
from database import Utente, Session

db_session = Session()


class GestisciUtente(Model):
    def __init__(self):
        super().__init__()

    def get_utente_by_username(self, username):
        print(username)
        utente = db_session.query(Utente).filter(Utente.username == username).first()
        print(utente.password)
        return utente
