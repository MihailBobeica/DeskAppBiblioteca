from abstract.view import View

from database import Utente as db_Utente
from model.utente import Utente
from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QMessageBox
from utils import hash_password

class ModificaView(View):
    def create_layout(self) -> None:
        self.setWindowTitle('Modifica operatore')
        layout = QVBoxLayout()

        grid_layout = QGridLayout()

        # Prima riga
        label1 = QLabel('username:')
        self.input1 = QLineEdit()
        self.input1.setText(self.utente.username)
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(self.input1, 0, 1)

        # Seconda riga
        label2 = QLabel('nome:')
        self.input2 = QLineEdit()
        self.input2.setText(self.utente.nome)
        grid_layout.addWidget(label2, 1, 0)
        grid_layout.addWidget(self.input2, 1, 1)

        # Terza riga
        label3 = QLabel('cognome:')
        self.input3 = QLineEdit()
        self.input3.setText(self.utente.cognome)
        grid_layout.addWidget(label3, 2, 0)
        grid_layout.addWidget(self.input3, 2, 1)

        '''label6 = QLabel('password:')
        self.input6 = QLineEdit()
        self.input6.setText(self.utente.password)
        grid_layout.addWidget(label6, 5, 0)
        grid_layout.addWidget(self.input6, 5, 1)'''

        layout.addLayout(grid_layout)

        invia = QPushButton('Invia')
        invia.clicked.connect(self.invia)
        layout.addWidget(invia)

        button_back = QPushButton('Indietro')
        button_back.clicked.connect(self.go_back)
        layout.addWidget(button_back)

        self.setLayout(layout)

    def __init__(self, db_utente: db_Utente):
        self.utente = db_utente
        super().__init__()

    def go_back(self):
        from view.home_admin import HomeAdminView
        self.redirect(HomeAdminView())

    def invia(self):
        if self.input1.text() and self.input2.text() and self.input3.text() :
            dati = {"username" : self.input1.text(),
                    "nome" : self.input2.text(),
                    "cognome" : self.input3.text()
                    }
            Utente.modifica(self,dati,self.utente.username)
            from view.home_admin import HomeAdminView
            self.redirect(HomeAdminView())
        else:
            alert_box = QMessageBox(self)
            alert_box.setWindowTitle("Errore")
            alert_box.setText("Devi fornire un valore per tutti i campi di input")
            alert_box.setIcon(QMessageBox.Warning)
            alert_box.addButton("Ok", QMessageBox.AcceptRole)
            alert_box.exec()