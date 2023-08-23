

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QListWidget

class StatsWindow(QMainWindow):
    def __init__(self, utenti, libri, prestiti, sospensioni,titoli):
        super().__init__()

        self.setWindowTitle("Statistiche")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        users = QLabel(f"Utenti totali: {utenti}")
        books = QLabel(f"Libri totali: {libri}")
        loans = QLabel(f"Prestiti totali: {prestiti}")
        sosp = QLabel(f"Sospensioni totali: {sospensioni}")

        title_label = QLabel("Top 3 Titoli più presi in prestito:")
        title_list = QListWidget()
        for title in titoli:
            title_list.addItem(title)

        layout.addWidget(users)
        layout.addWidget(books)
        layout.addWidget(loans)
        layout.addWidget(sosp)
        layout.addWidget(title_label)
        layout.addWidget(title_list)

        central_widget.setLayout(layout)

