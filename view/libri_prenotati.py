from PySide6.QtWidgets import QVBoxLayout

from abstract import View
from strategy.search import CercaPrenotazioniValide
from utils.backend import CONTEXT_CATALOGO_PRENOTAZIONI
from view.component.catalogo import CatalogoComponent


class LibriPrenotatiView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        layout.addWidget(self.catalogo)

    def __init__(self):
        self.catalogo: CatalogoComponent = CatalogoComponent(CercaPrenotazioniValide(),
                                                             context=CONTEXT_CATALOGO_PRENOTAZIONI)
        super().__init__()

    def update(self):
        self.catalogo.update()
