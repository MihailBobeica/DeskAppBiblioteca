from PySide6.QtWidgets import QWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_window()
        self.create_menu()

        from .first import First
        self.change_view(First(self))

    def init_window(self):
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

    def change_view(self, view: QWidget):
        self.setCentralWidget(view)
