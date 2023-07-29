from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QFrame

from abstract.view import View
from database import Libro
from utils import get_image_path, label_autori, Auth, UTENTE


class LibroComponent(View):
    def create_layout(self) -> None:
        self.setFixedSize(400, 240)

        # content
        # copertina
        image_label = QLabel(self)
        pixmap = QPixmap(get_image_path(self.info.immagine)).scaled(160, 240, aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        # titolo
        label_title = QLabel(f"Titolo: {self.info.titolo}")
        label_title.setWordWrap(True)
        # autori
        label_autor = QLabel(label_autori(self.info.autori))
        label_autor.setWordWrap(True)
        # copie disponibili
        label_disponibili = QLabel(f"Copie disponibili: {self.info.disponibili}")

        # layout
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        contenitore_dati = QFrame()
        contenitore_dati.setFixedSize(180, 240)

        v_layout = QVBoxLayout()
        v_layout.setAlignment(Qt.AlignTop)
        v_layout.setSpacing(8)

        v_layout.addWidget(label_title)
        v_layout.addWidget(label_autor)
        v_layout.addWidget(label_disponibili)

        v_layout.addStretch(1)

        self.buttons_utente(layout=v_layout)
        self.add_buttons(labels=("Visualizza",),
                         layout=v_layout)

        contenitore_dati.setLayout(v_layout)

        layout.addWidget(image_label)
        layout.addWidget(contenitore_dati)

    def connect_buttons(self) -> None:
        button_visualizza = self.get_button("Visualizza")
        button_visualizza.clicked.connect(self.visualizza)

    def __init__(self, db_libro: Libro):
        self.info = db_libro
        super().__init__()

    def visualizza(self):
        from view.libro import LibroView
        self.redirect(LibroView(self.info))

    def buttons_utente(self, layout):
        if Auth.is_logged_as(UTENTE):
            if self.info.disponibili > 0:
                labels = ("Prenota libro",)
            else:
                labels = ("Osserva libro",)
            self.add_buttons(labels=labels,
                             layout=layout)
