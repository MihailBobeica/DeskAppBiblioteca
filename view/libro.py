from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QFrame, QPushButton

from abstract.view import View
from database import Libro as DbLibro
from utils.auth import Auth
from utils.strings import UTENTE
from utils.ui import get_cover_image, label_autori


class LibroView(View):
    def create_layout(self) -> None:
        # content:
        # copertina
        image_label = QLabel()
        pixmap = QPixmap(get_cover_image(self.db_libro.immagine)).scaled(320, 480, aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        # font
        font = QFont()
        font.setPointSize(14)
        # titolo
        label_title = QLabel(f"Titolo: {self.db_libro.titolo}")
        label_title.setWordWrap(True)
        label_title.setFont(font)
        # autori
        label_autor = QLabel(label_autori(self.db_libro.autori))
        label_autor.setWordWrap(True)
        label_autor.setFont(font)
        # anno edizione
        label_anno_edizione = QLabel(f"Anno edizione: {self.db_libro.anno_edizione.strftime('%Y')}")
        label_anno_edizione.setFont(font)
        # anno pubblicazione
        label_anno_pubblicazione = QLabel(f"Anno pubblicazione: {self.db_libro.anno_pubblicazione.strftime('%Y')}")
        label_anno_pubblicazione.setFont(font)
        # editore
        label_editore = QLabel(f"Editore: {self.db_libro.editore}")
        label_editore.setFont(font)
        # copie disponibili
        label_disponibili = QLabel(f"Copie disponibili: {self.db_libro.disponibili}")
        label_disponibili.setFont(font)
        # dati generici
        label_dati = QLabel(f"Dati: {self.db_libro.dati}")
        label_dati.setFont(font)
        # isbn
        label_isbn = QLabel(f"ISBN: {self.db_libro.isbn}")
        label_isbn.setFont(font)

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
        v_layout.addWidget(label_isbn)
        v_layout.addStretch(1)

        if Auth.is_logged_as(UTENTE):
            if self.db_libro.disponibili > 0:
                button_prenota = QPushButton("Prenota libro")
                button_prenota.clicked.connect(self.send_prenota_libro_request)
                v_layout.addWidget(button_prenota)
            else:
                button_osserva = QPushButton("Osserva libro")
                button_osserva.clicked.connect(self.send_osserva_libro_request)
                v_layout.addWidget(button_osserva)

        contenitore_dati.setLayout(v_layout)

        layout.addWidget(image_label)
        layout.addWidget(contenitore_dati)

    def __init__(self, db_libro: DbLibro):
        self.db_libro = db_libro
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_catalogo
        self.attach(controller_catalogo)

    def send_prenota_libro_request(self):
        self.notify(message="prenota_libro",
                    data={"libro": self.db_libro})

    def send_osserva_libro_request(self):
        self.notify(message="osserva_libro",
                    data={"libro": self.db_libro})
