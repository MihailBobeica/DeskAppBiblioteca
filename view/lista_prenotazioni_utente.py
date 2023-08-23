import uuid
from datetime import datetime

from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QPushButton, QListWidget, QGridLayout, QMessageBox
from database import Utente as db_Utente
from abstract.view import View
from model.utente import Utente
from PySide6.QtCore import Qt
from view.home_operatore import HomeOperatoreView
from database import Prestito as db_prestito
from model.sanzione import Sanzione
from model.prenotazione_libro import PrenotazioneLibro


class ListaPrenotazioniUtente(View):
    def create_layout(self) -> None:

        layout = QVBoxLayout(self)
        
        label = QLabel("Nome: "+self.utente.nome)
        layout.addWidget(label)
        label = QLabel("Cognome: "+self.utente.cognome)
        layout.addWidget(label)
        label = QLabel("Username: "+self.utente.username)
        layout.addWidget(label)
        label = QLabel("Lista libri prenotati:")
        layout.addWidget(label)

        for j in self.lista_libri(self.utente):
            clickable_label = QLabel("codice: "+j.codice+"\nlibro: "+ j.libro.titolo)
            clickable_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            clickable_label.mousePressEvent = lambda event: self.on_label_clicked(event, j)



            layout.addWidget(clickable_label)

        self.setLayout(layout)


    def __init__(self, db_utente: db_Utente):
        self.utente = db_utente
        super().__init__()

    def lista_libri(self, utente: db_Utente):
        from model.prenotazione_libro import PrenotazioneLibro
        prenotazioni = PrenotazioneLibro.query_prenotazioni_valide(self,utente)
        return prenotazioni

    def on_label_clicked(self, event, prenotazione):
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Conferma")
        confirm_dialog.setText("Vuoi confermare l'avvenuto prestito del libro?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        result = confirm_dialog.exec_()
        if result == QMessageBox.Yes:
            from model.prestito import Prestito
            dati = {
                "libro": prenotazione.libro_id,
                "utente": prenotazione.utente_id
            }
            Prestito.inserisci(self, dati)
            PrenotazioneLibro.cancella(self,prenotazione)
            self.redirect(HomeOperatoreView())
        else:
            pass



