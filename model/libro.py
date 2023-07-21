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


