from datetime import datetime

from sqlalchemy import or_

from abstract import Model
from database import Libro, Prestito, PrenotazioneLibro
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

    def aggiungi(self,
                 titolo: str,
                 autori: str,
                 editore: str,
                 isbn: str,
                 anno_edizione: datetime,
                 anno_pubblicazione: datetime,
                 disponibili: int,
                 dati: str,
                 copertina: str):
        db_session = Session()
        libro = Libro(titolo=titolo,
                      autori=autori,
                      immagine=copertina,
                      editore=editore,
                      isbn=isbn,
                      anno_edizione=anno_edizione,
                      anno_pubblicazione=anno_pubblicazione,
                      disponibili=disponibili,
                      dati=dati)
        libro_presente = self.by_isbn(isbn)
        if libro_presente:
            libro_presente.disponibili += disponibili
            db_session.merge(libro_presente)
        else:
            db_session.add(libro)
        db_session.commit()
        db_session.close()

    def modifica(self,
                 id_libro: int,
                 titolo: str,
                 autori: str,
                 editore: str,
                 isbn: str,
                 anno_edizione: datetime,
                 anno_pubblicazione: datetime,
                 disponibili: int,
                 dati: str,
                 copertina: str):
        db_session = Session()
        libro: Libro = db_session.get(Libro, id_libro)
        libro.titolo = titolo
        libro.autori = autori
        libro.editore = editore
        libro.isbn = isbn
        libro.anno_edizione = anno_edizione
        libro.anno_pubblicazione = anno_pubblicazione
        libro.disponibili = disponibili
        libro.dati = dati
        libro.immagine = copertina
        db_session.merge(libro)
        db_session.commit()
        db_session.close()

    def elimina(self, id_libro: int):
        db_session = Session()
        libro = db_session.get(Libro, id_libro)
        db_session.delete(libro)
        db_session.commit()
        db_session.close()

    def by_id_prestito(self, id_prestito: int) -> Libro:
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
        prenotazione = db_session.query(PrenotazioneLibro).get(prenotazione.id)
        libro = prenotazione.libro
        db_session.close()
        return libro

    def by_text(self, text: str, n: int = RESULTS_LIMIT) -> list[Libro]:
        db_session = Session()
        libri = db_session.query(Libro).filter(or_(Libro.titolo.ilike(f"%{text}%"),
                                                   Libro.autori.ilike(f"%{text}%"))).limit(n).all()
        db_session.close()
        return libri

    def by_isbn(self, isbn: str) -> Libro:
        db_session = Session()
        libro = db_session.query(Libro).filter_by(isbn=isbn).first()
        db_session.close()
        return libro

    def by_id(self, id_libro: int) -> Libro:
        db_session = Session()
        libro = db_session.get(Libro, id_libro)
        db_session.close()
        return libro
