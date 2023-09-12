from PySide6.QtWidgets import QVBoxLayout

from abstract.view import View
from utils.key import KeyContext
from view.component import CatalogoComponent


# class VisualizzaPrestiti(View):
#     def create_layout(self) -> None:
#         layout = QVBoxLayout()
#         grid_layout = QGridLayout()
#
#         self.result_list = QListWidget()
#         layout.addWidget(self.result_list)
#
#         for res in self.results:
#             item = QListWidgetItem("Utente: "+res.utente)
#             item2 = QListWidgetItem("Data inizio: " + str(res.data_inizio))
#             item3 = QListWidgetItem("Data scadenza: " + str(res.data_scadenza))
#             item7 = QListWidgetItem("Data restituzione: " + str(res.data_restituzione))
#             item4 = QListWidgetItem("Libro: "+ res.libro)
#             item5 = QListWidgetItem("Codice: "+res.codice)
#             item6 = QListWidgetItem("")
#             self.result_list.addItem(item)
#             self.result_list.addItem(item2)
#             self.result_list.addItem(item3)
#             self.result_list.addItem(item4)
#             self.result_list.addItem(item5)
#             self.result_list.addItem(item6)
#
#         layout.addWidget(self.result_list)
#         layout.addLayout(grid_layout)
#         self.setLayout(layout)
#
#     def __init__(self, results):
#         self.results = results
#         super().__init__()


class LibriInPrestitoView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        layout.addWidget(self.catalogo)

    def __init__(self):
        self.catalogo: CatalogoComponent = CatalogoComponent(context=KeyContext.CATALOGO_LIBRI_IN_PRESTITO)
        super().__init__()

    def update(self):
        self.catalogo.update()
