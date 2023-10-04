from PySide6.QtWidgets import QLineEdit, QTableWidget, QVBoxLayout, QTableWidgetItem, QPushButton

from abstract import View
from utils.ui import get_style


class GestioneUtentiView(View):
    def create_layout(self) -> None:
        self.searchbar.textChanged.connect(self.search)
        self.searchbar.setPlaceholderText("Cerca utente per username, nome o cognome")
        self.searchbar.setStyleSheet(get_style("input"))

        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Username", "Nome", "Cognome", "", ""])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        layout = QVBoxLayout(self)

        layout.addWidget(self.searchbar)
        layout.addWidget(self.table)

    def __init__(self):
        self.searchbar = QLineEdit()
        self.table = QTableWidget()
        super().__init__()

        self.search("")

    def attach_controllers(self) -> None:
        from app import controller_utenti, controller_router
        self.attach(controller_utenti)
        self.attach(controller_router)

    def search(self, text: str) -> None:
        self.table.clearContents()
        self.table.setRowCount(0)
        self.notify("_fill_table_gestione_utenti",
                    data={"view": self,
                          "text": text})

    def add_row_table(self,
                      id_utente: int,
                      username: str,
                      nome: str,
                      cognome: str):
        item0 = QTableWidgetItem(username)
        item1 = QTableWidgetItem(nome)
        item2 = QTableWidgetItem(cognome)

        cronologia = QPushButton("Cronologia")
        sanzioni = QPushButton("Sanzioni")

        cronologia.clicked.connect(lambda: self.go_to_cronologia_utente(id_utente))
        sanzioni.clicked.connect(lambda: self.go_to_sanzioni_utente(id_utente))

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, item0)
        self.table.setItem(row_position, 1, item1)
        self.table.setItem(row_position, 2, item2)
        self.table.setCellWidget(row_position, 3, cronologia)
        self.table.setCellWidget(row_position, 4, sanzioni)

    def go_to_cronologia_utente(self, id_utente: int):
        self.notify("go_to_cronologia",
                    data={"id_utente": id_utente})

    def go_to_sanzioni_utente(self, id_utente: int):
        self.notify("go_to_sanzioni",
                    data={"id_utente": id_utente})
