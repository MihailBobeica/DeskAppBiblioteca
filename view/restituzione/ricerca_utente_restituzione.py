from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QGridLayout, QLineEdit, QPushButton, \
    QListWidget
from abstract.view import View
from PySide6.QtCore import Qt
from database import User as db_Utente
from model.utenti import ModelUtenti

class RicercaRestituzione(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        label = QLabel("matricola")
        self.input = QLineEdit()
        grid_layout.addWidget(label, 0, 0)
        grid_layout.addWidget(self.input, 0, 1)
        invia = QPushButton("Cerca")
        grid_layout.addWidget(invia, 1, 0)
        invia.clicked.connect(self.go_to_conferma_restituzione)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def __init__(self):
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_prestiti
        self.attach(controller_prestiti)




    def go_to_conferma_restituzione(self):
        self.notify(message="ricerca_prestito", data={"data": self.input.text()})
        '''if self.input.text():
            results = Utente.by_username(self, self.input.text())
            if results:
                from .libro_restituzione import Restituzione
                self.redirect(Restituzione(results))'''



