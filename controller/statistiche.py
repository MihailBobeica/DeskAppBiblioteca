from abstract import Controller
from model import ModelStatistiche
from view.admin import StatisticheView


class ControllerStatistiche(Controller):
    def __init__(self,
                 model_statistiche: ModelStatistiche):
        self.model_statistiche = model_statistiche
        super().__init__()

    def _fill_view_statistiche(self, view: StatisticheView):
        utenti_totali = self.model_statistiche.totale_utenti()
        libri_totali = self.model_statistiche.totale_libri()
        prestiti_totali = self.model_statistiche.totale_prestiti()
        sospensioni_totali = self.model_statistiche.totale_sospensioni()
        piu_prestati = self.model_statistiche.titoli_piu_prestati()
        view.fill_view(utenti_totali=utenti_totali,
                       libri_totali=libri_totali,
                       prestiti_totali=prestiti_totali,
                       sospensioni_totali=sospensioni_totali,
                       piu_prestati=piu_prestati)
