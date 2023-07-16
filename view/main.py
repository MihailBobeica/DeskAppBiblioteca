from PySide6.QtWidgets import QWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()
        self.create_menu()

    def initialize(self):
        self.setWindowTitle("Catalogo")
        width, height = 640, 480
        self.resize(width, height)
        self.setMinimumSize(width, height)

    def create_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu.addAction("Quit")

        help_menu = menu.addMenu("Help")
        help_menu.addAction("Docs")

    def set_view(self, view: QWidget):
        self.setCentralWidget(view)
