from PySide6.QtWidgets import QLabel, QVBoxLayout, QGridLayout, QLineEdit, QPushButton

from abstract.view import View


class RicercaPrenotazioneLibroView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        label = QLabel("matricola")
        grid_layout.addWidget(label, 0, 0)
        grid_layout.addWidget(self.text_input, 0, 1)
        invia = QPushButton("Cerca")
        invia.clicked.connect(self.go_to_lista_prenotazioni)
        grid_layout.addWidget(invia, 1, 0)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def __init__(self):
        self.text_input = QLineEdit()
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_prenotazioni_libri
        self.attach(controller_prenotazioni_libri)

    def go_to_lista_prenotazioni(self):
        self.notify(message="ricerca_prenotazioni", data={"data": self.text_input.text()})
