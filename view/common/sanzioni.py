from PySide6.QtWidgets import QLabel, QVBoxLayout

from abstract import View


class SanzioniView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout(self)

        layout.addWidget(self.label_sanzione)
        layout.addStretch()

    def __init__(self, id_utente: int):
        self.id_utente = id_utente
        self.label_sanzione = QLabel()
        super().__init__()

        self.fill_view()

    def attach_controllers(self) -> None:
        from app import controller_sanzioni
        self.attach(controller_sanzioni)

    def fill_view(self):
        self.notify("_fill_view_sanzioni",
                    data={"view": self})

    def change_label(self, text: str):
        self.label_sanzione.setText(text)
