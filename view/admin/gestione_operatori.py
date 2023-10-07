from PySide6.QtWidgets import QLineEdit, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout

from abstract import View
from utils.ui import get_style


class GestioneOperatoriView(View):
    def create_layout(self) -> None:
        self.searchbar.textChanged.connect(self.search)
        self.searchbar.setPlaceholderText("Cerca operatore per username, nome o cognome")
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
        from app import controller_router, controller_operatori
        self.attach(controller_router)
        self.attach(controller_operatori)

    def search(self, text: str) -> None:
        self.table.clearContents()
        self.table.setRowCount(0)
        self.notify("_fill_table_gestione_operatori",
                    data={"view": self,
                          "text": text})

    def add_row_table(self,
                      id_operatore: int,
                      username: str,
                      nome: str,
                      cognome: str):
        item0 = QTableWidgetItem(username)
        item1 = QTableWidgetItem(nome)
        item2 = QTableWidgetItem(cognome)

        modifica = QPushButton("Modifica")
        elimina = QPushButton("Elimina")

        modifica.clicked.connect(lambda: self.go_to_modifica_operatore(id_operatore))
        elimina.clicked.connect(lambda: self.elimina_operatore(id_operatore))

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, item0)
        self.table.setItem(row_position, 1, item1)
        self.table.setItem(row_position, 2, item2)
        self.table.setCellWidget(row_position, 3, modifica)
        self.table.setCellWidget(row_position, 4, elimina)

    def go_to_modifica_operatore(self, id_operatore: int):
        self.notify("go_to_modifica_operatore",
                    data={"id_operatore": id_operatore})

    def elimina_operatore(self, id_operatore: int):
        self.notify("elimina_operatore",
                    data={"id_operatore": id_operatore,
                          "view": self})
