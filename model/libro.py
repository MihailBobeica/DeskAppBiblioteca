from typing import Dict, Type

from sqlalchemy import or_

from abstract.model import Model
from database import Session
from database import Libro as DbLibro
from utils import RESULTS_LIMIT


class Libro(Model):
    def inserisci(self, dati: Dict[str, str]):
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

    def inserisci2(self, dati: Dict[str, str]):
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
        res = Libro.by_isbn(self,dati["isbn"])
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

    def get(self, n: int = RESULTS_LIMIT) -> list[Type[DbLibro]]:
        db_session = Session()
        libri = db_session.query(DbLibro).limit(n).all()
        db_session.close()
        return libri

    def search(self, text) -> list[Type[DbLibro]]:
        db_session = Session()
        libri = db_session.query(DbLibro).filter(or_(DbLibro.titolo.ilike(f"%{text}%"),
                                                     DbLibro.autori.ilike(f"%{text}%"))).limit(RESULTS_LIMIT).all()
        db_session.close()
        return libri

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

    def modifica(self, dati: Dict[str, str], old_isbn):
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


