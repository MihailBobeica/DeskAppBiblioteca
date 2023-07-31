from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from abstract.view import View

class VisualizzaPrenotazioneView(View):
    def __init__(self, prenotazione):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Visualizza i dettagli della prenotazione nella vista
        label_codice = QLabel(f"Codice prenotazione: {prenotazione.id}")
        layout.addWidget(label_codice)

        label_data = QLabel(f"Data prenotazione: {prenotazione.data_prenotazione}")
        layout.addWidget(label_data)

        label_ora_inizio = QLabel(f"Ora inizio: {prenotazione.ora_inizio}")
        layout.addWidget(label_ora_inizio)

        label_ora_fine = QLabel(f"Ora fine: {prenotazione.ora_fine}")
        layout.addWidget(label_ora_fine)

        # Aggiungi altri dettagli della prenotazione qui

        # Aggiungi layout orizzontale per i pulsanti Modifica e Cancella
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # Aggiungi il pulsante "Modifica"
        modifica_button = QPushButton("Modifica")
        modifica_button.clicked.connect(self.on_modifica_clicked)
        button_layout.addWidget(modifica_button)

        # Aggiungi il pulsante "Cancella"
        cancella_button = QPushButton("Cancella")
        cancella_button.clicked.connect(self.on_cancella_clicked)
        button_layout.addWidget(cancella_button)

    def on_modifica_clicked(self):
        
        print("Pulsante Modifica cliccato!")

    def on_cancella_clicked(self):

        print("Pulsante Cancella cliccato!")
