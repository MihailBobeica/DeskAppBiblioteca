from datetime import datetime

from sqlalchemy import or_

from abstract.model import Model
from database import Libro, Prestito
from database import PrenotazioneLibro
from database import Session
from utils.ui import RESULTS_LIMIT


class ModelLibri(Model):
    def inserisci(self,
                  titolo: str,
                  autori: str,
                  immagine: str,
                  editore: str,
                  isbn: str,
                  anno_edizione: datetime,
                  anno_pubblicazione: datetime,
                  disponibili: int,
                  dati: str):
        db_session = Session()
        libro = Libro(titolo=titolo,
                      autori=autori,
                      immagine=immagine,
                      editore=editore,
                      isbn=isbn,
                      anno_edizione=anno_edizione,
                      anno_pubblicazione=anno_pubblicazione,
                      disponibili=disponibili,
                      dati=dati)
        db_session.add(libro)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()

    def aggiungi(self, dati: dict[str, str]):
        db_session = Session()
        libro = Libro(titolo=dati["titolo"],
                      autori=dati["autori"],
                      immagine=dati["immagine"],
                      editore=dati["editore"],
                      isbn=dati["isbn"],
                      anno_edizione=dati["anno_edizione"],
                      anno_pubblicazione=dati["anno_pubblicazione"],
                      disponibili=dati["disponibili"],
                      dati=dati["dati"])
        res = ModelLibri.by_isbn(self, dati["isbn"])
        if res:
            res.disponibili += int(dati["disponibili"])
            db_session.merge(res)
            db_session.commit()
            db_session.close()
        else:
            db_session.add(libro)
            db_session.commit()
            db_session.close()

    def by_prestito(self, id_prestito: int) -> Libro:
        db_session = Session()
        prestito: Prestito = db_session.query(Prestito).get(id_prestito)
        libro = prestito.libro
        db_session.close()
        return libro

    def get(self, n: int = RESULTS_LIMIT) -> list[Libro]:
        db_session = Session()
        libri = db_session.query(Libro).limit(n).all()
        db_session.close()
        return libri

    def by_prenotazione(self, prenotazione: PrenotazioneLibro) -> Libro:
        db_session = Session()
        libro = prenotazione.libro
        db_session.close()
        return libro

    def search(self, text) -> list[Libro]:
        db_session = Session()
        libri = db_session.query(Libro).filter(or_(Libro.titolo.ilike(f"%{text}%"),
                                                   Libro.autori.ilike(f"%{text}%"))).limit(RESULTS_LIMIT).all()
        db_session.close()
        return libri

    def by_isbn(self, isbn):
        db_session = Session()
        libro = db_session.query(Libro).filter_by(isbn=isbn).first()
        db_session.close()
        return libro

    def by_id(self, id):
        db_session = Session()
        libro = db_session.query(Libro).filter_by(id=id).first()
        db_session.close()
        return libro

    def elimina(self, libro: Libro):
        db_session = Session()
        db_session.delete(libro)
        db_session.commit()
        db_session.close()

    def modifica(self, dati: dict[str, str], old_isbn):
        db_session = Session()
        libro = ModelLibri.by_isbn(self, old_isbn)
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
