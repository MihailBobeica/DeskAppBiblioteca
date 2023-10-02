from datetime import datetime
from typing import Optional

from PySide6.QtWidgets import QVBoxLayout, QLabel, QScrollArea, QTableWidget, QTableWidgetItem

from abstract import View


class CronologiaPrestitiView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        label_cronologia = QLabel("Cronologia prestiti:")

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.table)

        layout.addWidget(label_cronologia)
        layout.addWidget(scroll_area)

        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Titolo", "Autori", "ISBN", "Preso il", "Restituito il"])
        self.table.setMinimumWidth(700)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 250)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

    def __init__(self, id_utente: Optional[int]):
        self.id_utente = id_utente
        self.table = QTableWidget()
        super().__init__()

        self.fill_table()

    def attach_controllers(self) -> None:
        from app import controller_prestiti
        self.attach(controller_prestiti)

    def fill_table(self):
        self.notify("_fill_table_cronologia_prestiti",
                    data={"view": self})

    def add_row(self, titolo: str, autori: str, isbn: str, preso_il: datetime, restituito_il: datetime):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        item0 = QTableWidgetItem(titolo)
        item1 = QTableWidgetItem(autori)
        item2 = QTableWidgetItem(isbn)
        item3 = QTableWidgetItem(preso_il.strftime("%d %B %Y"))
        item4 = QTableWidgetItem(restituito_il.strftime("%d %B %Y"))

        self.table.setItem(row_position, 0, item0)
        self.table.setItem(row_position, 1, item1)
        self.table.setItem(row_position, 2, item2)
        self.table.setItem(row_position, 3, item3)
        self.table.setItem(row_position, 4, item4)
