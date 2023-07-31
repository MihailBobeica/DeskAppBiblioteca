# TODO: da eliminare

from abstract.controller import Controller
from database import Utente, Session
from utils.auth import hash_password


class gestione_operatore(Controller):

    def crea_operatore(self, nome, cognome, username, password):
        db_session = Session()
        utente = Utente(nome=nome, cognome=cognome, ruolo="operatore", username=username,
                        password=hash_password(password))
        db_session.add(utente)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()
