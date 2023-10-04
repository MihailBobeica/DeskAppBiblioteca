from PySide6.QtWidgets import QLabel, QListWidget, QVBoxLayout, QHBoxLayout

from abstract import View


class StatisticheView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        label_statistiche = QLabel("Statistiche")
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(label_statistiche)
        h_layout.addStretch()
        label_piu_presi_in_prestito = QLabel("Top 3 titoli più prestati:")

        layout.addLayout(h_layout)
        layout.addWidget(self.utenti_totali)
        layout.addWidget(self.libri_totali)
        layout.addWidget(self.prestiti_totali)
        layout.addWidget(self.sospensioni_totali)
        layout.addWidget(label_piu_presi_in_prestito)
        layout.addWidget(self.piu_prestati)

    def __init__(self):
        self.utenti_totali = QLabel()
        self.libri_totali = QLabel()
        self.prestiti_totali = QLabel()
        self.sospensioni_totali = QLabel()
        self.piu_prestati = QListWidget()
        super().__init__()

        self._fill_view()

    def attach_controllers(self) -> None:
        from app import controller_statistiche
        self.attach(controller_statistiche)

    def _fill_view(self):
        self.notify("_fill_view_statistiche",
                    data={"view": self})

    def fill_view(self,
                  utenti_totali: int,
                  libri_totali: int,
                  prestiti_totali: int,
                  sospensioni_totali: int,
                  piu_prestati: list[str]):
        self.utenti_totali.setText(f"Utenti totali: {utenti_totali}")
        self.libri_totali.setText(f"Libri totali: {libri_totali}")
        self.prestiti_totali.setText(f"Prestiti totali: {prestiti_totali}")
        self.sospensioni_totali.setText(f"Sospensioni totali: {sospensioni_totali}")

        # piu_prestati (pp)
        for pp in piu_prestati:
            self.piu_prestati.addItem(pp)
