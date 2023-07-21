from typing import Dict, Type

from abstract.model import Model
from database import Session
from database import Libro as DbLibro


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

    def get(self, n: int) -> list[Type[DbLibro]]:
        db_session = Session()
        libri = db_session.query(DbLibro).limit(n).all()
        return libri

