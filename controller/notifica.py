from typing import Optional

from PySide6.QtWidgets import QDialog

from abstract import Controller, BoundedModel
from model import LibroOsservato
from utils.auth import auth
from utils.request import Request
from utils.strings import *


class NotificaController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: Request, data: Optional[dict] = None) -> None:
        if message == Request.CHECK_LIBRI_OSSERVATI:
            self.check_libri_osservati()

    def check_libri_osservati(self):
        model_osserva_libro: LibroOsservato = self.models["osserva_libri"]
        libri_osservati = model_osserva_libro.get_libri_ossevati(auth.user)
        for libro_osservato in libri_osservati:
            if libro_osservato.disponibili > 0:
                model_osserva_libro.rimuovi(auth.user, libro_osservato)
                self.alert(title=ALERT_LIBRO_ORA_DISPONIBILE_TITLE,
                           message=ALERT_LIBRO_ORA_DISPONIBILE_MESSAGE.format(libro_osservato.titolo))
