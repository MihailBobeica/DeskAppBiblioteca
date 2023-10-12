from abstract import Model
from database import Aula
from database import Session


class ModelAule(Model):
    def inserisci(self, nome):
        db_session = Session()
        aula = Aula(nome=nome)
        db_session.add(aula)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()
