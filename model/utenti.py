from sqlalchemy import or_

from abstract import Model
from database import PrenotazioneLibro, Utente
from database import Session


class ModelUtenti(Model):
    def inserisci(self, **kwargs):
        pass

    def __init__(self):
        super().__init__()

    def by_username(self, username) -> Utente:
        db_session = Session()
        utente = db_session.query(Utente).filter_by(username=username).first()
        db_session.close()
        return utente

    def by_prenotazione(self, prenotazione: PrenotazioneLibro) -> Utente:
        db_session = Session()
        prenotazione = db_session.query(PrenotazioneLibro).get(prenotazione.id)
        utente = prenotazione.utente
        db_session.close()
        return utente

    def all(self) -> list[Utente]:
        db_session = Session()
        utenti = db_session.query(Utente).all()
        db_session.close()
        return utenti

    def by_text(self, text: str) -> list[Utente]:
        db_session = Session()
        utenti = db_session.query(Utente).filter(
            or_(Utente.username.ilike(f"%{text}%"),
                Utente.nome.ilike(f"%{text}%"),
                Utente.cognome.ilike(f"%{text}%"))
        ).all()
        db_session.close()
        return utenti
