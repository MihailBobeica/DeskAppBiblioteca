from typing import Optional

from PySide6.QtWidgets import QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QLabel, QGridLayout, QHBoxLayout

from abstract import View
from database import Operatore


class AggiungiModificaOperatoreView(View):
    def create_layout(self) -> None:
        v_layout = QVBoxLayout(self)

        label_window_title = QLabel()
        if self.metodo == "aggiungi":
            label_window_title.setText("Aggiungi operatore")
            self.conferma.setText("Aggiungi")
        elif self.metodo == "modifica":
            label_window_title.setText("Modifica operatore")
            self.conferma.setText("Modifica")
        else:
            raise ValueError("metodo aggiungi/modifica operatore view errato!")

        grid_layout = QGridLayout()

        label_username = QLabel("Username")
        label_nome = QLabel("Nome")
        label_cognome = QLabel("Cognome")
        label_password = QLabel("Password")

        grid_layout.addWidget(label_username, 0, 0)
        grid_layout.addWidget(self.username, 0, 1)
        grid_layout.addWidget(label_nome, 1, 0)
        grid_layout.addWidget(self.nome, 1, 1)
        grid_layout.addWidget(label_cognome, 2, 0)
        grid_layout.addWidget(self.cognome, 2, 1)
        grid_layout.addWidget(label_password, 3, 0)
        grid_layout.addWidget(self.password, 3, 1)

        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.conferma)
        h_layout.addStretch()

        v_layout.addLayout(grid_layout)
        v_layout.addStretch()
        v_layout.addLayout(h_layout)

        self.conferma.clicked.connect(self.aggiungi_modifica_operatore)

    def __init__(self, metodo: str, operatore: Optional[Operatore] = None):
        self.metodo = metodo
        self.operatore = operatore

        if self.metodo == "aggiungi":
            self.username = QLineEdit()
        elif self.metodo == "modifica":
            self.username = QLabel()
        else:
            raise ValueError("metodo aggiungi/modifica operatore view errato!")
        self.nome = QLineEdit()
        self.cognome = QLineEdit()
        self.password = QLineEdit()
        self.conferma = QPushButton()

        self.fill_dati_operatore()

        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_operatori
        self.attach(controller_operatori)

    def fill_dati_operatore(self):
        if self.operatore:
            self.username.setText(self.operatore.username)
            self.nome.setText(self.operatore.nome)
            self.cognome.setText(self.operatore.cognome)

    def aggiungi_modifica_operatore(self):
        if not (username := self.username.text()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire lo username\ndell'operatore.")
            return
        if not (nome := self.nome.text()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire il nome\ndell'operatore.")
            return
        if not (cognome := self.cognome.text()):
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire il cognome\ndell'operatore.")
            return
        if not (password := self.password.text()) and self.metodo == "aggiungi":
            QMessageBox.warning(self,
                                "Attenzione",
                                "Devi inserire la password dell'operatore.")
            return
        data = {"metodo": self.metodo,
                "username": username,
                "nome": nome,
                "cognome": cognome,
                "password": password}
        if self.metodo == "aggiungi":
            data.update({"id_operatore": None})
        elif self.metodo == "modifica":
            data.update({"id_operatore": self.operatore.id})
        else:
            raise ValueError("metodo aggiungi/modifica operatore view errato!")
        self.notify("aggiungi_modifica_operatore",
                    data=data)
