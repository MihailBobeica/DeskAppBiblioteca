from typing import Optional

from PySide6.QtWidgets import QMessageBox

from abstract import Controller, BoundedModel
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from model import PrenotazioneLibro
from utils.auth import Auth
from utils.strings import *
from view.component.catalogo import CatalogoComponent
from view.dettagli_prenotazione_libro import DettagliPrenotazioneLibroView
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
        self.message_visualizza_dettagli_prenotazione(message, data)
        self.message_cancella_prenotazione(message, data)

    def message_search(self, message: str, data: Optional[dict] = None):
        if message == "search":
            catalogo: CatalogoComponent = data["catalogo"]
            text = data["text"]
            data_list = catalogo.search_strategy.search(self.models, text)
            catalogo.load_grid(data_list)

    def message_visualizza_libro(self, message: str, data: Optional[dict] = None):
        if message == "visualizza_libro":
            libro: DbLibro = data["libro"]
            context: str = data["context"]
            self.redirect(LibroView(libro, context=context))

    def message_prenota_libro(self, message: str, data: Optional[dict] = None):
        if message == "prenota_libro":
            libro: DbLibro = data["libro"]
            model_prenotazione_libro: PrenotazioneLibro = self.models["prenotazioni_libri"]
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

    def message_osserva_libro(self, message: str, data: Optional[dict] = None):
        if message == "osserva_libro":
            pass

    def message_visualizza_dettagli_prenotazione(self, message: str, data: Optional[dict] = None):
        if message == "visualizza_dettagli_prenotazione":
            libro: DbLibro = data["libro"]
            prenotazione: DbPrenotazioneLibro = data["prenotazione"]
            self.redirect(DettagliPrenotazioneLibroView(libro=libro,
                                                        prenotazione=prenotazione))

    def message_cancella_prenotazione(self, message: str, data: Optional[dict] = None):
        if message == "cancella_prenotazione":
            libro: DbLibro = data["libro"]
            prenotazione: DbPrenotazioneLibro = data["prenotazione"]
            contesto = data["contesto"]
            response = self.confirm(title=CANCELLA_PRENOTAZIONE_TITLE,
                                    message=CONFIRM_CANCELLA_PRENOTAZIONE_MESSAGE.format(libro.titolo))
            if response == QMessageBox.StandardButton.Yes:
                model_prenotazione_libro: PrenotazioneLibro = self.models["prenotazioni_libri"]
                model_prenotazione_libro.cancella(prenotazione)
                self.update_view(LibriPrenotatiView)
                if contesto == "dettagli":
                    self.go_back()
                if contesto == "catalogo":
                    self.replace(LibriPrenotatiView())
                self.alert(title=CANCELLA_PRENOTAZIONE_TITLE,
                           message=CANCELLAZIONE_PRENOTAZIONE_RIUSCITA_MESSAGE)
