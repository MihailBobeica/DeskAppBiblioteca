from typing import Dict

from abstract.model import Model
from database import Session
from database import Libro as DbLibro


class Libro(Model):
    def inserisci(self, dati: Dict[str, str]):
        db_session = Session()
        libro = DbLibro(titolo=dati["titolo"],
                        autore=dati["autore"],
                        isbn=dati["isbn"],
                        immagine=dati["immagine"])
        db_session.add(libro)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()
