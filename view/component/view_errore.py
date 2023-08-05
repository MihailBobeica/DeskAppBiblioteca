# TODO: eliminare

from PySide6.QtWidgets import QMessageBox

from abstract.view import View


class view_errore(View):
    def create_layout(self) -> None:
        alert_box = QMessageBox(self)
        alert_box.setWindowTitle(self.title)
        alert_box.setText(self.message)
        alert_box.setIcon(QMessageBox.Warning)
        alert_box.addButton("Ok", QMessageBox.AcceptRole)
        alert_box.exec()

    def __init__(self,title,message):
        self.title = title
        self.message = message
        super().__init__()