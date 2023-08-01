from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QFrame, QPushButton

from abstract import View
from database import Libro
from utils.ui import get_cover_image, label_autori, BOX_WIDTH
from utils.auth import Auth
from utils.strings import UTENTE, OPERATORE, ADMIN


class LibroComponent(View):
    def create_layout(self) -> None:
        self.setFixedSize(400, 240)

        # content
        # copertina
        image_label = QLabel(self)
        pixmap = QPixmap(get_cover_image(self.db_libro.immagine)).scaled(160, 240, aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        # titolo
        label_title = QLabel(f"Titolo: {self.db_libro.titolo}")
        label_title.setWordWrap(True)
        # autori
        label_autor = QLabel(label_autori(self.db_libro.autori))
        label_autor.setWordWrap(True)
        # copie disponibili
        label_disponibili = QLabel(f"Copie disponibili: {self.db_libro.disponibili}")

        # layout
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        contenitore_dati = QFrame()
        contenitore_dati.setFixedSize(BOX_WIDTH, 240)

        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)
        v_layout.setSpacing(8)

        v_layout.addWidget(label_title)
        v_layout.addWidget(label_autor)
        v_layout.addWidget(label_disponibili)

        v_layout.addStretch(1)

        button_visualizza = QPushButton("Visualizza")
        button_visualizza.clicked.connect(self.send_visualizza_libro_request)

        if Auth.is_logged_as(UTENTE):
            if self.db_libro.disponibili > 0:
                button_prenota = QPushButton("Prenota libro")
                button_prenota.clicked.connect(self.send_prenota_libro_request)
                v_layout.addWidget(button_prenota)
            else:
                button_osserva = QPushButton("Osserva libro")
                button_osserva.clicked.connect(self.send_osserva_libro_request)
                v_layout.addWidget(button_osserva)
        elif Auth.is_logged_as(OPERATORE):
            pass
        elif Auth.is_logged_as(ADMIN):
            pass

        v_layout.addWidget(button_visualizza)

        contenitore_dati.setLayout(v_layout)

        layout.addWidget(image_label)
        layout.addWidget(contenitore_dati)

    # def connect_buttons(self) -> None:
    #     button_visualizza = self.get_button("Visualizza")
    #     button_visualizza.clicked.connect(self.visualizza)
    #     if self.get_button("Prenota libro"):
    #         self.get_button("Prenota libro").clicked.connect(self.prenota_libro)

    def __init__(self, db_libro: Libro):
        self.db_libro = db_libro
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_catalogo
        self.attach(controller_catalogo)

    def send_visualizza_libro_request(self):
        self.notify(message="visualizza_libro",
                    data={"libro": self.db_libro})

    def send_prenota_libro_request(self):
        self.notify(message="prenota_libro",
                    data={"libro": self.db_libro})

    def send_osserva_libro_request(self):
        self.notify(message="osserva_libro",
                    data={"libro": self.db_libro})

    # def visualizza(self):
    #     from view.libro import LibroView
    #     self.redirect(LibroView(self.info))
    #
    #
    #
    # def prenota_libro(self):
    #     from model.prenotazione_libro import PrenotazioneLibro
    #     PrenotazioneLibro.inserisci(self, self.info)