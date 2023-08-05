from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QFrame, QPushButton

from abstract import View
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from utils.auth import Auth
from utils.backend import CONTEXT_CATALOGO_PRENOTAZIONI, CONTEXT_CATALOGO, LABEL_LIBRO, LABEL_PRENOTAZIONE_LIBRO, \
    DATE_FORMAT
from utils.strings import UTENTE, OPERATORE, ADMIN
from utils.ui import get_cover_image, label_autori, BOX_WIDTH


class LibroComponent(View):
    def create_layout(self) -> None:
        self.setFixedSize(400, 240)

        # content
        # copertina
        image_label = QLabel(self)
        pixmap = QPixmap(get_cover_image(self.libro.immagine)).scaled(160, 240, aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        # titolo
        label_title = QLabel(f"Titolo: {self.libro.titolo}")
        label_title.setWordWrap(True)
        # autori
        label_autor = QLabel(label_autori(self.libro.autori))
        label_autor.setWordWrap(True)

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
        if self.context == CONTEXT_CATALOGO:
            # copie disponibili
            label_disponibili = QLabel(f"Copie disponibili: {self.libro.disponibili}")
            v_layout.addWidget(label_disponibili)
        if self.context == CONTEXT_CATALOGO_PRENOTAZIONI:
            prenotazione: DbPrenotazioneLibro = self.data[LABEL_PRENOTAZIONE_LIBRO]
            label_scadenza_prenotazione = QLabel(
                f"Scadenza prenotazione:\n{prenotazione.data_scadenza.strftime(DATE_FORMAT)}")
            v_layout.addWidget(label_scadenza_prenotazione)

        v_layout.addStretch(1)

        button_visualizza = QPushButton("Visualizza")
        button_visualizza.clicked.connect(self.send_visualizza_libro_request)

        if Auth.is_logged_as(UTENTE):
            if self.context == CONTEXT_CATALOGO_PRENOTAZIONI:
                button_dettagli_prenotazione = QPushButton("Dettagli prenotazione")
                button_dettagli_prenotazione.clicked.connect(self.send_visualizza_dettagli_prenotazione_request)
                v_layout.addWidget(button_dettagli_prenotazione)

                button_cancella_prenotazione = QPushButton("Cancella prenotazione")
                button_cancella_prenotazione.clicked.connect(self.send_cancella_prenotazione_request)
                v_layout.addWidget(button_cancella_prenotazione)
            else:
                if self.libro.disponibili > 0:
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

    def __init__(self, data: dict[str, object], context: Optional[str] = None):
        self.data = data
        self.libro: DbLibro = self.data[LABEL_LIBRO]
        self.context = context
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_catalogo
        self.attach(controller_catalogo)

    def send_visualizza_libro_request(self):
        self.notify(message="visualizza_libro",
                    data={"libro": self.libro,
                          "context": self.context})

    def send_prenota_libro_request(self):
        self.notify(message="prenota_libro",
                    data={"libro": self.libro})

    def send_osserva_libro_request(self):
        self.notify(message="osserva_libro",
                    data={"libro": self.libro})

    def send_visualizza_dettagli_prenotazione_request(self):
        prenotazione: DbPrenotazioneLibro = self.data[LABEL_PRENOTAZIONE_LIBRO]
        self.notify(message="visualizza_dettagli_prenotazione",
                    data={"libro": self.libro,
                          "prenotazione": prenotazione})

    def send_cancella_prenotazione_request(self):
        prenotazione: DbPrenotazioneLibro = self.data[LABEL_PRENOTAZIONE_LIBRO]
        self.notify(message="cancella_prenotazione",
                    data={"libro": self.libro,
                          "prenotazione": prenotazione,
                          "contesto": "catalogo"})
