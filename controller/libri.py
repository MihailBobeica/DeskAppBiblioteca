from datetime import datetime
from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller
from model import ModelLibri
from utils.strings import *
from view.admin.aggiungi_modifica_libro import AggiungiModificaLibroView
from view.admin.gestione_libri import GestioneLibriView


class ControllerLibri(Controller):
    def __init__(self,
                 model_libri: ModelLibri):
        self.model_libri = model_libri
        super().__init__()

    def aggiungi_libro(self,
                       titolo: str,
                       autori: str,
                       editore: str,
                       isbn: str,
                       anno_edizione: datetime,
                       anno_pubblicazione: datetime,
                       disponibili: int,
                       dati: str,
                       copertina: str):
        self.model_libri.aggiungi(titolo=titolo,
                                  autori=autori,
                                  editore=editore,
                                  isbn=isbn,
                                  anno_edizione=anno_edizione,
                                  anno_pubblicazione=anno_pubblicazione,
                                  disponibili=disponibili,
                                  dati=dati,
                                  copertina=copertina)
        self.redirect(GestioneLibriView())

    def modifica_libro(self,
                       id_libro: Optional[int],
                       titolo: str,
                       autori: str,
                       editore: str,
                       isbn: str,
                       anno_edizione: datetime,
                       anno_pubblicazione: datetime,
                       disponibili: int,
                       dati: str,
                       copertina: str):
        self.model_libri.modifica(id_libro=id_libro,
                                  titolo=titolo,
                                  autori=autori,
                                  editore=editore,
                                  isbn=isbn,
                                  anno_edizione=anno_edizione,
                                  anno_pubblicazione=anno_pubblicazione,
                                  disponibili=disponibili,
                                  dati=dati,
                                  copertina=copertina)
        self.redirect(GestioneLibriView())

    def _fill_table_gestione_libri(self, view: GestioneLibriView, text: str):
        libri = self.model_libri.by_text(text)
        for libro in libri:
            view.add_row_table(id_libro=libro.id,
                               titolo=libro.titolo,
                               autori=libro.autori,
                               isbn=libro.isbn)

    def modifica_libro(self, id_libro: int):
        libro = self.model_libri.by_id(id_libro)
        self.redirect(AggiungiModificaLibroView(metodo="modifica", libro=libro))

    def elimina_libro(self, id_libro: int, view: GestioneLibriView):
        response = self.confirm(title=CONFIRM_TITLE_ELIMINA_LIBRO,
                                message=CONFIRM_MESSAGE_ELIMINA_LIBRO)
        if response == QMessageBox.StandardButton.Yes:
            self.model_libri.elimina(id_libro)
            view.search(view.searchbar.text())
