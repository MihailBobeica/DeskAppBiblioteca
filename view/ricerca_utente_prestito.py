from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QGridLayout, QLineEdit, QPushButton, \
    QListWidget
from abstract.view import View
from PySide6.QtCore import Qt
from database import Utente as db_Utente
from model.utente import Utente

class RicercaPrestito(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        label = QLabel("matricola")
        self.input = QLineEdit()
        grid_layout.addWidget(label, 0, 0)
        grid_layout.addWidget(self.input, 0, 1)
        invia = QPushButton("Cerca")
        grid_layout.addWidget(invia, 1, 0)
        invia.clicked.connect(self.cerca)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def __init__(self):
        super().__init__()

    def cerca(self):
        if self.input.text():
            results = Utente.by_username(self, self.input.text())
            if results:
                from .lista_prenotazioni_utente import ListaPrenotazioniUtente
                print(results)
                self.redirect(ListaPrenotazioniUtente(results))