from PySide6.QtWidgets import QVBoxLayout

from abstract import View
from strategy.search import CercaPrenotazioniValide
from utils.backend import CONTEXT_CATALOGO_PRENOTAZIONI
from view.component.catalogo import CatalogoComponent


class LibriPrenotatiView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        catalogo = CatalogoComponent(CercaPrenotazioniValide(), context=CONTEXT_CATALOGO_PRENOTAZIONI)

        layout.addWidget(catalogo)

    def __init__(self):
        super().__init__()
