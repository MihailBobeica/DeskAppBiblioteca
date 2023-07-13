import sys

from PySide6.QtWidgets import QApplication

from view.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # init views
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
