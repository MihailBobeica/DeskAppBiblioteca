from abstract import Model
from database import Session
from database import User


class ModelUsers(Model):
    def inserisci(self,
                  nome: str,
                  cognome: str,
                  ruolo: str,
                  username: str,
                  password: str):
        db_session = Session()
        user = User(nome=nome,
                    cognome=cognome,
                    ruolo=ruolo,
                    username=username,
                    password=password)
        db_session.add(user)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()

    def by_username(self, username: str) -> User:
        db_session = Session()
        user = db_session.query(User).filter(User.username == username).first()
        db_session.close()
        return user
