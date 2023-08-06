from datetime import datetime, timedelta
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox

from abstract import View
from controller.gestione_prenotazione_posto import PrenotazioneController
from model.posto import Posto

class DettaglioAulaView(View):
    def __init__(self, nome_aula, data_selezionata, durata):
        self.nome_aula = nome_aula
        self.data_selezionata = data_selezionata
        self.durata = durata
        super().__init__()

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
        # Effettua la prenotazione solo se il posto è selezionato
        if posto_data and self.data_selezionata:
            # Converti la data selezionata in un oggetto datetime.date
            data_prenotazione = datetime.strptime(self.data_selezionata, "%Y-%m-%d").date()

            # Converti la durata in un numero intero rappresentante le ore e moltiplicala per 60 per ottenere i minuti
            durata_ore = int(self.durata)
            durata_minuti = durata_ore * 60

            # Crea oggetti datetime completi per ora_inizio e ora_fine
            ora_inizio = datetime.combine(data_prenotazione, datetime.strptime("08:30", "%H:%M").time())
            ora_fine = datetime.combine(data_prenotazione, datetime.strptime("08:30", "%H:%M").time()) + timedelta(minutes=durata_minuti)

            prenotazione_controller = PrenotazioneController()
            utente_id = prenotazione_controller.get_username_utente_loggato()
            # Effettua la prenotazione del posto
            prenotazione_controller.crea_prenotazione_posto(
                posto=posto_data.nome,
                data=data_prenotazione,
                utente_id=utente_id,  # Sostituisci "ID_UTENTE" con l'ID dell'utente corrente
                durata=durata_minuti,
                ora_inizio=ora_inizio,
                ora_fine=ora_fine
            )

            # Mostra un messaggio di conferma
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Prenotazione effettuata")
            msg_box.setText(f"Prenotazione effettuata per il posto: {posto_data.nome} - Aula: {posto_data.aula}")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.exec()
        else:
            QMessageBox.warning(self, "Attenzione", "Devi selezionare una data prima di prenotare un posto.")

    def clear_layout(self):
        while self.layout().count():
            item = self.layout().takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()