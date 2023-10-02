from sqlalchemy import or_, and_

from abstract import Model
from database import Libro as DbLibro
from database import LibroOsservato as DbOsservaLibro
from database import Session
from database import User as DbUtente
from utils.backend import MAX_OSSERVAZIONI


class ModelLibriOsservati(Model):
    def inserisci(self, dati: dict[str, str]):
        pass

    def __init__(self):
        super().__init__()

    def by_utente(self, utente: DbUtente) -> list[DbLibro]:
        db_session = Session()
        osservazioni_libri = db_session.query(DbOsservaLibro).filter_by(utente_id=utente.id).all()
        libri_osservati = [ol.libro for ol in osservazioni_libri]
        return libri_osservati

    def rimuovi(self, utente: DbUtente, libro: DbLibro):
        db_session = Session()

        libro_osservato = db_session.query(DbOsservaLibro).filter(
            and_(DbOsservaLibro.utente_id == utente.id,
                 DbOsservaLibro.libro_id == libro.id)
        ).first()

        db_session.delete(libro_osservato)
        db_session.commit()
        db_session.close()

    def limite_raggiunto(self, utente: DbUtente) -> bool:
        db_session = Session()

        numero_libri_osservati = db_session.query(DbOsservaLibro).filter_by(utente_id=utente.id).count()

        db_session.close()
        return numero_libri_osservati > MAX_OSSERVAZIONI

    def aggiungi(self, utente: DbUtente, libro: DbLibro):
        db_session = Session()

        osserva_libro = DbOsservaLibro(utente_id=utente.id,
                                       libro_id=libro.id)

        db_session.add(osserva_libro)
        db_session.commit()
        db_session.close()

    def search_libri_osservati(self, utente: DbUtente, text: str):  ######
        db_session = Session()

        libri_osservati = db_session.query(DbLibro).join(DbOsservaLibro).filter(
            and_(DbOsservaLibro.utente_id == utente.id,
                 or_(DbLibro.titolo.ilike(f"%{text}%"),
                     DbLibro.autori.ilike(f"%{text}%")))
        ).all()

        return libri_osservati

    def by_libro(self, utente: DbUtente, libro: DbLibro):
        db_session = Session()

        libro_osservato = db_session.query(DbOsservaLibro).filter(
            and_(DbOsservaLibro.utente_id == utente.id,
                 DbOsservaLibro.libro_id == libro.id)
        )

        db_session.close()

        return libro_osservato

    def gia_osservato(self, utente: DbUtente, libro: DbLibro):
        db_session = Session()
        n = self.by_libro(utente, libro).count()
        db_session.close()
        return n >= 1
