from datetime import datetime, timedelta

from sqlalchemy import and_

from abstract.model import Model
from database import Libro as DbLibro, Utente as DbUtente
from database import PrenotazioneLibro as DbPrenotazioneLibro
from database import Session
from utils.auth import Auth
from utils.backend import DURATA_PRENOTAZIONE, get_codice, MAX_PRENOTAZIONI


class PrenotazioneLibro(Model):
    def __init__(self):
        super().__init__()

    def raggiunto_limite(self, utente: DbUtente) -> bool:
        db_session = Session()
        prenotazioni = db_session.query(DbPrenotazioneLibro).filter_by(utente=utente.id).count()
        db_session.close()
        return prenotazioni >= MAX_PRENOTAZIONI

    def gia_effettuata(self, utente: DbUtente, libro: DbLibro):
        db_session = Session()
        effettuata = db_session.query(DbPrenotazioneLibro).filter(
            and_(DbPrenotazioneLibro.utente == utente.id,
                 DbPrenotazioneLibro.libro == libro.id)).first()
        db_session.close()
        return effettuata is not None

    def inserisci(self, libro: DbLibro) -> None:
        db_session = Session()

        libro_id = libro.id
        user_id = Auth.user.id
        data_prenotazione = datetime.now()
        data_scadenza = data_prenotazione + timedelta(days=DURATA_PRENOTAZIONE)
        codice = get_codice()

        prenotazione_libro = DbPrenotazioneLibro(libro=libro_id,
                                                 utente=user_id,
                                                 data_prenotazione=data_prenotazione,
                                                 data_scadenza=data_scadenza,
                                                 codice=codice)
        db_session.add(prenotazione_libro)
        # aggiorna la disponibilità del libro
        libro.disponibili -= 1
        db_session.merge(libro)
        db_session.commit()
        db_session.close()

    def ricerca(self, input=None):
        db_session = Session()
        if input:
            pass
        else:
            prestiti = db_session.query(DbPrenotazioneLibro).filter_by(utente=Auth.user.username).all()
            db_session.close()
            return prestiti

    def sospensione(self):
        pass

    def libro_non_disponibile(self):
        pass

    def by_codice(self, codice):
        db_session = Session()
        prestiti = db_session.query(DbPrenotazioneLibro).filter_by(codice=codice).first()
        db_session.close()
        return prestiti
