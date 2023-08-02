from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QGridLayout, QMessageBox, \
    QDateTimeEdit, QSpinBox, QDateEdit, QFileDialog
from datetime import datetime

from abstract.view import View
from view.home_admin import HomeAdminView
from model.libro import Libro


class InserisciView(View):
    def create_layout(self) -> None:
        self.setWindowTitle('Inserisci libro')
        layout = QVBoxLayout()

        grid_layout = QGridLayout()

        # Prima riga
        '''label1 = QLabel('immagine:')
        self.input1 = QFileDialog()
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(self.input1, 0, 1)'''

        # Seconda riga
        label2 = QLabel('titolo:')
        self.input2 = QLineEdit()
        grid_layout.addWidget(label2, 1, 0)
        grid_layout.addWidget(self.input2, 1, 1)

        # Terza riga
        label3 = QLabel('autori:')
        self.input3 = QLineEdit()
        grid_layout.addWidget(label3, 2, 0)
        grid_layout.addWidget(self.input3, 2, 1)

        label4 = QLabel('editore:')
        self.input4 = QLineEdit()
        grid_layout.addWidget(label4, 3, 0)
        grid_layout.addWidget(self.input4, 3, 1)

        label5 = QLabel('isbn:')
        self.input5 = QLineEdit()
        grid_layout.addWidget(label5, 4, 0)
        grid_layout.addWidget(self.input5, 4, 1)

        label6 = QLabel('anno edizione:')
        self.input6 = QDateEdit()
        grid_layout.addWidget(label6, 5, 0)
        grid_layout.addWidget(self.input6, 5, 1)

        label7 = QLabel('anno pubblicazione:')
        self.input7 = QDateEdit()
        grid_layout.addWidget(label7, 6, 0)
        grid_layout.addWidget(self.input7, 6, 1)

        label8 = QLabel('disponibili:')
        self.input8 = QSpinBox()
        self.input8.setMinimum(1)
        grid_layout.addWidget(label8, 7, 0)
        grid_layout.addWidget(self.input8, 7, 1)

        label9 = QLabel('dati:')
        self.input9 = QLineEdit()
        grid_layout.addWidget(label9, 8, 0)
        grid_layout.addWidget(self.input9, 8, 1)

        layout.addLayout(grid_layout)

        invia = QPushButton('Aggiungi libro')
        invia.clicked.connect(self.invia)
        layout.addWidget(invia)


        self.setLayout(layout)


    def attach_controllers(self) -> None:
        from app import controller_gestione_libri
        self.attach(controller_gestione_libri)

    def __init__(self):
        super().__init__()


    def invia(self):
        self.notify(message="inserisci_libro", data={"titolo" : self.input2.text(),"autori" : self.input3.text(), "editore": self.input4.text(), "isbn" : self.input5.text(), "disponibili" :self.input8.text(), "dati":self.input9.text(), "anno_edizione":datetime.strptime(self.input6.date().toString('yyyy-MM-dd'), '%Y-%m-%d'),"anno_pubblicazione":datetime.strptime(self.input7.date().toString('yyyy-MM-dd'), '%Y-%m-%d'), "immagine":"prova"})
