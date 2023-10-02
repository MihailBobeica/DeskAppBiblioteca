from PySide6.QtWidgets import QVBoxLayout

from abstract import View
from utils.key import KeyContext
from view.component.catalogo import CatalogoComponent


class CatalogoView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        layout.addWidget(self.catalogo)

    def __init__(self, context: KeyContext):
        self.catalogo: CatalogoComponent = CatalogoComponent(context=context)
        super().__init__()

    def refresh(self):
        self.catalogo.refresh()


class LibriPrenotatiView(CatalogoView):
    def __init__(self):
        super().__init__(KeyContext.CATALOGO_PRENOTAZIONI_LIBRI)


class ListaDiOsservazioneView(CatalogoView):
    def __init__(self):
        super().__init__(KeyContext.CATALOGO_LIBRI_OSSERVATI)


class LibriInPrestitoView(CatalogoView):
    def __init__(self):
        super().__init__(KeyContext.CATALOGO_LIBRI_IN_PRESTITO)
