from database import Utente as db_Utente
from abstract.view import View
from PySide6.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QPushButton


class VisualizzaView(View):
    def create_layout(self) -> None:
        self.setWindowTitle('Visualizza operatore')
        layout = QVBoxLayout()

        grid_layout = QGridLayout()

        label1 = QLabel('username:'+self.utente.username)
        grid_layout.addWidget(label1, 0, 0)

        label2 = QLabel('nome:'+self.utente.nome)
        grid_layout.addWidget(label2, 1, 0)

        label3 = QLabel('cognome:'+self.utente.cognome)
        grid_layout.addWidget(label3, 2, 0)

        label4 = QLabel('ruolo:'+self.utente.ruolo)
        grid_layout.addWidget(label4, 3, 0)

        label5 = QLabel('password:'+self.utente.password)
        grid_layout.addWidget(label5, 4, 0)

        layout.addLayout(grid_layout)

        button_back = QPushButton('Indietro')
        button_back.clicked.connect(self.go_back)
        layout.addWidget(button_back)

        self.setLayout(layout)

    def __init__(self, db_utente: db_Utente):
        self.utente = db_utente
        super().__init__()

    def go_back(self):
        from view.homepage.admin import HomeAdminView
        self.redirect(HomeAdminView())

