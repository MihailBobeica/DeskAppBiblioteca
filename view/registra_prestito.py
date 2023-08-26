

from PySide6.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton
from abstract.view import View
from view.homepage.operatore import HomeOperatoreView



class RegistraPrestito(View):
    def create_layout(self) -> None:
        self.setWindowTitle('Ricerca prenotazione')
        layout = QVBoxLayout()

        grid_layout = QGridLayout()

        # Prima riga
        label1 = QLabel('codice prenotazione:')
        self.input1 = QLineEdit()
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(self.input1, 0, 1)

        layout.addLayout(grid_layout)

        invia = QPushButton('Invia')
        invia.clicked.connect(self.invia)
        layout.addWidget(invia)
        self.setLayout(layout)

    def invia(self):
        if self.input1.text():
            from model.prenotazione_libro import PrenotazioneLibro
            prenotazione = PrenotazioneLibro.by_codice(self,self.input1.text())
            dati = {"utente" : prenotazione.utente_id, "libro" : prenotazione.libro_id}
            from model.prestito import Prestito
            Prestito.inserisci(self,dati)
            self.redirect(HomeOperatoreView())

