from typing import Dict

from sqlalchemy import or_

from abstract.model import Model
from database import Session, PrenotazioneLibro, Utente
from database import User as DbUtente


class ModelUtenti(Model):
    def __init__(self):
        super().__init__()

    def by_username(self, username):
        db_session = Session()
        utente = db_session.query(DbUtente).filter_by(username=username).first()
        db_session.close()
        return utente

    def by_prenotazione(self, prenotazione: PrenotazioneLibro) -> DbUtente:
        db_session = Session()
        prenotazione = db_session.query(PrenotazioneLibro).get(prenotazione.id)
        utente = prenotazione.utente
        db_session.close()
        return utente

    def inserisci(self, dati: Dict[str, str]):
        db_session = Session()
        utente = DbUtente(nome=dati["nome"],
                          cognome=dati["cognome"],
                          ruolo=dati["ruolo"],
                          username=dati["username"],
                          password=dati["password"])
        if ModelUtenti.by_username(self, utente.username):
            from view.component.view_errore import view_errore
            view_errore.create_layout(self, "Errore", "L'operatore è già presente nel sistema")
        else:
            db_session.add(utente)
            db_session.commit()
            db_session.close()

    def all(self) -> list[DbUtente]:
        db_session = Session()
        utenti = db_session.query(DbUtente).all()
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
