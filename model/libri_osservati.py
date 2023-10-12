from sqlalchemy import or_, and_

from abstract import Model
from database import Libro, LibroOsservato, Utente
from database import Session
from utils.backend import MAX_OSSERVAZIONI


class ModelLibriOsservati(Model):
    def inserisci(self, dati: dict[str, str]):
        pass

    def __init__(self):
        super().__init__()

    def aggiungi(self, utente: Utente, libro: Libro):
        db_session = Session()

        osserva_libro = LibroOsservato(utente_id=utente.id,
                                       libro_id=libro.id)

        db_session.add(osserva_libro)
        db_session.commit()
        db_session.close()

    def rimuovi(self, utente: Utente, libro: Libro):
        db_session = Session()

        libro_osservato = db_session.query(LibroOsservato).filter(
            and_(LibroOsservato.utente_id == utente.id,
                 LibroOsservato.libro_id == libro.id)
        ).first()

        db_session.delete(libro_osservato)
        db_session.commit()
        db_session.close()

    def by_utente(self, utente: Utente) -> list[Libro]:
        db_session = Session()
        osservazioni_libri = db_session.query(LibroOsservato).filter_by(utente_id=utente.id).all()
        libri_osservati = [ol.libro for ol in osservazioni_libri]
        return libri_osservati

    def limite_raggiunto(self, utente: Utente) -> bool:
        db_session = Session()

        numero_libri_osservati = db_session.query(LibroOsservato).filter_by(utente_id=utente.id).count()

        db_session.close()
        return numero_libri_osservati > MAX_OSSERVAZIONI

    def by_text(self, utente: Utente, text: str) -> list[Libro]:
        db_session = Session()

        libri_osservati = db_session.query(Libro).join(LibroOsservato).filter(
            and_(LibroOsservato.utente_id == utente.id,
                 or_(Libro.titolo.ilike(f"%{text}%"),
                     Libro.autori.ilike(f"%{text}%")))
        ).all()

        return libri_osservati

    def gia_osservato(self, utente: Utente, libro: Libro) -> bool:
        db_session = Session()
        n = db_session.query(LibroOsservato).filter(
            and_(LibroOsservato.utente_id == utente.id,
                 LibroOsservato.libro_id == libro.id)
        ).count()
        db_session.close()
        return n >= 1
