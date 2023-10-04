from sqlalchemy import func

from abstract.model import Model
from database import Prestito
from database import Session
from database import Sanzione
from database import Libro


class ModelStatistiche(Model):
    def inserisci(self, **kwargs):
        pass

    def __init__(self):
        super().__init__()

    def totale_prestiti(self) -> int:
        db_session = Session()
        totale_prestiti = db_session.query(Prestito).count()
        db_session.close()
        return totale_prestiti

    def totale_utenti(self) -> int:
        db_session = Session()
        totale_utenti = db_session.query(Prestito.utente_id).distinct().count()
        db_session.close()
        return totale_utenti

    def titoli_piu_prestati(self):
        db_session = Session()
        # prestiti_libri: list[tuple[int(id_libro), int(numero_prestiti)]]
        prestiti_libri = db_session.query(
            Prestito.libro_id,
            func.count(Prestito.libro_id).label('total_borrowed')
        ).group_by(Prestito.libro_id).order_by(func.count(Prestito.libro_id).desc()).all()
        titoli_libri = []
        for id_libro, numero_prestiti in prestiti_libri[:3]:
            libro: Libro = db_session.query(Libro).get(id_libro)
            titoli_libri.append(libro.titolo)
        db_session.close()
        return titoli_libri

    def totale_sospensioni(self):
        db_session = Session()
        totale_sospensioni = db_session.query(Sanzione).count()
        db_session.close()
        return totale_sospensioni

    def totale_libri(self):
        db_session = Session()
        totale_libri = db_session.query(Libro).count()
        db_session.close()
        return totale_libri
