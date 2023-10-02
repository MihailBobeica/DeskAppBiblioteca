from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout

from abstract.view import View
from database import User as db_Utente


class ConfermaPrenotazioneLibroView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        label = QLabel("Nome: " + self.utente.nome)
        layout.addWidget(label)
        label = QLabel("Cognome: " + self.utente.cognome)
        layout.addWidget(label)
        label = QLabel("Username: " + self.utente.username)
        layout.addWidget(label)
        label = QLabel("Lista libri prenotati:")
        layout.addWidget(label)

        '''for j in self.lista_libri(self.utente):
            clickable_label = QLabel("codice: "+j.codice+"\nlibro: "+ j.libro.titolo)
            clickable_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            clickable_label.mousePressEvent = lambda event: self.on_label_clicked(event, j)'''

        for j in self.lista_libri:
            clickable_label = QLabel("codice: " + j.codice + "\nlibro: " + j.libro.titolo)
            clickable_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            clickable_label.mousePressEvent = lambda event: self.registra_prestito(event, j)

            layout.addWidget(clickable_label)

        self.setLayout(layout)

    def __init__(self, db_utente: db_Utente, prenotazioni):
        self.utente = db_utente
        self.lista_libri = prenotazioni
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_prestiti
        self.attach(controller_prestiti)

    def registra_prestito(self, event, prenotazione):
        self.notify(message="registra_prestito", data={"libro": prenotazione.libro_id, "utente": prenotazione.utente_id,
                                                       "prenotazione": prenotazione})
