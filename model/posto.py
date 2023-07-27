from abstract.model import Model
from database import Session
from database import Posto as DbPosto
from typing import List, Type, Dict
from utils import POSTI

class Posto(Model):
    def inserisci(self, dati: Dict[str, str]):
        db_session = Session()
        posto = DbPosto(nome=dati["nome"],
                        aula=dati["aula"])
        db_session.add(posto)
        db_session.commit()
        db_session.close()

    def get_posti_by_aula(self, nome_aula: str, n: int = POSTI) -> List[Type[DbPosto]]:
        # Ottiene una sessione per l'accesso al database
        db_session = Session()

        # Esegue una query per ottenere i posti dell'aula specificata
        posti = db_session.query(DbPosto).filter_by(aula=nome_aula).limit(n).all()

        # Chiude la sessione dopo aver ottenuto i dati dal database
        db_session.close()

        # Restituisce la lista dei posti dell'aula
        return posti
