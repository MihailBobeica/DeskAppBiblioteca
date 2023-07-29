from PySide6.QtWidgets import QLabel, QVBoxLayout
from abstract.view import View


class ListaPrenotazioniView(View):
    def create_layout(self):
        layout = QVBoxLayout(self)
        label = QLabel("Prenotazioni:")
        layout.addWidget(label)

    def attach_controllers(self):
        # Se necessario, collega i controller per questa vista qui
        pass

    def __init__(self):
        super().__init__()
