from abstract import Controller, BoundedModel
from typing import Optional
from model.statistiche import Statistiche
from model.libro import Libro
from utils.request import Request


class StatisticheController(Controller):
    def __init__(self):
        super().__init__()

    def receive_message(self, message: Request, data: Optional[dict] = None) -> None:
        if message == Request.GO_TO_STATISTICHE:
            num_prestiti = Statistiche.num_prestiti(self)
            num_utenti = Statistiche.num_utenti(self)
            num_sospensioni = Statistiche.num_sospensioni(self)
            num_libri = Statistiche.num_libri(self)
            results = Statistiche.libri_piu_prestati(self)
            libri = []
            for res in results:
                libri.append(Libro.by_id(self,res.libro_id).titolo)
            from view.Statistiche import StatsWindow
            self.redirect(StatsWindow(num_utenti,num_libri,num_prestiti,num_sospensioni,libri))

