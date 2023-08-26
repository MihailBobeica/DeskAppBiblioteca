from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QFrame

from abstract.view import View
from database import Libro as DbLibro, BoundedDbModel
from utils.auth import Auth
from utils.context import CONTEXT_CATALOGO_LIBRI_GUEST
from utils.key import *
from utils.strings import UTENTE
from utils.ui import get_cover_image, LIBRO_VIEW_WIDTH, LIBRO_VIEW_HEIGHT
from view.component.button import *
from view.component.label import *
from view.scaffold import LibroViewScaffold


# class LibroViewScaffold(View):
#     def create_layout(self) -> None:
#         # content
#         # copertina
#         image_label = QLabel()
#         pixmap = QPixmap(get_cover_image(self.libro.immagine)).scaled(LIBRO_VIEW_WIDTH, LIBRO_VIEW_HEIGHT,
#                                                                       aspectMode=Qt.KeepAspectRatio)
#         image_label.setPixmap(pixmap)
#
#         # layout
#         layout = QHBoxLayout(self)
#         layout.setAlignment(Qt.AlignCenter)
#         layout.setSpacing(50)
#
#         contenitore_dati = QFrame()
#         contenitore_dati.setMaximumSize(LIBRO_VIEW_WIDTH, LIBRO_VIEW_HEIGHT)
#
#         v_layout = QVBoxLayout()
#         v_layout.setAlignment(Qt.AlignTop)
#         v_layout.setSpacing(8)
#
#         self.set_labels(v_layout)
#
#         v_layout.addStretch(1)
#
#         self.set_buttons(v_layout)
#
#         contenitore_dati.setLayout(v_layout)
#
#         layout.addWidget(image_label)
#         layout.addWidget(contenitore_dati)
#
#     def __init__(self, libro: DbLibro, context: str):
#         self.libro = libro
#         self.context = context
#         super().__init__()
#
#     def set_labels(self, layout: QVBoxLayout) -> None:
#         pass
#
#     def set_buttons(self, layout: QVBoxLayout) -> None:
#         pass


class LibroViewGuest(LibroViewScaffold):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(data=data)

        self.add_labels((KeyLabelComponent.TITOLO,
                         KeyLabelComponent.AUTORI,
                         KeyLabelComponent.ANNO_EDIZIONE,
                         KeyLabelComponent.ANNO_PUBBLICAZIONE,
                         KeyLabelComponent.EDITORE))


class LibroViewUtente(LibroViewScaffold):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(data=data)


class LibroView(View):
    def create_layout(self) -> None:
        # content:
        # copertina
        image_label = QLabel()
        pixmap = QPixmap(get_cover_image(self.libro.immagine)).scaled(320, 480, aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        # font
        font = QFont()
        font.setPointSize(14)
        # titolo
        label_title = QLabel(f"Titolo: {self.libro.titolo}")
        label_title.setWordWrap(True)
        label_title.setFont(font)
        # autori
        label_autor = QLabel(label_autori(self.libro.autori))
        label_autor.setWordWrap(True)
        label_autor.setFont(font)
        # anno edizione
        label_anno_edizione = QLabel(f"Anno edizione: {self.libro.anno_edizione.strftime('%Y')}")
        label_anno_edizione.setFont(font)
        # anno pubblicazione
        label_anno_pubblicazione = QLabel(f"Anno pubblicazione: {self.libro.anno_pubblicazione.strftime('%Y')}")
        label_anno_pubblicazione.setFont(font)
        # editore
        label_editore = QLabel(f"Editore: {self.libro.editore}")
        label_editore.setFont(font)
        # copie disponibili
        label_disponibili = QLabel(f"Copie disponibili: {self.libro.disponibili}")
        label_disponibili.setFont(font)
        # dati generici
        label_dati = QLabel(f"Dati: {self.libro.dati}")
        label_dati.setFont(font)
        # isbn
        label_isbn = QLabel(f"ISBN: {self.libro.isbn}")
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
            if self.context == CONTEXT_CATALOGO_LIBRI_GUEST:
                if self.libro.disponibili > 0:
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

    def __init__(self, libro: DbLibro, context: Optional[str] = None):
        self.libro = libro
        self.context = context
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_catalogo
        self.attach(controller_catalogo)

    def send_prenota_libro_request(self):
        self.notify(message="prenota_libro",
                    data={"libro": self.libro})

    def send_osserva_libro_request(self):
        self.notify(message="osserva_libro",
                    data={"libro": self.libro})
