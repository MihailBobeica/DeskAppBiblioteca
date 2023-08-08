from PySide6.QtWidgets import QLabel, QVBoxLayout
from database import Utente as db_Utente
from abstract.view import View
from PySide6.QtCore import Qt
from view.homepage.operatore import HomeOperatoreView



class Restituzione(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)
        for i in self.utente:
            label = QLabel("Nome: "+i.nome)
            layout.addWidget(label)
            label = QLabel("Cognome: "+i.cognome)
            layout.addWidget(label)
            label = QLabel("Username: "+i.username)
            layout.addWidget(label)
            label = QLabel("Lista libri in prestito:")
            layout.addWidget(label)
            for j in self.lista_libri(i.username):
                clickable_label = QLabel("ISBN: "+j.libro, self)
                clickable_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
                clickable_label.mousePressEvent = lambda event: self.on_label_clicked(event, j)

                layout.addWidget(clickable_label)

        self.setLayout(layout)


    def __init__(self, db_utente: db_Utente):
        self.utente = db_utente
        super().__init__()

    def lista_libri(self, username):
        from model.prestito import Prestito
        libri = Prestito.by_utente(self,username)
        return libri

    def on_label_clicked(self, event, prestito):
        from model.prestito import Prestito
        Prestito.restituzione(self,prestito)
        self.redirect(HomeOperatoreView())





