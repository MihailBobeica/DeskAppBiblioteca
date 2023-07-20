from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel

from abstract.view import View


class LibroComponent(View):
    def create_layout(self) -> None:
        # content
        image_label = QLabel()


        # layout
        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignTop)


    def connect_buttons(self) -> None:
        pass

    def __init__(self):
        super().__init__()
