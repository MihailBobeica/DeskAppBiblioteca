from PySide6.QtWidgets import QLineEdit, QTableWidget, QVBoxLayout, QTableWidgetItem, QPushButton

from abstract import View
from utils.ui import get_style


class GestioneLibriView(View):
    def create_layout(self) -> None:
        self.searchbar.textChanged.connect(self.search)
        self.searchbar.setPlaceholderText("Cerca libro per titolo o autore")
        self.searchbar.setStyleSheet(get_style("input"))

        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Titolo", "Autori", "ISBN", "", ""])
        self.table.setColumnWidth(0, 220)
        self.table.setColumnWidth(1, 220)
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
        from app import controller_router, controller_libri
        self.attach(controller_router)
        self.attach(controller_libri)

    def search(self, text: str) -> None:
        self.table.clearContents()
        self.table.setRowCount(0)
        self.notify("_fill_table_gestione_libri",
                    data={"view": self,
                          "text": text})

    def add_row_table(self,
                      id_libro: int,
                      titolo: str,
                      autori: str,
                      isbn: str):
        item0 = QTableWidgetItem(titolo)
        item1 = QTableWidgetItem(autori)
        item2 = QTableWidgetItem(isbn)

        modifica = QPushButton("Modifica")
        elimina = QPushButton("Elimina")

        modifica.clicked.connect(lambda: self.go_to_modifica_libro(id_libro))
        elimina.clicked.connect(lambda: self.elimina_libro(id_libro))

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, item0)
        self.table.setItem(row_position, 1, item1)
        self.table.setItem(row_position, 2, item2)
        self.table.setCellWidget(row_position, 3, modifica)
        self.table.setCellWidget(row_position, 4, elimina)

    def go_to_modifica_libro(self, id_libro: int):
        self.notify("go_to_modifica_libro",
                    data={"id_libro": id_libro})

    def elimina_libro(self, id_libro: int):
        self.notify("elimina_libro",
                    data={"id_libro": id_libro,
                          "view": self})
