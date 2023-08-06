from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from abstract import View


class ModificaPrenotazioneView(View):
    def __init__(self, prenotazione):
        self.prenotazione = prenotazione
        super().__init__()
        # Salva la prenotazione come attributo


        # Chiama il metodo create_layout per creare e aggiungere i widget al layout


    def create_layout(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        # self.layout = QVBoxLayout()  # Correggi il nome della variabile layout
        # Visualizza i dettagli della prenotazione nella vista
        if hasattr(self.prenotazione, 'codice_aula'):
            label_aula = QLabel(f"Aula prenotata: {self.prenotazione.codice_aula}")
            layout.addWidget(label_aula)
        elif hasattr(self.prenotazione, 'codice_posto'):
            label_posto = QLabel(f"Posto prenotato: {self.prenotazione.codice_posto}")
            layout.addWidget(label_posto)
        else:
            label_nessuna_prenotazione = QLabel("Nessuna prenotazione trovata")
            layout.addWidget(label_nessuna_prenotazione)

        label_data = QLabel(f"Data prenotazione: {self.prenotazione.data_prenotazione}")
        layout.addWidget(label_data)

        label_ora_inizio = QLabel(f"Ora inizio: {self.prenotazione.ora_inizio}")
        layout.addWidget(label_ora_inizio)

        label_ora_fine = QLabel(f"Ora fine: {self.prenotazione.ora_fine}")
        layout.addWidget(label_ora_fine)
