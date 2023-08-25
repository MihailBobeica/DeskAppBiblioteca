from typing import Optional, Callable

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from model import PrenotazioneLibro
from utils.auth import Auth
from utils.key import KeyModel, KeyDb, Key
from utils.request import Request
from utils.strings import *
from view.component.catalogo import CatalogoComponent
from view.dettagli_prenotazione_libro import DettagliPrenotazioneLibroView
from view.libri_prenotati import LibriPrenotatiView
from view.libro import LibroView


class CatalogoController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

        self.action: dict[Request, Callable] = dict()

        self.action[Request.SEARCH] = self.search
        self.action[Request.GO_TO_DETTAGLI_LIBRO] = self.go_to_dettagli_libro
        self.action[Request.PRENOTA_LIBRO] = self.prenota_libro
        self.action[Request.OSSERVA_LIBRO] = self.osserva_libro
        self.action[Request.GO_TO_DETTAGLI_PRENOTAZIONE_LIBRO] = self.go_to_dettagli_prenotazione_libro
        self.action[Request.CANCELLA_PRENOTAZIONE_LIBRO] = self.cancella_prenotazione_libro

    def receive_message(self, message: Request, data: Optional[dict] = None) -> None:
        action = self.action.get(message)
        if action:
            action(data)
        else:
            raise ValueError("Invalid action type")

    def search(self, data: Optional[dict] = None):
        catalogo: CatalogoComponent = data[Key.CATALOGO]
        text = data[Key.TEXT]
        data_list = catalogo.search_strategy.search(self.models, text)
        catalogo.load_grid(data_list)

    def go_to_dettagli_libro(self, data: Optional[dict] = None):
        libro: DbLibro = data[KeyDb.LIBRO]
        context: str = data[Key.CONTESTO]
        self.redirect(LibroView(libro, context=context))  # TODO

    def prenota_libro(self, data: Optional[dict] = None):
        libro: DbLibro = data[KeyDb.LIBRO]
        model_prenotazione_libro: PrenotazioneLibro = self.models[KeyModel.PRENOTAZIONE_LIBRO]
        # check se l'utente non è sanzionato
        is_sanzionato = False  # TODO
        if is_sanzionato:
            self.alert(title=ALERT_PRENOTAZIONE_NEGATA_TITLE,
                       message=ALERT_UTENTE_SANZIONATO_MESSAGE)
            return
        # check se l'utente ha già prenotato questo libro
        has_already_this_prenotazione = model_prenotazione_libro.gia_effettuata(utente=Auth.user,
                                                                                libro=libro)
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
                                message=CONFIRM_PRENOTAZIONE_LIBRO_MESSAGE.format(libro.titolo))
        if response == QMessageBox.StandardButton.Yes:
            model_prenotazione_libro.inserisci(libro)
            self.redirect(LibriPrenotatiView())

    def osserva_libro(self, data: Optional[dict] = None):
        ...

    def go_to_dettagli_prenotazione_libro(self, data: Optional[dict] = None):
        libro: DbLibro = data[KeyDb.LIBRO]
        prenotazione: DbPrenotazioneLibro = data[KeyDb.PRENOTAZIONE_LIBRO]
        self.redirect(DettagliPrenotazioneLibroView(libro=libro,
                                                    prenotazione=prenotazione))

    def cancella_prenotazione_libro(self, data: Optional[dict] = None):
        libro: DbLibro = data[KeyDb.LIBRO]
        prenotazione: DbPrenotazioneLibro = data[KeyDb.PRENOTAZIONE_LIBRO]
        catalogo: CatalogoComponent = data[Key.CATALOGO]
        contesto = data[Key.CONTESTO]
        response = self.confirm(title=CANCELLA_PRENOTAZIONE_TITLE,
                                message=CONFIRM_CANCELLA_PRENOTAZIONE_MESSAGE.format(libro.titolo))
        if response == QMessageBox.StandardButton.Yes:
            model_prenotazione_libro: PrenotazioneLibro = self.models[KeyModel.PRENOTAZIONE_LIBRO]
            model_prenotazione_libro.cancella(prenotazione)
            # self.update_view(LibriPrenotatiView)
            catalogo.update()
            # self.replace(LibriPrenotatiView())
            # self.alert(title=CANCELLA_PRENOTAZIONE_TITLE,
            #            message=CANCELLAZIONE_PRENOTAZIONE_RIUSCITA_MESSAGE)
