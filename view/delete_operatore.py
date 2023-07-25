from PySide6.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from abstract.view import View
from view.home_admin import HomeAdminView
from model.utente import Utente

class DeleteOpView(View):
    def create_layout(self) -> None:
        self.setWindowTitle('Elimina operatore')
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

        button_back = QPushButton('Indietro')
        button_back.clicked.connect(self.go_back)
        layout.addWidget(button_back)

        self.setLayout(layout)


    def __init__(self):
        super().__init__()


    def go_back(self):
        from .home_admin import HomeAdminView
        self.redirect(HomeAdminView())

    def invia(self):
        if self.input1.text():
            Utente.elimina(self,self.input1.text())
            from .home_admin import HomeAdminView
            self.redirect(HomeAdminView())
        else:
            alert_box = QMessageBox(self)
            alert_box.setWindowTitle("Errore")
            alert_box.setText("Devi fornire un valore per tutti i campi di input")
            alert_box.setIcon(QMessageBox.Warning)
            alert_box.addButton("Ok", QMessageBox.AcceptRole)
            alert_box.exec()
