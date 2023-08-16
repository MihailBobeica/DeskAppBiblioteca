from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QFrame, QVBoxLayout

from abstract import View, BoundedView
from database import BoundedDbModel
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from utils.backend import LABEL_LIBRO, LABEL_PRENOTAZIONE_LIBRO
from utils.ui import get_cover_image, BOX_WIDTH
from view.component import CatalogoComponent


class LibroScaffold(View):
    def create_layout(self) -> None:
        self.setFixedSize(400, 240)

        # content
        # copertina
        image_label = QLabel()
        pixmap = QPixmap(get_cover_image(self.libro.immagine)).scaled(160, 240, aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)

        # layout
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        contenitore_dati = QFrame()
        contenitore_dati.setFixedSize(BOX_WIDTH, 240)

        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)
        v_layout.setSpacing(8)

        self.set_labels(v_layout)

        v_layout.addStretch(1)

        self.set_buttons(v_layout)

        contenitore_dati.setLayout(v_layout)

        layout.addWidget(image_label)
        layout.addWidget(contenitore_dati)

    def __init__(self, catalogo: CatalogoComponent, data: dict[str, BoundedDbModel]):
        self.catalogo = catalogo
        self.context = self.catalogo.context
        self.libro: DbLibro = data[LABEL_LIBRO]
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_catalogo
        self.attach(controller_catalogo)

    def set_labels(self, layout: QVBoxLayout) -> None:
        pass

    def set_buttons(self, layout: QVBoxLayout) -> None:
        pass


class LibroPrenotatoScaffold(LibroScaffold):
    def __init__(self, catalogo: BoundedView, data: dict[str, BoundedDbModel]):
        self.prenotazione: DbPrenotazioneLibro = data[LABEL_PRENOTAZIONE_LIBRO]
        super().__init__(catalogo=catalogo, data=data)
