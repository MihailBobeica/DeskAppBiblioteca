from functools import partial
from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMessageBox
from database import Session
from abstract.view import View
from database import Aula
from view.aula import DettaglioAulaView


class ScegliAulaView(View):
    def __init__(self, tipo_prenotazione, data, durata):
        super().__init__()
        self.tipo_prenotazione = tipo_prenotazione
        self.data_selezionata = data
        self.durata = durata
        self.popup_shown = False

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

    def on_opzione_clicked(self, aula_data):
        if self.tipo_prenotazione == "prenota_aula" and not self.popup_shown:
            # Mostra il pop-up solo se il cliente ha scelto di prenotare un'aula e il pop-up non è stato mostrato ancora
            QMessageBox.information(self, "Prenotazione effettuata",
                                    f"Prenotazione effettuata per l'aula: {aula_data.nome}")
            self.popup_shown = True
        else:
            # Altrimenti, apri la vista DettaglioAulaView
            layout = self.layout()
            if layout is not None:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()

            # Crea una nuova istanza della vista DettaglioAulaView e passa il nome dell'aula selezionata
            dettaglio_aula_view = DettaglioAulaView(aula_data.nome)
            self.main_window.set_view(dettaglio_aula_view)