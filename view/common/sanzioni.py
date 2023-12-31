from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton

from abstract import View


class SanzioniView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        layout.addWidget(self.label_sanzione)
        layout.addStretch()

        if self.id_utente:
            h_layout = QHBoxLayout()
            indietro = QPushButton("Indietro")
            indietro.clicked.connect(self._go_to_gestione_utenti)
            h_layout.addStretch()
            h_layout.addWidget(indietro)
            h_layout.addStretch()
            layout.addLayout(h_layout)

    def __init__(self, id_utente: int):
        self.id_utente = id_utente
        self.label_sanzione = QLabel()
        super().__init__()

        self.fill_view()

    def attach_controllers(self) -> None:
        from app import controller_sanzioni
        self.attach(controller_sanzioni)
        if self.id_utente:
            from app import controller_router
            self.attach(controller_router)

    def fill_view(self):
        self.notify("_fill_view_sanzioni",
                    data={"view": self})

    def change_label(self, text: str):
        self.label_sanzione.setText(text)

    def _go_to_gestione_utenti(self):
        self.notify("go_to_gestione_utenti")
