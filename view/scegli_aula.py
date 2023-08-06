from functools import partial
from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMessageBox

from controller.gestione_prenotazione_posto import PrenotazioneController
from database import Session
from abstract.view import View
from database import Aula
from view.aula import DettaglioAulaView
from datetime import datetime, timedelta

from view.lisat_prenotazioni import ListaPrenotazioniView


class ScegliAulaView(View):
    def __init__(self, tipo_prenotazione, data, durata):
        self.tipo_prenotazione = tipo_prenotazione
        self.data_selezionata = data
        self.durata = durata
        super().__init__()
        self.popup_shown = False
        self.dettaglio_aula_view = None
        # Crea il layout delle aule solo all'inizializzazione della vista
        self.create_layout()

    def create_layout(self):
        layout = QVBoxLayout(self)

        label_scegli_aula = QLabel("Scegli un aula disponibile:")
        layout.addWidget(label_scegli_aula)

        # Ottieni aule dal database utilizzando il modello Aula
        db_session = Session()
        aule = db_session.query(Aula).all()
        db_session.close()



        # Aggiungi i pulsanti delle opzioni aula dinamicamente
        for aula in aule:
            nome = aula.nome
            opzione_button = QPushButton(nome)
            layout.addWidget(opzione_button)

            # Connetti il segnale clicked del pulsante dell'opzione aula al metodo on_opzione_clicked
            opzione_button.clicked.connect(partial(self.on_opzione_clicked, aula))

    def close_dettaglio_aula_view(self):
        if self.dettaglio_aula_view:
            self.dettaglio_aula_view.deleteLater()
            self.dettaglio_aula_view = None

    def on_opzione_clicked(self, aula_data):
        if self.tipo_prenotazione == "prenota_aula" and not self.popup_shown:
            # Converti la data selezionata in un oggetto datetime
            data_selezionata = datetime.strptime(self.data_selezionata, "%Y-%m-%d %H:%M")

            # Converti la durata in un numero intero rappresentante le ore e moltiplicala per 60 per ottenere i minuti
            durata_ore = int(self.durata)
            durata_minuti = durata_ore * 60

            # Calcola ora_inizio e ora_fine in base alla data selezionata e alla durata
            ora_inizio = data_selezionata
            ora_fine = data_selezionata + timedelta(minutes=durata_minuti)
            # Ottieni l'username dell'utente loggato
            prenotazione_controller = PrenotazioneController()
            utente_id = prenotazione_controller.get_username_utente_loggato()

            # Salva effettivamente la prenotazione nel database
            prenotazione_controller = PrenotazioneController()
            prenotazione_controller.crea_prenotazione_aula(
                aula=aula_data.nome,
                data=data_selezionata,
                utente_id=utente_id,  # Sostituisci "ID_UTENTE" con l'ID dell'utente corrente
                durata=durata_minuti,  # Salva la durata in minuti
                ora_inizio=ora_inizio,
                ora_fine=ora_fine
            )

            # Mostra il pop-up solo se il cliente ha scelto di prenotare un'aula e il pop-up non è stato mostrato ancora
            QMessageBox.information(self, "Prenotazione effettuata",
                                    f"Prenotazione effettuata per l'aula: {aula_data.nome}")
            self.popup_shown = True
            lista_prenotazioni_view = ListaPrenotazioniView(prenotazione_controller, self.main_window)
            self.main_window.set_view(lista_prenotazioni_view)
        else:
            # Rimuovi tutti i widget dal layout attuale
            self.clear_layout()
            # Esegui lo split per ottenere solo la parte della data fino a "YYYY-MM-DD"
            data_selezionata = self.data_selezionata.split(" ")[0]

            # Crea una nuova istanza della vista DettaglioAulaView e passa il nome dell'aula selezionata
            self.dettaglio_aula_view = DettaglioAulaView(aula_data.nome, data_selezionata, self.durata)

            # Imposta la finestra principale come genitore della vista DettaglioAulaView
            self.dettaglio_aula_view.main_window = self.main_window

            # Aggiungi la vista DettaglioAulaView al layout principale della ScegliAulaView
            self.main_window.set_view(self.dettaglio_aula_view)

    def clear_layout(self):
        # Rimuovi tutti i widget dal layout principale
        while self.layout().count():
            item = self.layout().takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def update_aule_layout(self):
        # Rimuovi tutti i widget dal layout attuale
        self.clear_layout()

        # Ricrea il layout delle aule
        self.create_layout()
