from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from database import Libro as DbLibro
from model import Libro, PrenotazioneLibro
from utils.auth import Auth
from utils.strings import *
from view.component.catalogo import CatalogoComponent
from view.libri_prenotati import LibriPrenotatiView
from view.libro import LibroView


class CatalogoController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        self.message_search(message, data)
        self.message_visualizza_libro(message, data)
        self.message_prenota_libro(message, data)
        self.message_osserva_libro(message, data)

    def message_search(self, message: str, data: Optional[dict] = None):
        if message == "search":
            catalogo: CatalogoComponent = data["catalogo"]
            text = data["text"]
            model_libro: Libro = self.models["libri"]
            db_libri = catalogo.cerca_libri_strategy.search(model_libro, text)
            catalogo.load_grid(db_libri)

    def message_visualizza_libro(self, message: str, data: Optional[dict] = None):
        if message == "visualizza_libro":
            db_libro: DbLibro = data["libro"]
            self.redirect(LibroView(db_libro))

    def message_prenota_libro(self, message: str, data: Optional[dict] = None):
        if message == "prenota_libro":
            db_libro: DbLibro = data["libro"]
            model_prenotazione_libro: PrenotazioneLibro = self.models["prenotazioni_libri"]
            # check se l'utente non è sanzionato
            is_sanzionato = False  # TODO
            if is_sanzionato:
                self.alert(title=ALERT_PRENOTAZIONE_NEGATA_TITLE,
                           message=ALERT_UTENTE_SANZIONATO_MESSAGE)
                return
            # check se l'utente ha già prenotato questo libro
            has_already_this_prenotazione = model_prenotazione_libro.gia_effettuata(utente=Auth.user,
                                                                                    libro=db_libro)
            if has_already_this_prenotazione:
                self.alert(title=ALERT_PRENOTAZIONE_NEGATA_TITLE,
                           message=ALERT_LIBRO_GIA_PRENOTATO_MESSAGE)
                return
            # check se l'utente non ha fatto il numero massimo di prenotazioni
            has_max_prenotazioni = model_prenotazione_libro.raggiunto_limite(utente=Auth.user)
            if has_max_prenotazioni:
                self.alert(title=ALERT_PRENOTAZIONE_NEGATA_TITLE,
                           message=ALERT_MAX_PRENOTAZIONI_MESSAGE)
                return
            # il controllo della disponibilità del libro è stato già fatto

            # aggiungi prenotazione
            response = self.confirm(title=CONFIRM_PRENOTAZIONE_LIBRO_TITLE,
                                    message=CONFIRM_PRENOTAZIONE_LIBRO_MESSAGE.format(db_libro.titolo))
            if response == QMessageBox.StandardButton.Yes:
                model_prenotazione_libro.inserisci(db_libro)
                self.redirect(LibriPrenotatiView())

    def message_osserva_libro(self, message: str, data: Optional[dict] = None):
        if message == "osserva_libro":
            pass
