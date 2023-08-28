from typing import Optional, Callable

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from factory import LibroViewFactory
from model import PrenotazioneLibro
from utils.auth import auth
from utils.key import KeyDb
from utils.request import *
from utils.strings import *
from view.component.catalogo import CatalogoComponent
from view.libri_prenotati import LibriPrenotatiView
from view.libro import PrenotazioneLibroView


class CatalogoController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

        self.action: dict[Request, Callable] = dict()

        self.action[Request.SEARCH] = self.search
        self.action[Request.GO_TO_VISUALIZZA_LIBRO] = self.visualizza_libro
        self.action[Request.PRENOTA_LIBRO] = self.prenota_libro
        self.action[Request.OSSERVA_LIBRO] = self.osserva_libro
        self.action[Request.GO_TO_DETTAGLI_PRENOTAZIONE_LIBRO] = self.visualizza_dettagli_prenotazione_libro
        self.action[Request.CANCELLA_PRENOTAZIONE_LIBRO] = self.cancella_prenotazione_libro
        self.action[Request.GO_TO_LIBRI_PRENOTATI] = self.visualizza_libri_prenotati

    def receive_message(self, message: Request, data: Optional[dict] = None) -> None:
        action = self.action.get(message)
        if action:
            action(data)

    def search(self, data: Optional[dict] = None):
        catalogo: CatalogoComponent = data["catalogo"]
        text = data["text"]
        data_list = catalogo.search_strategy.search(self.models, text)
        catalogo.load_grid(data_list)

    def visualizza_libro(self, data: Optional[dict] = None):
        key = auth.get_key()
        libro_view_factory = LibroViewFactory(data=data)
        self.main_window.set_view(libro_view_factory.create(key=key))

    def prenota_libro(self, data: Optional[dict] = None):
        libro: DbLibro = data.get(KeyDb.LIBRO)
        model_prenotazione_libro: PrenotazioneLibro = self.models["prenotazioni_libri"]
        # check se l'utente non è sanzionato
        is_sanzionato = False  # TODO
        if is_sanzionato:
            self.alert(title=ALERT_PRENOTAZIONE_NEGATA_TITLE,
                       message=ALERT_UTENTE_SANZIONATO_MESSAGE)
            return
        # check se l'utente ha già prenotato questo libro
        has_already_this_prenotazione = model_prenotazione_libro.gia_effettuata(utente=auth.user,
                                                                                libro=libro)
        if has_already_this_prenotazione:
            self.alert(title=ALERT_PRENOTAZIONE_NEGATA_TITLE,
                       message=ALERT_LIBRO_GIA_PRENOTATO_MESSAGE)
            return
        # check se l'utente non ha fatto il numero massimo di prenotazioni
        has_max_prenotazioni = model_prenotazione_libro.raggiunto_limite(utente=auth.user)
        if has_max_prenotazioni:
            self.alert(title=ALERT_PRENOTAZIONE_NEGATA_TITLE,
                       message=ALERT_MAX_PRENOTAZIONI_MESSAGE)
            return
        # il controllo della disponibilità del libro è stato già fatto

        # aggiungi prenotazione
        response = self.confirm(title=CONFIRM_PRENOTAZIONE_LIBRO_TITLE,
                                message=CONFIRM_PRENOTAZIONE_LIBRO_MESSAGE.format(libro.titolo))
        if response == QMessageBox.StandardButton.Yes:
            model_prenotazione_libro.inserisci(libro)
            self.redirect(LibriPrenotatiView())

    def osserva_libro(self, data):
        ...

    def visualizza_dettagli_prenotazione_libro(self, data: Optional[dict] = None):
        self.redirect(PrenotazioneLibroView(data))

    def cancella_prenotazione_libro(self, data: Optional[dict] = None):
        libro: DbLibro = data.get(KeyDb.LIBRO)
        prenotazione: DbPrenotazioneLibro = data.get(KeyDb.PRENOTAZIONE_LIBRO)
        response = self.confirm(title=CANCELLA_PRENOTAZIONE_TITLE,
                                message=CONFIRM_CANCELLA_PRENOTAZIONE_MESSAGE.format(libro.titolo))
        if response == QMessageBox.StandardButton.Yes:
            model_prenotazione_libro: PrenotazioneLibro = self.models["prenotazioni_libri"]
            model_prenotazione_libro.cancella(prenotazione)
            catalogo: CatalogoComponent = data.get("catalogo")
            if catalogo:
                catalogo.update()
            else:
                self.visualizza_libri_prenotati()

    def visualizza_libri_prenotati(self, data: Optional[dict] = None):
        self.redirect(LibriPrenotatiView())
