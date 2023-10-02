from datetime import datetime

from PySide6.QtWidgets import QVBoxLayout, QPushButton, QFrame, QHBoxLayout

from abstract import View


class ScegliAulaView(View):
    def create_layout(self) -> None:
        main_layout = QVBoxLayout(self)

        container = QFrame()

        h_layout = QHBoxLayout(container)

        container.setLayout(h_layout)

        button_container = QFrame()
        button_container.setLayout(self.v_layout)

        h_layout.addStretch()
        h_layout.addWidget(button_container)
        h_layout.addStretch()

        main_layout.addWidget(container)
        main_layout.addStretch()

    def __init__(self, metodo: str, ora_inizio: datetime, ora_fine: datetime):
        self.metodo = metodo
        self.ora_inizio = ora_inizio
        self.ora_fine = ora_fine

        self.v_layout = QVBoxLayout()

        super().__init__()

        self.fill_view()

    def attach_controllers(self) -> None:
        from app import controller_posti
        self.attach(controller_posti)

    def fill_view(self):
        self.notify("_fill_view_scegli_aula",
                    data={"view": self})

    def add_aula(self, codice_aula: str):
        button_aula = QPushButton(codice_aula)
        button_aula.setFixedSize(200, 36)
        if self.metodo == "posto_singolo":
            button_aula.clicked.connect(lambda: self.scegli_posto_singolo(codice_aula))
        elif self.metodo == "aula":
            button_aula.clicked.connect(lambda: self.prenota_aula(codice_aula))
        else:
            raise ValueError("metodo prenotazione posto non valido")
        self.v_layout.addWidget(button_aula)

    def scegli_posto_singolo(self, codice_aula: str):
        self.notify("scegli_posto_singolo",
                    data={"codice_aula": codice_aula,
                          "ora_inizio": self.ora_inizio,
                          "ora_fine": self.ora_fine})

    def prenota_aula(self, codice_aula: str):
        self.notify("prenota_aula",
                    data={"codice_aula": codice_aula,
                          "ora_inizio": self.ora_inizio,
                          "ora_fine": self.ora_fine})
