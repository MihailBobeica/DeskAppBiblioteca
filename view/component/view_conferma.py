# TODO: eliminare

from PySide6.QtWidgets import QMessageBox

from abstract.view import View


class view_conferma(View):
    def create_layout(self, title, message) -> None:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Ok)

        # Esegui la finestra di dialogo e attendi la risposta dell'utente
        response = msg_box.exec()
        return response
