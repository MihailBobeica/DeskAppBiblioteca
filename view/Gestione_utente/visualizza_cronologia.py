from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton, QListWidget, QGridLayout, QListWidgetItem
from database import PrenotazioneLibro as db_prenotazioni
from abstract.view import View
from model.utenti import ModelUtenti


class VisualizzaCronologiaView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout()
        grid_layout = QGridLayout()

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        for res in self.results:
            item2 = QListWidgetItem("Data inizio: " + str(res.data_inizio))
            item3 = QListWidgetItem("Data scadenza: " + str(res.data_scadenza))
            if res.data_restituzione is not None:
                item7 = QListWidgetItem("Data restituzione: " + str(res.data_restituzione))
            else:
                item7 = QListWidgetItem("Data restituzione: ")
            item4 = QListWidgetItem("ID libro: " + str(res.libro_id))
            item8 = QListWidgetItem("Titolo: " + res.libro.titolo)
            item5 = QListWidgetItem("Codice: " + res.codice)
            item6 = QListWidgetItem("")
            self.result_list.addItem(item2)
            self.result_list.addItem(item3)
            self.result_list.addItem(item7)
            self.result_list.addItem(item5)
            self.result_list.addItem(item8)
            self.result_list.addItem(item4)
            self.result_list.addItem(item6)

        layout.addWidget(self.result_list)
        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def __init__(self, results):
        self.results = results
        super().__init__()
