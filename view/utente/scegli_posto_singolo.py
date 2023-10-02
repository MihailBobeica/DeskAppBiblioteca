from datetime import datetime

from PySide6.QtWidgets import QVBoxLayout, QScrollArea, QFrame, QPushButton, QLabel

from abstract import View


class ScegliPostoSingoloView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        label_aula = QLabel(f"Aula: {self.codice_aula}")

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(label_aula)
        layout.addWidget(scroll_area)

        content_widget = QFrame(scroll_area)
        scroll_area.setWidget(content_widget)

        self.v_layout = QVBoxLayout(content_widget)

    def __init__(self, codice_aula: str, ora_inizio: datetime, ora_fine: datetime):
        self.codice_aula = codice_aula
        self.ora_inizio = ora_inizio
        self.ora_fine = ora_fine

        self.v_layout = QVBoxLayout()
        super().__init__()

        self.fill_view()

    def attach_controllers(self) -> None:
        from app import controller_posti
        self.attach(controller_posti)

    def fill_view(self):
        self.notify("_fill_view_scegli_posto_singolo",
                    data={"view": self})

    def add_posto_singolo(self, codice_posto_singolo: str):
        button_posto_singolo = QPushButton(codice_posto_singolo)
        button_posto_singolo.setFixedSize(200, 24)
        button_posto_singolo.clicked.connect(lambda: self.prenota_posto_singolo(codice_posto_singolo))
        self.v_layout.addWidget(button_posto_singolo)

    def prenota_posto_singolo(self, codice_posto_singolo: str):
        self.notify("prenota_posto_singolo",
                    data={"codice_posto_singolo": codice_posto_singolo,
                          "ora_inizio": self.ora_inizio,
                          "ora_fine": self.ora_fine})
