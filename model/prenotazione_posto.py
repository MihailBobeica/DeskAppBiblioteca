from typing import Dict, Type, List

from abstract.model import Model
from database import Session
from database import PrenotazionePosto as DbPrenotazionePosto
from utils import POSTI

class prenotazione_posto(Model):
    def inserisci(self, dati: Dict[str, str]):
        db_session = Session()
        prenotazione = DbPrenotazionePosto(id=dati["id"],
                                           posto=dati["posto"],
                                           data=dati["data"],
                                           utente_id=dati["utente_id"],
                                           ora_inizio=dati["ora_inizio"],
                                           ora_fine=dati["ora_fine"],
                                           ora_attivazione=dati["ora_attivazione"],
                                           durata=dati["durata"])

        db_session.add(prenotazione)
        db_session.commit()
        db_session.close()

    def get(self, n: int = POSTI) -> list[Type[DbPrenotazionePosto]]:
        db_session = Session()
        prenotazioni = db_session.query(DbPrenotazionePosto).limit(n).all()
        db_session.close()
        return prenotazioni

    def by_id(self, prenotazione_id):
        db_session = Session()
        prenotazione = db_session.query(DbPrenotazionePosto).filter_by(id=prenotazione_id).first()
        db_session.close()
        return prenotazione

    def by_utente(self, utente_id: str) -> List[Type[DbPrenotazionePosto]]:
        db_session = Session()
        prenotazioni_utente = db_session.query(DbPrenotazionePosto).filter_by(utente_id=utente_id).all()
        db_session.close()
        return prenotazioni_utente

    def __init__(self):
        super().__init__()
