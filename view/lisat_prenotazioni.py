from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from abstract.view import View

class ListaPrenotazioniView(View):
    def __init__(self, prenotazione_controller):
        super().__init__()
        self.prenotazione_controller = prenotazione_controller

        # Ottieni l'ID dell'utente corrente
        utente_id = prenotazione_controller.get_username_utente_loggato()

        # Ottieni le prenotazioni dell'utente corrente utilizzando il controller
        prenotazioni_aula = prenotazione_controller.by_utente(utente_id)
        prenotazioni_posto = prenotazione_controller.search_by_utente(utente_id)  # Aggiunto

        # Crea un layout verticale per la vista
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Mostra le prenotazioni dell'utente nella vista
        label_prenotazioni_aula = QLabel("Prenotazioni Aula:")
        layout.addWidget(label_prenotazioni_aula)
        for prenotazione in prenotazioni_aula:
            label = QLabel(f"Aula: {prenotazione.codice_aula} - Data: {prenotazione.data_prenotazione}")
            layout.addWidget(label)

        label_prenotazioni_posto = QLabel("Prenotazioni Posto:")
        layout.addWidget(label_prenotazioni_posto)
        for prenotazione in prenotazioni_posto:
            label = QLabel(f"Posto: {prenotazione.codice_posto} - Data: {prenotazione.data_prenotazione}")
            layout.addWidget(label)
