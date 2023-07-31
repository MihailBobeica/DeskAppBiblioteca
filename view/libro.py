from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QFrame

from abstract.view import View
from database import Libro
from utils.ui import get_cover_image, label_autori


class LibroView(View):
    def create_layout(self) -> None:
        # content

        # copertina
        image_label = QLabel()
        pixmap = QPixmap(get_cover_image(self.info.immagine)).scaled(320, 480, aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        # font
        font = QFont()
        font.setPointSize(16)
        # titolo
        label_title = QLabel(f"Titolo: {self.info.titolo}")
        label_title.setWordWrap(True)
        label_title.setFont(font)
        # autori
        label_autor = QLabel(label_autori(self.info.autori))
        label_autor.setWordWrap(True)
        label_autor.setFont(font)
        # anno edizione
        label_anno_edizione = QLabel(f"Anno edizione: {self.info.anno_edizione.strftime('%Y')}")
        label_anno_edizione.setFont(font)
        # anno pubblicazione
        label_anno_pubblicazione = QLabel(f"Anno pubblicazione: {self.info.anno_pubblicazione.strftime('%Y')}")
        label_anno_pubblicazione.setFont(font)
        # editore
        label_editore = QLabel(f"Editore: {self.info.editore}")
        label_editore.setFont(font)
        # copie disponibili
        label_disponibili = QLabel(f"Copie disponibili: {self.info.disponibili}")
        label_disponibili.setFont(font)
        # dati generici
        label_dati = QLabel(f"Dati: {self.info.dati}")
        label_dati.setFont(font)

        # layout
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(50)

        contenitore_dati = QFrame()
        contenitore_dati.setMaximumSize(320, 480)

        v_layout = QVBoxLayout()
        v_layout.setSpacing(8)

        v_layout.addWidget(label_title)
        v_layout.addWidget(label_autor)
        v_layout.addWidget(label_editore)
        v_layout.addWidget(label_anno_edizione)
        v_layout.addWidget(label_anno_pubblicazione)
        v_layout.addWidget(label_disponibili)
        v_layout.addWidget(label_dati)
        v_layout.addStretch(1)

        contenitore_dati.setLayout(v_layout)

        layout.addWidget(image_label)
        layout.addWidget(contenitore_dati)

    def __init__(self, db_libro: Libro):
        self.info = db_libro
        super().__init__()
