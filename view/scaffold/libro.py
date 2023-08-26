from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QFrame, QVBoxLayout

from abstract import View
from database import BoundedDbModel
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from factory.button_component import ButtonComponentFactory
from factory.label_component import LabelComponentFactory
from utils.key import KeyButtonComponent
from utils.key import KeyDb
from utils.key import KeyLabelComponent
from utils.ui import get_cover_image
from view.component import CatalogoComponent


class LibroScaffold(View):
    def create_layout(self) -> None:
        # content
        # copertina
        image_label = QLabel()
        pixmap = QPixmap(get_cover_image(self.libro.immagine)).scaled(self.half_box_width, self.box_height,
                                                                      aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)

        # layout
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        contenitore_dati = QFrame()

        padding = 8
        h = self.box_height - padding

        if self.fullscreen:
            layout.setSpacing(50)
            contenitore_dati.setMaximumSize(self.half_box_width, h)
        else:
            self.setFixedSize(self.box_width, self.box_height)
            contenitore_dati.setFixedSize(self.half_box_width, h)

        self.v_layout.setAlignment(Qt.AlignTop)

        contenitore_dati.setLayout(self.v_layout)

        layout.addWidget(image_label)
        layout.addWidget(contenitore_dati)

    def __init__(self, catalogo: Optional[CatalogoComponent],
                 data: dict[KeyDb, BoundedDbModel],
                 box_size: tuple[int, int],
                 fullscreen: bool):
        self.catalogo = catalogo
        self.data = data
        self.box_width, self.box_height = box_size
        self.half_box_width = self.box_width // 2
        self.fullscreen = fullscreen

        self.libro: DbLibro = self.data.get(KeyDb.LIBRO)
        self.prenotazione: DbPrenotazioneLibro = self.data.get(KeyDb.PRENOTAZIONE_LIBRO)

        self.label_component_factory = LabelComponentFactory(data=self.data)
        self.button_component_factory = ButtonComponentFactory(view=self)

        self.v_layout = QVBoxLayout()
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_catalogo
        self.attach(controller_catalogo)

    def add_labels(self, label_keys: tuple[KeyLabelComponent, ...]) -> None:
        for label_key in label_keys:
            label = self.label_component_factory.create(label_key)
            self.v_layout.addWidget(label)
        self.v_layout.addStretch(1)

    def add_buttons(self, button_keys: tuple[KeyButtonComponent, ...]) -> None:
        for button_key in button_keys:
            button = self.button_component_factory.create(button_key)
            self.v_layout.addWidget(button)
