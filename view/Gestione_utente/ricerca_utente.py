from PySide6.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton
from abstract.view import View
from model.utente import Utente

class RicercaUtenteView(View):
    def create_layout(self) -> None:
        self.setWindowTitle('Ricerca operatore')
        layout = QVBoxLayout()

        grid_layout = QGridLayout()

        # Prima riga
        label1 = QLabel('username:')
        self.input1 = QLineEdit()
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(self.input1, 0, 1)

        layout.addLayout(grid_layout)

        invia = QPushButton('Invia')
        invia.clicked.connect(self.invia)
        layout.addWidget(invia)


        self.setLayout(layout)

    def attach_controllers(self) -> None:
        from app import  controller_gestione_utenti
        self.attach(controller_gestione_utenti)

    def __init__(self):
        super().__init__()



    def invia(self):
        self.notify(message="trova_utente", data={"username": self.input1.text()})
