from datetime import datetime, timedelta

from sqlalchemy import and_, or_

from abstract.model import Model
from database import Libro as DbLibro, User as DbUtente
from database import PrenotazioneLibro
from database import Session
from utils.auth import auth
from utils.backend import DURATA_PRENOTAZIONE, get_codice, MAX_PRENOTAZIONI


class ModelPrenotazioniLibri(Model):
    def inserisci(self,
                  data_prenotazione: datetime,
                  codice: str,
                  utente_id: int,
                  libro_id: int):
        db_session = Session()
        prenotazione_libro = PrenotazioneLibro(data_prenotazione=data_prenotazione,
                                               data_scadenza=data_prenotazione + timedelta(days=DURATA_PRENOTAZIONE),
                                               codice=codice,
                                               utente_id=utente_id,
                                               libro_id=libro_id)
        db_session.add(prenotazione_libro)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()

    def quasi_scadute(self, utente: DbUtente) -> list[PrenotazioneLibro]:
        db_session = Session()
        prenotazioni_valide = self._query_prenotazioni_valide(utente)
        one_day_later = datetime.now() + timedelta(days=1)
        prenotazioni_quasi_scadute = prenotazioni_valide.filter(
            PrenotazioneLibro.data_scadenza <= one_day_later
        ).all()
        db_session.close()
        return prenotazioni_quasi_scadute

    def _query_prenotazioni_valide(self, utente: DbUtente):
        db_session = Session()
        query = db_session.query(PrenotazioneLibro).filter(
            and_(PrenotazioneLibro.utente_id == utente.id,
                 PrenotazioneLibro.data_cancellazione == None,
                 PrenotazioneLibro.data_scadenza > datetime.now())
        )
        db_session.close()
        return query

    def by_id(self, id_prenotazione: int) -> PrenotazioneLibro:
        db_session = Session()
        prenotazione_libro = db_session.query(PrenotazioneLibro).get(id_prenotazione)
        db_session.close()
        return prenotazione_libro

    def get_utenti_con_prenotazioni(self, text):
        db_session = Session()
        utenti_con_prenotazioni = db_session.query(DbUtente).join(PrenotazioneLibro).filter(
            and_(DbUtente.id == PrenotazioneLibro.utente_id,
                 PrenotazioneLibro.data_cancellazione == None,
                 PrenotazioneLibro.data_scadenza > datetime.now(),
                 or_(
                     DbUtente.username.ilike(f"%{text}%"),
                     DbUtente.nome.ilike(f"%{text}%"),
                     DbUtente.cognome.ilike(f"%{text}%")
                 ))
        ).limit(3).all()
        db_session.close()
        return utenti_con_prenotazioni

    def valide_by_utente(self, utente: DbUtente) -> list[PrenotazioneLibro]:
        db_session = Session()
        query_prenotazioni_valide = self._query_prenotazioni_valide(utente=utente)
        prenotazioni_valide: list[PrenotazioneLibro] = query_prenotazioni_valide.all()
        db_session.close()
        return prenotazioni_valide

    def ricerca_valide(self, utente: DbUtente, text: str) -> list[PrenotazioneLibro]:
        db_session = Session()
        query_prenotazioni_valide = self._query_prenotazioni_valide(utente=utente)
        query_ricerca_prenotazioni_valide = query_prenotazioni_valide.join(DbLibro).filter(
            or_(DbLibro.titolo.ilike(f"%{text}%"),
                DbLibro.autori.ilike(f"%{text}%"))
        )
        prenotazioni_valide: list[PrenotazioneLibro] = query_ricerca_prenotazioni_valide.all()
        db_session.close()
        return prenotazioni_valide

    def limite_raggiunto(self, utente: DbUtente) -> bool:
        db_session = Session()
        query_prenotazioni_valide = self._query_prenotazioni_valide(utente=utente)
        numero_prenotazioni_valide = query_prenotazioni_valide.count()
        db_session.close()
        return numero_prenotazioni_valide >= MAX_PRENOTAZIONI

    def gia_prenotato(self, utente: DbUtente, libro: DbLibro) -> bool:
        db_session = Session()
        query_prenotazioni_valide = self._query_prenotazioni_valide(utente=utente)
        query_prenotazione_effettuata = query_prenotazioni_valide.filter(
            PrenotazioneLibro.libro_id == libro.id
        )
        prenotazione_effettuata = query_prenotazione_effettuata.all()
        db_session.close()
        t = len(prenotazione_effettuata)
        assert t <= 1
        return t == 1

    def aggiungi(self, utente: DbUtente, libro: DbLibro) -> None:
        db_session = Session()

        libro_id = libro.id
        user_id = utente.id
        data_prenotazione = datetime.now()
        data_scadenza = data_prenotazione + timedelta(days=DURATA_PRENOTAZIONE)
        codice = get_codice()

        prenotazione_libro = PrenotazioneLibro(libro_id=libro_id,
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

    def get_libro(self, prenotazione_libro: PrenotazioneLibro) -> DbLibro:
        db_session = Session()
        prenotazione_libro: PrenotazioneLibro = db_session.query(PrenotazioneLibro).get(prenotazione_libro.id)
        libro = prenotazione_libro.libro
        db_session.close()
        return libro

    def cancella(self, prenotazione: PrenotazioneLibro) -> None:
        db_session = Session()
        prenotazione = db_session.query(PrenotazioneLibro).get(prenotazione.id)
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
            prestiti = db_session.query(PrenotazioneLibro).filter_by(utente=auth.user.id).all()
            db_session.close()
            return prestiti

    def sospensione(self):
        pass

    def libro_non_disponibile(self):
        pass

    def by_codice(self, codice):
        db_session = Session()
        prestiti = db_session.query(PrenotazioneLibro).filter_by(codice=codice).first()
        db_session.close()
        return prestiti

    '''def by_utente(selfself, id):
        db_session = Session()
        prestiti = db_session.query(DbPrenotazioneLibro).filter_by(utente_id=id).filter().first()
        db_session.close()'''

    def scadute(self, utente: DbUtente):
        db_session = Session()
        prenotazioni_scadute = db_session.query(PrenotazioneLibro).filter(
            and_(PrenotazioneLibro.utente_id == utente.id,
                 PrenotazioneLibro.data_cancellazione == None,
                 PrenotazioneLibro.data_scadenza < datetime.now())
        ).all()
        db_session.close()
        return prenotazioni_scadute
