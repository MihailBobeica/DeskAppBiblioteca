from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton, QListWidget, QGridLayout
from database import Utente as db_Utente
from abstract.view import View
from model.utente import Utente

class VisualizzaUtente(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        label = QLabel("nome o matricola")
        self.input = QLineEdit()
        grid_layout.addWidget(label,0,0)
        grid_layout.addWidget(self.input,0,1)
        invia = QPushButton("Cerca")
        grid_layout.addWidget(invia,1,0)
        invia.clicked.connect(self.cerca)

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)


        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def __init__(self, db_utente: db_Utente = None):
        self.utente = db_utente
        super().__init__()

    def cerca(self):
        if self.input.text():
            results = Utente.ricerca(self,self.input.text())
            if results:
                self.update_results(results)


    def update_results(self, results):
        self.result_list.clear()
        text = []
        for result in results:
            line1 = "Username: "+result.username
            line2 = "Nome: "+result.nome
            line3 = "Cognome: "+result.cognome
            line4 = "Ruolo: "+result.ruolo
            line5 = '\n'

            text.append(line1)
            text.append(line2)
            text.append(line3)
            text.append(line4)
            text.append(line5)
        self.result_list.addItems(text)


