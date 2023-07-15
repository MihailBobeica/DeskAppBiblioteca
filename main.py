import sys

from PySide6.QtWidgets import QApplication

from database import Session
from view.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    db_session = Session()

    window = MainWindow()

    window.show()
    sys.exit(app.exec())
