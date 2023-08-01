from typing import Dict, Type, List

from abstract.model import Model
from database import PrenotazioneAula as DbPrenotazioneAula
from database import Session
from utils.backend import POSTI_PER_AULA



class prenotazione_aula(Model):
    def inserisci(self, dati: Dict[str, str]):
        db_session = Session()
        prenotazione = DbPrenotazioneAula(id=dati["id"],
                                          codice_aula=dati["codice_aula"],
                                          data_prenotazione=dati["data_prenotazione"],
                                          codice_utente=dati["codice_utente"],
                                          ora_inizio=dati["ora_inizio"],
                                          ora_fine=dati["ora_fine"],
                                          ora_attivazione=dati["ora_attivazione"],
                                          durata=dati["durata"])

        db_session.add(prenotazione)
        db_session.commit()
        db_session.close()

    def get(self, n: int = POSTI_PER_AULA) -> list[Type[DbPrenotazioneAula]]:
        db_session = Session()
        prenotazioni = db_session.query(DbPrenotazioneAula).limit(n).all()
        db_session.close()
        return prenotazioni

    def by_id(self, prenotazione_id):
        db_session = Session()
        prenotazione = db_session.query(DbPrenotazioneAula).filter_by(id=prenotazione_id).first()
        db_session.close()
        return prenotazione

    def by_utente(self, utente_id: str) -> List[Type[DbPrenotazioneAula]]:
        db_session = Session()
        prenotazioni_utente = db_session.query(DbPrenotazioneAula).filter_by(utente_id=utente_id).all()
        db_session.close()
        return prenotazioni_utente

    def __init__(self):
        super().__init__()
