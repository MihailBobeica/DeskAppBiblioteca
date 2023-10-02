import uuid
from datetime import datetime

from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton, QListWidget, QGridLayout, QMessageBox
from PySide6.QtWidgets import QLabel, QVBoxLayout
from database import User as db_Utente
from abstract.view import View
from PySide6.QtCore import Qt
from database import Prestito as db_prestito
from model.sanzioni import ModelSanzioni



class ConfermaRestituzioneView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        label = QLabel("Nome: "+self.utente.nome)
        layout.addWidget(label)
        label = QLabel("Cognome: "+self.utente.cognome)
        layout.addWidget(label)
        label = QLabel("Username: "+self.utente.username)
        layout.addWidget(label)
        label = QLabel("Lista libri in prestito:")
        layout.addWidget(label)

        for j in self.lista_libri:
            clickable_label = QLabel("codice: "+j.codice+"\ntitolo: ")
            clickable_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            clickable_label.mousePressEvent = lambda event: self.go_to_da_restituire(event, j)

            layout.addWidget(clickable_label)

        self.setLayout(layout)


    def __init__(self, db_utente: db_Utente, prestiti):
        self.utente = db_utente
        self.lista_libri = prestiti
        super().__init__()

    '''def lista_libri(self, id):
        from model.prestito import Prestito
        prestiti = Prestito.da_restituire(self,id)
        return prestiti'''


    def attach_controllers(self) -> None:
        from app import controller_prestiti
        self.attach(controller_prestiti)



    def go_to_da_restituire(self, event, prestito):
        self.notify(message="registra_restituzione", data={"prestito" : prestito})
        '''confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Conferma")
        confirm_dialog.setText("Vuoi confermare l'avvenuto prestito del libro?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        result = confirm_dialog.exec_()
        if result == QMessageBox.Yes:
            from model.prestito import Prestito
            Prestito.restituzione(self, prestito)
            # self.main_window.set_view(HomeOperatoreView())
        else:
            pass'''









