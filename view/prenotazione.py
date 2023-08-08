from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox
from abstract.view import View
from controller.gestione_prenotazione_posto import PrenotazioneController
from view.modifica_prenotazione import ModificaPrenotazioneView


class VisualizzaPrenotazioneView(View):
    def __init__(self, prenotazione):
        super().__init__()
        self.prenotazione = prenotazione  # Salva la prenotazione come attributo

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

    def open_modifica_view(self, prenotazione):
        # Crea un'istanza della nuova vista "vuota" passando l'oggetto prenotazione
        modifica_prenotazione_view = ModificaPrenotazioneView(prenotazione)

        # Imposta la nuova vista come vista corrente nella finestra principale
        self.main_window.set_view(modifica_prenotazione_view)

    def on_modifica_clicked(self):
        # Apri la nuova vista "vuota" per la modifica
        # self.open_modifica_view(self.prenotazione)

        modifica_prenotazione_view = ModificaPrenotazioneView(self.prenotazione)

    # Imposta la nuova vista come vista corrente nella finestra principale
        self.main_window.set_view(modifica_prenotazione_view)
    def on_cancella_clicked(self):
        # Chiedi conferma all'utente prima di procedere con la cancellazione
        conferma_cancellazione = QMessageBox.question(self, "Conferma cancellazione",
                                                      "Sei sicuro di voler cancellare questa prenotazione?",
                                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if conferma_cancellazione == QMessageBox.Yes:
            # Chiamare il metodo del controller per cancellare la prenotazione
            prenotazione_controller = PrenotazioneController()
            if hasattr(self.prenotazione, 'codice_aula'):
                prenotazione_controller.cancella_prenotazione_aula(self.prenotazione.id)

            else:
                prenotazione_controller.cancella_prenotazione_posto(self.prenotazione.id)



            # Importa la classe ListaPrenotazioniView qui all'interno della funzione on_cancella_clicked
        from view.lisat_prenotazioni import ListaPrenotazioniView

            # Dopo aver cancellato la prenotazione, vai alla vista ListaPrenotazioniView
        lista_prenotazioni_view = ListaPrenotazioniView(prenotazione_controller, self.main_window)
        self.main_window.set_view(lista_prenotazioni_view)
