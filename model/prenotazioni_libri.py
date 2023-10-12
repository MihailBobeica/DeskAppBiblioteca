from datetime import datetime, timedelta

from sqlalchemy import and_, or_

from abstract import Model
from database import Libro, Utente, PrenotazioneLibro
from database import Session
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

    def aggiungi(self, utente: Utente, libro: Libro) -> None:
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

    def cancella(self, prenotazione: PrenotazioneLibro) -> None:
        db_session = Session()
        prenotazione = db_session.query(PrenotazioneLibro).get(prenotazione.id)
        prenotazione.data_cancellazione = datetime.now()
        libro: Libro = prenotazione.libro
        libro.disponibili += 1
        db_session.merge(libro)
        db_session.merge(prenotazione)
        db_session.commit()
        db_session.close()

    def by_id(self, id_prenotazione: int) -> PrenotazioneLibro:
        db_session = Session()
        prenotazione_libro = db_session.query(PrenotazioneLibro).get(id_prenotazione)
        db_session.close()
        return prenotazione_libro

    def get_libro(self, prenotazione_libro: PrenotazioneLibro) -> Libro:
        db_session = Session()
        prenotazione_libro: PrenotazioneLibro = db_session.query(PrenotazioneLibro).get(prenotazione_libro.id)
        libro = prenotazione_libro.libro
        db_session.close()
        return libro

    def get_utenti_con_prenotazioni(self, text: str) -> list[Utente]:
        db_session = Session()
        utenti_con_prenotazioni = db_session.query(Utente).join(PrenotazioneLibro).filter(
            and_(Utente.id == PrenotazioneLibro.utente_id,
                 PrenotazioneLibro.data_cancellazione == None,
                 PrenotazioneLibro.data_scadenza > datetime.now(),
                 or_(
                     Utente.username.ilike(f"%{text}%"),
                     Utente.nome.ilike(f"%{text}%"),
                     Utente.cognome.ilike(f"%{text}%")
                 ))
        ).limit(3).all()
        db_session.close()
        return utenti_con_prenotazioni

    def valide_by_utente(self, utente: Utente) -> list[PrenotazioneLibro]:
        db_session = Session()
        query_prenotazioni_valide = self._query_prenotazioni_valide(utente=utente)
        prenotazioni_valide: list[PrenotazioneLibro] = query_prenotazioni_valide.all()
        db_session.close()
        return prenotazioni_valide

    def quasi_scadute(self, utente: Utente) -> list[PrenotazioneLibro]:
        db_session = Session()
        prenotazioni_valide = self._query_prenotazioni_valide(utente)
        one_day_later = datetime.now() + timedelta(days=1)
        prenotazioni_quasi_scadute = prenotazioni_valide.filter(
            PrenotazioneLibro.data_scadenza <= one_day_later
        ).all()
        db_session.close()
        return prenotazioni_quasi_scadute

    def ricerca_valide_by_text(self, utente: Utente, text: str) -> list[PrenotazioneLibro]:
        db_session = Session()
        query_prenotazioni_valide = self._query_prenotazioni_valide(utente=utente)
        query_ricerca_prenotazioni_valide = query_prenotazioni_valide.join(Libro).filter(
            or_(Libro.titolo.ilike(f"%{text}%"),
                Libro.autori.ilike(f"%{text}%"))
        )
        prenotazioni_valide: list[PrenotazioneLibro] = query_ricerca_prenotazioni_valide.all()
        db_session.close()
        return prenotazioni_valide

    def limite_raggiunto(self, utente: Utente) -> bool:
        db_session = Session()
        query_prenotazioni_valide = self._query_prenotazioni_valide(utente=utente)
        numero_prenotazioni_valide = query_prenotazioni_valide.count()
        db_session.close()
        return numero_prenotazioni_valide >= MAX_PRENOTAZIONI

    def gia_prenotato(self, utente: Utente, libro: Libro) -> bool:
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

    def _query_prenotazioni_valide(self, utente: Utente):
        db_session = Session()
        query = db_session.query(PrenotazioneLibro).filter(
            and_(PrenotazioneLibro.utente_id == utente.id,
                 PrenotazioneLibro.data_cancellazione == None,
                 PrenotazioneLibro.data_scadenza > datetime.now())
        )
        db_session.close()
        return query
