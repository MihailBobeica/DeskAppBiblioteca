from PySide6.QtWidgets import QMessageBox

from abstract.view import View


class Controller:
    def receive_message(self, message: str, data: dict) -> None:
        pass

    def __init__(self):
        from app import main_window
        self.main_window = main_window

    def redirect(self, view: View) -> None:
        self.main_window.set_view(view)

    def popup(self, title: str, message: str) -> QMessageBox:
        return QMessageBox.information(self.main_window.centralWidget(),
                                       title,
                                       message)

    def confirm(self, title: str, message: str) -> QMessageBox:
        return QMessageBox.question(self.main_window,
                                    title,
                                    message,
                                    QMessageBox.StandardButton.Yes,
                                    QMessageBox.StandardButton.No)

    def logout(self):
        from view.first import FirstView
        self.redirect(FirstView())
