from PySide6.QtWidgets import QVBoxLayout

from abstract import View
from utils.context import CONTEXT_CATALOGO_PRENOTAZIONI_LIBRI
from view.component.catalogo import CatalogoComponent


class LibriPrenotatiView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        layout.addWidget(self.catalogo)

    def __init__(self):
        self.catalogo: CatalogoComponent = CatalogoComponent(context=CONTEXT_CATALOGO_PRENOTAZIONI_LIBRI)
        super().__init__()

    def update(self):
        self.catalogo.update()
