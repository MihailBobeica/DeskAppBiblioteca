from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QHBoxLayout, QFrame, QVBoxLayout, QLabel, QPushButton

from abstract import View
from database import Libro as DbLibro
from database import PrenotazioneLibro as DbPrenotazioneLibro
from utils.backend import DATE_FORMAT
from utils.ui import label_autori, get_cover_image


class DettagliPrenotazioneLibroView(View):
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
        # data prenotazione
        label_data_prenotazione = QLabel(
            f"Data prenotazione:\n{self.prenotazione.data_prenotazione.strftime(DATE_FORMAT)}")
        label_data_prenotazione.setFont(font)
        # data scadenza prenotazione
        label_data_scadenza = QLabel(
            f"Data scadenza prenotazione:\n{self.prenotazione.data_scadenza.strftime(DATE_FORMAT)}")
        label_data_scadenza.setFont(font)
        # codice prenotazione
        label_codice = QLabel(f"Codice prenotazione:\n{self.prenotazione.codice}")
        label_codice.setFont(font)

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
        v_layout.addWidget(label_data_prenotazione)
        v_layout.addWidget(label_data_scadenza)
        v_layout.addWidget(label_codice)
        v_layout.addStretch(1)

        button_cancella_prenotazione = QPushButton("Cancella prenotazione")
        button_cancella_prenotazione.clicked.connect(self.send_cancella_prenotazione_request)
        v_layout.addWidget(button_cancella_prenotazione)

        contenitore_dati.setLayout(v_layout)

        layout.addWidget(image_label)
        layout.addWidget(contenitore_dati)

    def __init__(self, libro: DbLibro, prenotazione: DbPrenotazioneLibro):
        self.libro = libro
        self.prenotazione = prenotazione
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_catalogo
        self.attach(controller_catalogo)

    def send_cancella_prenotazione_request(self):
        self.notify(message="cancella_prenotazione",
                    data={"libro": self.libro,
                          "prenotazione": self.prenotazione,
                          "contesto": "dettagli"})
