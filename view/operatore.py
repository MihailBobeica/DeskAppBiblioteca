from PySide6.QtCore import QFile
from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QGridLayout

from abstract.view import View
from view.component import SidebarComponent
from view.home_admin import HomeAdminView
from controller.gestione_operatore import gestione_operatore




class ProvaView(View):
    def create_layout(self) -> None:
        self.setWindowTitle('Input Utente')
        layout = QVBoxLayout()

        grid_layout = QGridLayout()

        # Prima riga
        label1 = QLabel('username:')
        self.input1 = QLineEdit()
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(self.input1, 0, 1)

        # Seconda riga
        label2 = QLabel('nome:')
        self.input2 = QLineEdit()
        grid_layout.addWidget(label2, 1, 0)
        grid_layout.addWidget(self.input2, 1, 1)

        # Terza riga
        label3 = QLabel('cognome:')
        self.input3 = QLineEdit()
        grid_layout.addWidget(label3, 2, 0)
        grid_layout.addWidget(self.input3, 2, 1)

        '''label4 = QLabel('età:')
        self.input4 = QLineEdit()
        grid_layout.addWidget(label4, 3, 0)
        grid_layout.addWidget(self.input4, 3, 1)

        label5 = QLabel('telefono:')
        self.input5 = QLineEdit()
        grid_layout.addWidget(label5, 4, 0)
        grid_layout.addWidget(self.input5, 4, 1)'''

        label6 = QLabel('password:')
        self.input6 = QLineEdit()
        grid_layout.addWidget(label6, 5, 0)
        grid_layout.addWidget(self.input6, 5, 1)

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
        gestione_operatore.crea_operatore(self,self.input1.text(),self.input2.text(),self.input3.text(),self.input6.text())
        self.redirect(HomeAdminView())



















