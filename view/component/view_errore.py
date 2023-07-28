from PySide6.QtWidgets import QMessageBox

from abstract.view import View


class view_errore(View):
    def create_layout(self,title,message) -> None:
        alert_box = QMessageBox(self)
        alert_box.setWindowTitle(title)
        alert_box.setText(message)
        alert_box.setIcon(QMessageBox.Warning)
        alert_box.addButton("Ok", QMessageBox.AcceptRole)
        alert_box.exec()