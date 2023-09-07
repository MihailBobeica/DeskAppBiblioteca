from datetime import datetime

from PySide6.QtWidgets import QVBoxLayout, QPushButton, QMessageBox, QLabel
from abstract.view import View
from database import PrenotazioneAula, PrenotazionePosto


class ListaTuttePrenotazioniView(View):
    def __init__(self, prenotazione_controller, main_window):
        super().__init__()
        self.prenotazione_controller = prenotazione_controller
        self.main_window = main_window

        # Crea un layout verticale per la vista
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Carica le prenotazioni iniziali
        self.update_prenotazioni()

    def update_prenotazioni(self):
        # Rimuovi tutti i widget dal layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        # Ottieni tutte le prenotazioni
        prenotazioni_aula = self.prenotazione_controller.get_all_prenotazioni_aula_senza_attivazione()
        prenotazioni_posto = self.prenotazione_controller.get_all_prenotazioni_posto_senza_attivazione()

        if not prenotazioni_aula and not prenotazioni_posto:
            # Se non ci sono prenotazioni, mostra un messaggio di avviso
            label = QLabel("Non ci sono prenotazioni da confermare!")
            self.layout.addWidget(label)
        else:
            # Mostra le prenotazioni dell'utente nella vista come pulsanti
            for prenotazione in prenotazioni_aula:
                button = QPushButton(f"Aula: {prenotazione.codice_aula} - Data: {prenotazione.data_prenotazione}")
                button.clicked.connect(self.create_apri_prenotazione_closure(prenotazione))
                self.layout.addWidget(button)

            for prenotazione in prenotazioni_posto:
                button = QPushButton(f"Posto: {prenotazione.codice_posto} - Data: {prenotazione.data_prenotazione}")
                button.clicked.connect(self.create_apri_prenotazione_closure(prenotazione))
                self.layout.addWidget(button)

    def create_apri_prenotazione_closure(self, prenotazione):
        def apri_prenotazione():
            # Verifica se la data di attivazione è prima della data di inizio
            if datetime.now() <= prenotazione.data_prenotazione:
                message = "Ancora non è iniziata la prenotazione!"
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Attenzione")
                msg_box.setText(message)
                msg_box.exec_()
            else:
                # Mostra un pop-up con la scritta "Prenotazione Confermata!"
                message = "Prenotazione Confermata!"
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Conferma Prenotazione")
                msg_box.setText(message)
                msg_box.exec_()

                # Chiamata al metodo di conferma prenotazione del controller corrispondente
                if isinstance(prenotazione, PrenotazioneAula):
                    self.prenotazione_controller.conferma_prenotazione_aula(prenotazione.id)
                elif isinstance(prenotazione, PrenotazionePosto):
                    self.prenotazione_controller.conferma_prenotazione_posto(prenotazione.id)

                # Aggiorna la vista dopo la conferma
                self.update_prenotazioni()

        return apri_prenotazione
