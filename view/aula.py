from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox
from model.posto import Posto


class DettaglioAulaView(QWidget):
    def __init__(self, nome_aula):
        super().__init__()
        self.nome_aula = nome_aula
        self.create_layout()

    def create_layout(self):
        layout = QVBoxLayout(self)
        label = QLabel(f"Aula: {self.nome_aula}")
        layout.addWidget(label)

        # Crea un'istanza della classe Posto
        posto_instance = Posto()

        # Ottieni i posti dal database utilizzando l'istanza di Posto per l'aula corrente
        posti = posto_instance.get_posti_by_aula(self.nome_aula)

        # Aggiungi i pulsanti dei posti dinamicamente
        for posto in posti:
            nome_posto = posto.nome
            posto_button = QPushButton(nome_posto)
            layout.addWidget(posto_button)

            # Connetti il segnale clicked del pulsante del posto al metodo on_posto_clicked
            posto_button.clicked.connect(lambda *args, posto=posto: self.on_posto_clicked(posto))

    def on_posto_clicked(self, posto_data):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Prenotazione effettuata")
        msg_box.setText(f"Prenotazione effettuata per il posto: {posto_data.nome} - Aula: {posto_data.aula}")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec()

