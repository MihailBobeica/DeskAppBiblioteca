from PySide6.QtWidgets import QVBoxLayout, QPushButton, QMessageBox
from abstract.view import View
from database import PrenotazioneAula, PrenotazionePosto


class ListaTuttePrenotazioniView(View):
        def __init__(self, prenotazione_controller, main_window):
            super().__init__()
            self.prenotazione_controller = prenotazione_controller
            self.main_window = main_window



            # Ottieni tutte le prenotazioni
            prenotazioni_aula = prenotazione_controller.get_all_prenotazioni_aula()
            prenotazioni_posto = prenotazione_controller.get_all_prenotazioni_posto()

            # Crea un layout verticale per la vista
            layout = QVBoxLayout()
            self.setLayout(layout)

            # Mostra le prenotazioni dell'utente nella vista come pulsanti
            for prenotazione in prenotazioni_aula:
                button = QPushButton(f"Aula: {prenotazione.codice_aula} - Data: {prenotazione.data_prenotazione}")
                button.clicked.connect(self.create_apri_prenotazione_closure(prenotazione))
                layout.addWidget(button)

            for prenotazione in prenotazioni_posto:
                button = QPushButton(f"Posto: {prenotazione.codice_posto} - Data: {prenotazione.data_prenotazione}")
                button.clicked.connect(self.create_apri_prenotazione_closure(prenotazione))
                layout.addWidget(button)

        def create_apri_prenotazione_closure(self, prenotazione):
            def apri_prenotazione():
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

            return apri_prenotazione