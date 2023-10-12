from abstract import Model
from database import Posto
from database import Session


class ModelPosti(Model):
    def inserisci(self,
                  nome: str,
                  aula: str):
        db_session = Session()
        posto = Posto(nome=nome,
                      aula=aula)
        db_session.add(posto)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()
