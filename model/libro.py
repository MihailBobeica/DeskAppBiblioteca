from sqlalchemy import or_, and_

from abstract.model import Model
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from database import Session
from database import Utente as DbUtente
from utils.ui import RESULTS_LIMIT


class Libro(Model):
    def inserisci(self, dati: dict[str, str]):
        db_session = Session()
        libro = DbLibro(titolo=dati["titolo"],
                        autori=dati["autori"],
                        immagine=dati["immagine"],
                        editore=dati["editore"],
                        isbn=dati["isbn"],
                        anno_edizione=dati["anno_edizione"],
                        anno_pubblicazione=dati["anno_pubblicazione"],
                        disponibili=dati["disponibili"],
                        dati=dati["dati"])

        db_session.add(libro)
        db_session.commit()
        db_session.close()

    def inserisci2(self, dati: dict[str, str]):
        db_session = Session()
        libro = DbLibro(titolo=dati["titolo"],
                        autori=dati["autori"],
                        immagine=dati["immagine"],
                        editore=dati["editore"],
                        isbn=dati["isbn"],
                        anno_edizione=dati["anno_edizione"],
                        anno_pubblicazione=dati["anno_pubblicazione"],
                        disponibili=dati["disponibili"],
                        dati=dati["dati"])
        res = Libro.by_isbn(self, dati["isbn"])
        if res:
            res.disponibili += int(dati["disponibili"])
            db_session.merge(res)
            db_session.commit()
            db_session.close()
        else:
            db_session.add(libro)
            db_session.commit()
            db_session.close()

    def __init__(self):
        super().__init__()

    def get(self, n: int = RESULTS_LIMIT) -> list[DbLibro]:
        db_session = Session()
        libri = db_session.query(DbLibro).limit(n).all()
        db_session.close()
        return libri

    def get_prenotati(self, utente: DbUtente) -> list[DbLibro]:
        db_session = Session()
        libri_prenotati = db_session.query(DbLibro).join(DbPrenotazioneLibro).filter(
            DbPrenotazioneLibro.utente_id == utente.id).all()
        db_session.close()
        return libri_prenotati

    def search(self, text) -> list[DbLibro]:
        db_session = Session()
        libri = db_session.query(DbLibro).filter(or_(DbLibro.titolo.ilike(f"%{text}%"),
                                                     DbLibro.autori.ilike(f"%{text}%"))).limit(RESULTS_LIMIT).all()
        db_session.close()
        return libri

    def search_prenotati(self, utente: DbUtente, text: str) -> list[DbLibro]:
        db_session = Session()
        libri_prenotati = db_session.query(DbLibro).join(DbPrenotazioneLibro).filter(
            and_(DbPrenotazioneLibro.utente_id == utente.id,
                 or_(DbLibro.titolo.ilike(f"%{text}%"),
                     DbLibro.autori.ilike(f"%{text}%")))).all()
        db_session.close()
        return libri_prenotati

    def by_isbn(self, isbn):
        db_session = Session()
        libro = db_session.query(DbLibro).filter_by(isbn=isbn).first()
        db_session.close()
        return libro

    def elimina(self, libro: DbLibro):
        db_session = Session()
        db_session.delete(libro)
        db_session.commit()
        db_session.close()

    def modifica(self, dati: dict[str, str], old_isbn):
        db_session = Session()
        libro = Libro.by_isbn(self, old_isbn)
        libro.titolo = dati['titolo']
        libro.autori = dati['autori']
        libro.editore = dati['editore']
        libro.anno_edizione = dati['anno_edizione']
        libro.anno_pubblicazione = dati['anno_pubblicazione']
        libro.disponibili = dati['disponibili']
        libro.dati = dati['dati']
        db_session.merge(libro)
        db_session.commit()
        db_session.close()
