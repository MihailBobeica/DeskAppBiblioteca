from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout

from abstract.view import View
from database import Libro
from utils import get_image_path, label_autori


class LibroComponent(View):
    def create_layout(self) -> None:
        # layout
        layout = QHBoxLayout(self)

        layout.setAlignment(Qt.AlignTop)

    def connect_buttons(self) -> None:
        pass

    def __init__(self, db_libro: Libro):
        super().__init__()

        self.setFixedSize(400, 240)

        image_label = QLabel(self)
        pixmap = QPixmap(get_image_path(db_libro.immagine)).scaled(160, 240, aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)

        label_title = QLabel(f"Titolo: {db_libro.titolo}")
        label_title.setWordWrap(True)
        label_autor = QLabel(label_autori(db_libro.autori))
        label_autor.setWordWrap(True)
        label_editore = QLabel(f"Editore: {db_libro.editore}")
        label_disponibili = QLabel(f"Copie disponibili: {db_libro.disponibili}")
        label_dati = QLabel(f"Dati: {db_libro.dati}")

        layout = self.layout()
        v_layout = QVBoxLayout()
        layout.addWidget(image_label)
        layout.addLayout(v_layout)

        v_layout.addWidget(label_title)
        v_layout.addWidget(label_autor)
        v_layout.addWidget(label_editore)
        v_layout.addWidget(label_disponibili)
        v_layout.addWidget(label_dati)

        v_layout.addStretch(1)

        self.add_buttons(labels=("Visualizza",),
                         layout=v_layout)

        v_layout.setAlignment(Qt.AlignTop)

