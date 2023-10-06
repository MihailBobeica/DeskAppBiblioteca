import unittest
from datetime import datetime

from model import ModelLibri


class TestModelLibri(unittest.TestCase):
    def setUp(self) -> None:
        self.model_libri = ModelLibri()

    def test_aggiungi_libro(self):
        titolo = "Titolo"
        autori = "Autori"
        editore = "Editore"
        isbn = "ISBN_test_aggiungi_libro"
        anno_edizione = datetime(year=2000, month=1, day=1)
        anno_pubblicazione = datetime(year=2000, month=1, day=1)
        disponibili = 2
        dati = "12 pagine"
        copertina = "Immagine.jpg"

        self.model_libri.aggiungi(titolo=titolo,
                                  autori=autori,
                                  editore=editore,
                                  isbn=isbn,
                                  anno_edizione=anno_edizione,
                                  anno_pubblicazione=anno_pubblicazione,
                                  disponibili=disponibili,
                                  dati=dati,
                                  copertina=copertina)

        libro = self.model_libri.by_isbn(isbn)

        self.assertEqual(titolo, libro.titolo)
        self.assertEqual(autori, libro.autori)
        self.assertEqual(editore, libro.editore)
        self.assertEqual(isbn, libro.isbn)
        self.assertEqual(anno_edizione.year, libro.anno_edizione.year)
        self.assertEqual(anno_pubblicazione.year, libro.anno_pubblicazione.year)
        self.assertEqual(disponibili, libro.disponibili)
        self.assertEqual(dati, libro.dati)
        self.assertEqual(copertina, libro.immagine)

    def test_somma_disponibili(self):
        titolo = "Titolo"
        autori = "Autori"
        editore = "Editore"
        isbn = "ISBN_test_somma_disponibili"
        anno_edizione = datetime(year=2000, month=1, day=1)
        anno_pubblicazione = datetime(year=2000, month=1, day=1)
        disponibili_1 = 4
        disponibili_2 = 3
        dati = "12 pagine"
        copertina = "Immagine.jpg"

        self.model_libri.aggiungi(titolo=titolo,
                                  autori=autori,
                                  editore=editore,
                                  isbn=isbn,
                                  anno_edizione=anno_edizione,
                                  anno_pubblicazione=anno_pubblicazione,
                                  disponibili=disponibili_1,
                                  dati=dati,
                                  copertina=copertina)
        self.model_libri.aggiungi(titolo=titolo,
                                  autori=autori,
                                  editore=editore,
                                  isbn=isbn,
                                  anno_edizione=anno_edizione,
                                  anno_pubblicazione=anno_pubblicazione,
                                  disponibili=disponibili_2,
                                  dati=dati,
                                  copertina=copertina)

        libro = self.model_libri.by_isbn(isbn)

        totale_disponibili = disponibili_1 + disponibili_2

        self.assertEqual(totale_disponibili, libro.disponibili)

    def test_elimina_libro(self):
        titolo = "Titolo"
        autori = "Autori"
        editore = "Editore"
        isbn = "ISBN_test_elimina_libro"
        anno_edizione = datetime(year=2000, month=1, day=1)
        anno_pubblicazione = datetime(year=2000, month=1, day=1)
        disponibili = 2
        dati = "12 pagine"
        copertina = "Immagine.jpg"

        self.model_libri.aggiungi(titolo=titolo,
                                  autori=autori,
                                  editore=editore,
                                  isbn=isbn,
                                  anno_edizione=anno_edizione,
                                  anno_pubblicazione=anno_pubblicazione,
                                  disponibili=disponibili,
                                  dati=dati,
                                  copertina=copertina)

        libro_aggiunto = self.model_libri.by_isbn(isbn)
        self.assertIsNotNone(libro_aggiunto)
        self.model_libri.elimina(libro_aggiunto.id)
        libro_eliminato = self.model_libri.by_isbn(isbn)
        self.assertIsNone(libro_eliminato)

    def test_modifica_libro(self):
        titolo = "Titolo"
        autori = "Autori"
        editore = "Editore"
        isbn = "ISBN_test_modifica_libro"
        anno_edizione = datetime(year=2000, month=1, day=1)
        anno_pubblicazione = datetime(year=2000, month=1, day=1)
        disponibili = 2
        dati = "12 pagine"
        copertina = "Immagine.jpg"

        self.model_libri.aggiungi(titolo=titolo,
                                  autori=autori,
                                  editore=editore,
                                  isbn=isbn,
                                  anno_edizione=anno_edizione,
                                  anno_pubblicazione=anno_pubblicazione,
                                  disponibili=disponibili,
                                  dati=dati,
                                  copertina=copertina)

        libro = self.model_libri.by_isbn(isbn)
        id_libro = libro.id

        titolo_modificato = "Titolo modificato"
        autori_modificato = "Autori modificato"
        editore_modificato = "Editore modificato"
        isbn_modificato = "ISBN_test_modifica_libro modificato"
        anno_edizione_modificato = datetime(year=2003, month=1, day=1)
        anno_pubblicazione_modificato = datetime(year=2003, month=1, day=1)
        disponibili_modificato = 4
        dati_modificato = "12 pagine e mezzo"
        copertina_modificato = "Immagine modificato.jpg"

        self.model_libri.modifica(id_libro=id_libro,
                                  titolo=titolo_modificato,
                                  autori=autori_modificato,
                                  editore=editore_modificato,
                                  isbn=isbn_modificato,
                                  anno_edizione=anno_edizione_modificato,
                                  anno_pubblicazione=anno_pubblicazione_modificato,
                                  disponibili=disponibili_modificato,
                                  dati=dati_modificato,
                                  copertina=copertina_modificato)

        libro_modificato = self.model_libri.by_id(id_libro)

        self.assertEqual(titolo_modificato, libro_modificato.titolo)
        self.assertEqual(autori_modificato, libro_modificato.autori)
        self.assertEqual(editore_modificato, libro_modificato.editore)
        self.assertEqual(isbn_modificato, libro_modificato.isbn)
        self.assertEqual(anno_edizione_modificato.year, libro_modificato.anno_edizione.year)
        self.assertEqual(anno_pubblicazione_modificato.year, libro_modificato.anno_pubblicazione.year)
        self.assertEqual(disponibili_modificato, libro_modificato.disponibili)
        self.assertEqual(dati_modificato, libro_modificato.dati)
        self.assertEqual(copertina_modificato, libro_modificato.immagine)


if __name__ == '__main__':
    unittest.main()
