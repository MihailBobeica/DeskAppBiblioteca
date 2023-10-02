from datetime import datetime

from PySide6.QtWidgets import QScrollArea, QTableWidget, QVBoxLayout, QTableWidgetItem, QPushButton, QFrame, \
    QGridLayout, QLabel

from abstract import View


class PostiPrenotatiView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        label_posti_singoli = QLabel("Prenotazioni posti singoli:")
        label_aule = QLabel("Prenotazioni aule:")

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        content_widget = QFrame(scroll_area)
        scroll_area.setWidget(content_widget)

        # Create a grid layout for the content widget
        grid_layout = QGridLayout(content_widget)

        self.table_posti_singoli.setColumnCount(5)
        self.table_posti_singoli.setHorizontalHeaderLabels(["Giorno", "Ora inizio", "Ora fine", "Codice posto", ""])
        self.table_posti_singoli.setColumnWidth(3, 200)
        self.table_posti_singoli.setMinimumWidth(600)
        self.table_posti_singoli.setEditTriggers(QTableWidget.NoEditTriggers)

        self.table_aule.setColumnCount(5)
        self.table_aule.setHorizontalHeaderLabels(["Giorno", "Ora inizio", "Ora fine", "Codice aula", ""])
        self.table_aule.setColumnWidth(3, 200)
        self.table_aule.setMinimumWidth(600)
        self.table_aule.setEditTriggers(QTableWidget.NoEditTriggers)

        grid_layout.addWidget(label_posti_singoli, 0, 0)
        grid_layout.addWidget(self.table_posti_singoli, 1, 0)
        grid_layout.addWidget(label_aule, 2, 0)
        grid_layout.addWidget(self.table_aule, 3, 0)

    def __init__(self):
        self.table_posti_singoli = QTableWidget()
        self.table_aule = QTableWidget()
        super().__init__()
        self._fill_table()

    def attach_controllers(self) -> None:
        from app import controller_posti
        self.attach(controller_posti)

    def add_row_posti_singoli(self,
                              id_prenotazione_posto_singolo: int,
                              ora_inizio: datetime,
                              ora_fine: datetime,
                              codice_posto_singolo: str):
        row_position = self.table_posti_singoli.rowCount()
        self.table_posti_singoli.insertRow(row_position)

        item1 = QTableWidgetItem(ora_inizio.strftime("%d %B %Y"))
        item2 = QTableWidgetItem(ora_inizio.strftime("%H:%M"))
        item3 = QTableWidgetItem(ora_fine.strftime("%H:%M"))
        item4 = QTableWidgetItem(codice_posto_singolo)

        button = QPushButton("Cancella")
        button.clicked.connect(lambda: self.cancella_prenotazione_posto_singolo(id_prenotazione_posto_singolo))

        self.table_posti_singoli.setItem(row_position, 0, item1)
        self.table_posti_singoli.setItem(row_position, 1, item2)
        self.table_posti_singoli.setItem(row_position, 2, item3)
        self.table_posti_singoli.setItem(row_position, 3, item4)
        self.table_posti_singoli.setCellWidget(row_position, 4, button)

    def add_row_aule(self,
                     id_prenotazione_aula: int,
                     ora_inizio: datetime,
                     ora_fine: datetime,
                     codice_aula: str):
        row_position = self.table_aule.rowCount()
        self.table_aule.insertRow(row_position)

        item1 = QTableWidgetItem(ora_inizio.strftime("%d %B %Y"))
        item2 = QTableWidgetItem(ora_inizio.strftime("%H:%M"))
        item3 = QTableWidgetItem(ora_fine.strftime("%H:%M"))
        item4 = QTableWidgetItem(codice_aula)

        button = QPushButton("Cancella")
        button.clicked.connect(lambda: self.cancella_prenotazione_aula(id_prenotazione_aula))

        self.table_aule.setItem(row_position, 0, item1)
        self.table_aule.setItem(row_position, 1, item2)
        self.table_aule.setItem(row_position, 2, item3)
        self.table_aule.setItem(row_position, 3, item4)
        self.table_aule.setCellWidget(row_position, 4, button)

    def _fill_table(self):
        self.notify("_fill_table_posti_prenotati",
                    data={"view": self})

    def cancella_prenotazione_posto_singolo(self, id_prenotazione_posto_singolo):
        self.notify("cancella_prenotazione_posto_singolo",
                    data={"id_prenotazione_posto_singolo": id_prenotazione_posto_singolo})

    def cancella_prenotazione_aula(self, id_prenotazione_aula):
        self.notify("cancella_prenotazione_aula",
                    data={"id_prenotazione_aula": id_prenotazione_aula})
