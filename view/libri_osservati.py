from PySide6.QtWidgets import QVBoxLayout

from abstract import View
from utils.key import KeyContext
from view.component.catalogo import CatalogoComponent


class LibriOsservatiView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        layout.addWidget(self.catalogo)

    def __init__(self):
        self.catalogo: CatalogoComponent = CatalogoComponent(context=KeyContext.CATALOGO_LIBRI_OSSERVATI)
        super().__init__()

    def refresh(self):
        self.catalogo.refresh()
