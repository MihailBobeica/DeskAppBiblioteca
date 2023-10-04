from typing import Optional

from abstract import Controller
from model.libri import ModelLibri
from model.statistiche import Statistiche


class StatisticheController(Controller):
    def __init__(self):
        super().__init__()

    def visualizza_statistiche(self, data: Optional[dict] = None) -> None:
        num_prestiti = Statistiche().num_prestiti()
        num_utenti = Statistiche().num_utenti()
        num_sospensioni = Statistiche().num_sospensioni()
        num_libri = Statistiche().num_libri()
        results = Statistiche().libri_piu_prestati()
        libri = []
        for res in results:
            libri.append(ModelLibri().by_id(res.libro_id).titolo)
        from view.Statistiche import StatsWindow
        self.redirect(StatsWindow(num_utenti, num_libri, num_prestiti, num_sospensioni, libri))
