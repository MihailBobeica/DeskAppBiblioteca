from typing import Dict
from abstract.model import Model
from database import Session
from database import Aula as DbAula


class Aula(Model):
    def inserisci(self, dati: Dict[str, str]):
        db_session = Session()
        aula = DbAula(nome=dati["nome"])
        db_session.add(aula)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()
