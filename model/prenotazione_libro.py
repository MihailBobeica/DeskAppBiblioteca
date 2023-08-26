from datetime import datetime, timedelta

from sqlalchemy import and_, or_

from abstract.model import Model
from database import Libro as DbLibro, Utente as DbUtente
from database import PrenotazioneLibro as DbPrenotazioneLibro
from database import Session
from utils.auth import auth
from utils.backend import DURATA_PRENOTAZIONE, get_codice, MAX_PRENOTAZIONI


class PrenotazioneLibro(Model):
    def __init__(self):
        super().__init__()

    def query_prenotazioni_valide(self, utente: DbUtente):
        db_session = Session()
        query = db_session.query(DbPrenotazioneLibro).filter(
            and_(DbPrenotazioneLibro.utente_id == utente.id,
                 DbPrenotazioneLibro.data_cancellazione == None,
                 DbPrenotazioneLibro.data_scadenza > datetime.now())
        )
        db_session.close()
        return query

    def valide(self, utente: DbUtente) -> list[DbPrenotazioneLibro]:
        db_session = Session()
        query_prenotazioni_valide = self.query_prenotazioni_valide(utente=utente)
        prenotazioni_valide: list[DbPrenotazioneLibro] = query_prenotazioni_valide.all()
        db_session.close()
        return prenotazioni_valide

    def ricerca_valide(self, utente: DbUtente, text: str) -> list[DbPrenotazioneLibro]:
        db_session = Session()
        query_prenotazioni_valide = self.query_prenotazioni_valide(utente=utente)
        query_ricerca_prenotazioni_valide = query_prenotazioni_valide.join(DbLibro).filter(
            or_(DbLibro.titolo.ilike(f"%{text}%"),
                DbLibro.autori.ilike(f"%{text}%"))
        )
        prenotazioni_valide: list[DbPrenotazioneLibro] = query_ricerca_prenotazioni_valide.all()
        db_session.close()
        return prenotazioni_valide

    def raggiunto_limite(self, utente: DbUtente) -> bool:
        db_session = Session()
        query_prenotazioni_valide = self.query_prenotazioni_valide(utente=utente)
        numero_prenotazioni_valide = query_prenotazioni_valide.count()
        db_session.close()
        return numero_prenotazioni_valide >= MAX_PRENOTAZIONI

    def gia_effettuata(self, utente: DbUtente, libro: DbLibro) -> bool:
        db_session = Session()
        query_prenotazioni_valide = self.query_prenotazioni_valide(utente=utente)
        query_prenotazione_effettuata = query_prenotazioni_valide.filter(
            DbPrenotazioneLibro.libro_id == libro.id
        )
        prenotazione_effettuata = query_prenotazione_effettuata.all()
        db_session.close()
        t = len(prenotazione_effettuata)
        assert t <= 1
        return t == 1

    def inserisci(self, libro: DbLibro) -> None:
        db_session = Session()

        libro_id = libro.id
        user_id = auth.user.id
        data_prenotazione = datetime.now()
        data_scadenza = data_prenotazione + timedelta(days=DURATA_PRENOTAZIONE)
        codice = get_codice()

        prenotazione_libro = DbPrenotazioneLibro(libro_id=libro_id,
                                                 utente_id=user_id,
                                                 data_prenotazione=data_prenotazione,
                                                 data_scadenza=data_scadenza,
                                                 codice=codice)
        db_session.add(prenotazione_libro)
        # aggiorna la disponibilità del libro
        libro.disponibili -= 1
        db_session.merge(libro)
        db_session.commit()
        db_session.close()

    def cancella(self, prenotazione: DbPrenotazioneLibro) -> None:
        db_session = Session()
        prenotazione.data_cancellazione = datetime.now()
        libro: DbLibro = prenotazione.libro
        libro.disponibili += 1
        db_session.merge(libro)
        db_session.merge(prenotazione)
        db_session.commit()
        db_session.close()

    def ricerca(self, input=None):
        db_session = Session()
        if input:
            pass
        else:
            prestiti = db_session.query(DbPrenotazioneLibro).filter_by(utente=auth.user.id).all()
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

    '''def by_utente(selfself, id):
        db_session = Session()
        prestiti = db_session.query(DbPrenotazioneLibro).filter_by(utente_id=id).filter().first()
        db_session.close()'''








