from datetime import datetime, timedelta
from datetime import datetime, timedelta

from sqlalchemy import or_, and_

from abstract.model import Model
from database import Libro as DbLibro
from database import Session, Prestito
from database import User as DbUtente
from model.sanzioni import ModelSanzioni
from utils.backend import get_codice, DURATA_PRESTITO, MAX_PRESTITI
# from view.component.view_errore import view_errore
from .libri import ModelLibri


class ModelPrestiti(Model):
    def inserisci(self,
                  data_inizio: datetime,
                  data_restituzione: datetime,
                  utente_id: int,
                  libro_id: int):
        db_session = Session()
        prestito = Prestito(data_inizio=data_inizio,
                            data_scadenza=data_inizio + timedelta(days=DURATA_PRESTITO),
                            data_restituzione=data_restituzione,
                            codice=get_codice(),
                            utente_id=utente_id,
                            libro_id=libro_id)
        db_session.add(prestito)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()

    def aggiungi(self, utente: DbUtente, libro: DbLibro):
        db_session = Session()
        adesso = datetime.now()
        prestito = Prestito(data_inizio=adesso,
                            data_scadenza=adesso + timedelta(DURATA_PRESTITO),
                            codice=get_codice(),
                            utente_id=utente.id,
                            libro_id=libro.id)
        db_session.add(prestito)
        db_session.commit()
        db_session.close()

    def get_utenti_con_prestiti(self, text) -> list[DbUtente]:
        db_session = Session()
        utenti_con_prestiti = db_session.query(DbUtente).join(Prestito).filter(
            and_(DbUtente.id == Prestito.utente_id,
                 Prestito.data_restituzione == None,
                 or_(
                     DbUtente.username.ilike(f"%{text}%"),
                     DbUtente.nome.ilike(f"%{text}%"),
                     DbUtente.cognome.ilike(f"%{text}%"),
                 ))
        ).limit(3).all()
        db_session.close()
        return utenti_con_prestiti

    def by_id(self, id_prestito: int) -> Prestito:
        db_session = Session()
        prestito = db_session.query(Prestito).get(id_prestito)
        db_session.close()
        return prestito

    def is_scaduto(self, prestito: Prestito):
        return prestito.data_scadenza < datetime.now()

    def restituzione(self, prestito: Prestito):
        db_session = Session()

        prestito: Prestito = db_session.query(Prestito).get(prestito.id)
        prestito.data_restituzione = datetime.now()

        libro = prestito.libro
        libro.disponibili += 1

        db_session.merge(prestito)
        db_session.merge(libro)

        db_session.commit()
        db_session.close()

    def passati(self, id_utente: int) -> list[Prestito]:
        db_session = Session()
        prestiti = db_session.query(Prestito).filter(
            and_(Prestito.utente_id == id_utente,
                 Prestito.data_restituzione != None)
        ).order_by(Prestito.data_inizio.desc()).all()
        db_session.close()
        return prestiti

    def get_libro(self, prestito: Prestito) -> DbLibro:
        db_session = Session()
        prestito: Prestito = db_session.query(Prestito).get(prestito.id)
        libro = prestito.libro
        db_session.close()
        return libro

    def validi_by_utente(self, utente: DbUtente) -> list[Prestito]:
        db_session = Session()
        prestiti_non_restituiti = db_session.query(Prestito).filter(
            and_(Prestito.utente_id == utente.id,
                 Prestito.data_restituzione == None)
        ).all()
        db_session.close()
        return prestiti_non_restituiti

    def validi_by_utente_and_text(self, utente: DbUtente, text: str) -> list[Prestito]:
        db_session = Session()
        prestiti_non_restituiti = db_session.query(Prestito).join(DbLibro).filter(
            and_(Prestito.utente_id == utente.id,
                 Prestito.data_restituzione == None,
                 or_(DbLibro.titolo.ilike(f"%{text}%"),
                     DbLibro.autori.ilike(f"%{text}%")))
        ).all()
        db_session.close()
        return prestiti_non_restituiti

    def da_restituire(self, id):
        db_session = Session()
        prestiti = db_session.query(Prestito).filter(and_(Prestito.utente_id == id),
                                                     (Prestito.data_restituzione == None)).all()
        # print(prestiti)
        db_session.close()
        return prestiti

    def scaduti(self, utente: DbUtente):
        db_session = Session()
        prestiti_scaduti = db_session.query(Prestito).filter(
            and_(Prestito.utente_id == utente.id,
                 Prestito.data_scadenza > datetime.now())
        ).all()
        db_session.close()
        return prestiti_scaduti

    def has_max(self, utente: DbUtente) -> bool:
        db_session = Session()
        numero_prestiti = db_session.query(Prestito).filter(
            and_(Prestito.utente_id == utente.id,
                 Prestito.data_restituzione == None)
        ).count()
        return numero_prestiti > MAX_PRESTITI
