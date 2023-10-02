from abstract.model import Model
from database import Posto as DbPosto
from database import Session


class ModelPosti(Model):
    def inserisci(self,
                  nome: str,
                  aula: str):
        db_session = Session()
        posto = DbPosto(nome=nome,
                        aula=aula)
        db_session.add(posto)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()
