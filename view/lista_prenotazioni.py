from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton
from abstract.view import View
from view.prenotazione import VisualizzaPrenotazioneView


class ListaPrenotazioniView(View):
    def __init__(self):
        super().__init__()

        from controller.gestione_prenotazione_posto import PrenotazioneController
        self.prenotazione_controller = PrenotazioneController()

        # Ottieni l'ID dell'utente corrente
        utente_id = self.prenotazione_controller.get_username_utente_loggato()

        # Ottieni le prenotazioni dell'utente corrente utilizzando il controller
        prenotazioni_aula = self.prenotazione_controller.by_utente(utente_id)
        prenotazioni_posto = self.prenotazione_controller.search_by_utente(utente_id)

        # Crea un layout verticale per la vista
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Se non ci sono prenotazioni, mostra la scritta "Non ci sono Prenotazioni"
        if not prenotazioni_aula and not prenotazioni_posto:
            label = QLabel("Non ci sono prenotazioni!")
            layout.addWidget(label)
        else:
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
            # Apri la vista della prenotazione con i dettagli corrispondenti
            prenotazione_view = VisualizzaPrenotazioneView(prenotazione)
            self.main_window.set_view(prenotazione_view)

        return apri_prenotazione
