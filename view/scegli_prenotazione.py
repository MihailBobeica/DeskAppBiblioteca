from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout

from abstract.view import View
from view.scegli_data import ScegliDataView

class ScegliPrenotazione(View):
    def __init__(self):
        super().__init__()
        self.tipo_prenotazione = None  # Inizializza l'attributo tipo_prenotazione a None

    def create_layout(self):
        layout = QVBoxLayout(self)
        label = QLabel("Scegli il tipo di prenotazione:")
        prenota_aula_btn = QPushButton("Prenota Aula")
        prenota_singolo_btn = QPushButton("Prenota Singolo")

        layout.addWidget(label)
        layout.addWidget(prenota_aula_btn)
        layout.addWidget(prenota_singolo_btn)

        prenota_aula_btn.clicked.connect(self.on_prenota_aula_clicked)
        prenota_singolo_btn.clicked.connect(self.on_prenota_singolo_clicked)

    def on_prenota_aula_clicked(self):
        self.tipo_prenotazione = "prenota_aula"  # Imposta il tipo di prenotazione a "prenota_aula"
        scegli_data_view = ScegliDataView(self.tipo_prenotazione)  # Passa il tipo di prenotazione alla vista ScegliDataView
        self.main_window.set_view(scegli_data_view)  # Imposta la nuova vista come vista attiva

    def on_prenota_singolo_clicked(self):
        self.tipo_prenotazione = "prenota_singolo"  # Imposta il tipo di prenotazione a "prenota_singolo"
        scegli_data_view = ScegliDataView(self.tipo_prenotazione)  # Passa il tipo di prenotazione alla vista ScegliDataView
        self.main_window.set_view(scegli_data_view)  # Imposta la nuova vista come vista attiva

    def get_tipo_prenotazione(self):
        return self.tipo_prenotazione  # Restituisce il tipo di prenotazione selezionato
