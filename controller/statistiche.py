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
            self.visualizza_statistiche(data)



    def visualizza_statistiche(self, data: Optional[dict] = None) -> None:
        num_prestiti = Statistiche().num_prestiti()
        num_utenti = Statistiche().num_utenti()
        num_sospensioni = Statistiche().num_sospensioni()
        num_libri = Statistiche().num_libri()
        results = Statistiche().libri_piu_prestati()
        libri = []
        for res in results:
            libri.append(Libro().by_id( res.libro_id).titolo)
        from view.Statistiche import StatsWindow
        self.redirect(StatsWindow(num_utenti, num_libri, num_prestiti, num_sospensioni, libri))

