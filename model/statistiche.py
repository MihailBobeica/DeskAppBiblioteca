from sqlalchemy import and_, or_, func

from abstract.model import Model
from database import Prestito as db_Prestito,Session, Sanzione as db_Sanzioni,Libro as db_Libro

class Statistiche(Model):
    def __init__(self):
        super().__init__()

    def num_prestiti(self):
        db_session = Session()
        num = db_session.query(db_Prestito).count()
        db_session.close()
        return num

    def num_utenti(self):
        db_session = Session()
        num = db_session.query(db_Prestito.utente_id).distinct().count()
        db_session.close()
        return num

    def libri_piu_prestati(self):
        db_session = Session()
        most_borrowed_books = db_session.query(
            db_Prestito.libro_id,
            func.count(db_Prestito.libro_id).label('total_borrowed')
        ).group_by(db_Prestito.libro_id).order_by(func.count(db_Prestito.libro_id).desc())
        db_session.close()
        return most_borrowed_books

    def num_sospensioni(self):
        db_session = Session()
        num = db_session.query(db_Sanzioni).count()
        db_session.close()
        return num

    def num_libri(self):
        db_session = Session()
        num = db_session.query(db_Libro).count()
        db_session.close()
        return num