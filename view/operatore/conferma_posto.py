from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QLabel, QScrollArea, QFrame, QTableWidget, QTableWidgetItem, \
    QPushButton

from abstract import View
from utils.ui import get_style


class ConfermaPostoView(View):
    def create_layout(self) -> None:
        self.searchbar.textChanged.connect(self.search)
        self.searchbar.setPlaceholderText("Ricerca utente tramite username, nome o cognome")
        self.searchbar.setStyleSheet(get_style("input"))

        adesso = datetime.now()
        label_titolo = QLabel(f"Prenotazioni posti di oggi {adesso.strftime('%d %B %Y')}")

        layout = QVBoxLayout(self)
        layout.addWidget(self.searchbar)
        layout.addWidget(label_titolo)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        content_widget = QFrame(scroll_area)
        scroll_area.setWidget(content_widget)

        # Create a grid layout for the content widget
        self.v_layout = QVBoxLayout(content_widget)
        self.v_layout.setAlignment(Qt.AlignTop)

    def __init__(self):
        self.searchbar = QLineEdit()
        self.v_layout = QVBoxLayout()
        super().__init__()

        self.search("")

    def attach_controllers(self) -> None:
        from app import controller_posti
        self.attach(controller_posti)

    def search(self, text: str):
        # clear layout
        while self.v_layout.count():
            item = self.v_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # fill layout
        self.notify("_fill_view_conferma_posto",
                    data={"view": self,
                          "text": text})

    def add_dati(self, username: str, nome: str, cognome: str, dati: list[dict]):
        container = QFrame()
        container.setFrameStyle(QFrame.Box)
        container.setLineWidth(1)
        container.setFixedHeight(200)
        v_layout = QVBoxLayout(container)

        label_username = QLabel(f"Username: {username}")
        label_nome = QLabel(f"Nome: {nome}")
        label_cognome = QLabel(f"Cognome: {cognome}")

        v_layout.addWidget(label_username)
        v_layout.addWidget(label_nome)
        v_layout.addWidget(label_cognome)

        self._add_table_prenotazioni(v_layout, dati)

        self.v_layout.addWidget(container)

    def _add_table_prenotazioni(self, layout: QVBoxLayout, dati: list[dict]):
        table = QTableWidget()
        table.setColumnCount(4)
        table.setColumnWidth(0, 220)
        table.setHorizontalHeaderLabels(["Codice", "Ora inizio", "Ora fine", ""])
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        for d in dati:
            self._add_row_prenotazione(table, **d)
        table.setFixedHeight(120)
        layout.addWidget(table)

    def _add_row_prenotazione(self,
                              table: QTableWidget,
                              id_prenotazione: int,
                              metodo: str,
                              codice: str,
                              ora_inizio: datetime,
                              ora_fine: datetime):
        row_position = table.rowCount()
        table.insertRow(row_position)

        item0 = QTableWidgetItem(codice)
        item1 = QTableWidgetItem(ora_inizio.strftime("%H:%M"))
        item2 = QTableWidgetItem(ora_fine.strftime("%H:%M"))

        button = QPushButton("Conferma")
        if metodo == "posto_singolo":
            button.clicked.connect(lambda: self.registra_prenotazione_posto_singolo(id_prenotazione))
        elif metodo == "aula":
            button.clicked.connect(lambda: self.registra_prenotazione_aula(id_prenotazione))
        else:
            raise ValueError("Metodo conferma prenotazione posto errato!")
        table.setItem(row_position, 0, item0)
        table.setItem(row_position, 1, item1)
        table.setItem(row_position, 2, item2)
        table.setCellWidget(row_position, 3, button)

    def registra_prenotazione_posto_singolo(self, id_prenotazione: int):
        self.notify("registra_prenotazione_posto_singolo",
                    data={"id_prenotazione": id_prenotazione,
                          "view": self})

    def registra_prenotazione_aula(self, id_prenotazione: int):
        self.notify("registra_prenotazione_aula",
                    data={"id_prenotazione": id_prenotazione,
                          "view": self})
