import sys

from PySide6.QtWidgets import QApplication

from database import Session


if __name__ == "__main__":
    app = QApplication(sys.argv)

    db_session = Session()

    from app import main_window
    main_window.show()

    sys.exit(app.exec())
