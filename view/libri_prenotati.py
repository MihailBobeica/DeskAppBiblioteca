from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton, QListWidget, QGridLayout, QListWidgetItem
from database import PrenotazioneLibro as db_prenotazioni
from abstract.view import View
from model.utente import Utente

class VisualizzaPrenotazioni(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout()
        grid_layout = QGridLayout()

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        for res in self.results:
            item = QListWidgetItem("Utente: "+res.utente)
            item2 = QListWidgetItem("Data prenotazione: " + str(res.data_prenotazione))
            item3 = QListWidgetItem("Data scadenza: " + str(res.data_scadenza))
            item4 = QListWidgetItem("Libro: "+ res.libro)
            item5 = QListWidgetItem("Codice: "+res.codice)
            item6 = QListWidgetItem("")
            self.result_list.addItem(item)
            self.result_list.addItem(item2)
            self.result_list.addItem(item3)
            self.result_list.addItem(item4)
            self.result_list.addItem(item5)
            self.result_list.addItem(item6)

        layout.addWidget(self.result_list)
        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def __init__(self, results):
        self.results = results
        super().__init__()





