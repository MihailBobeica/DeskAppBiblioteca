from PySide6.QtWidgets import QWidget, QHBoxLayout

from component import Sidebar, Placeholder


class First(QWidget):
    def __init__(self, parent_window: QWidget):
        super().__init__(parent_window)

        sidebar = Sidebar()
        self.btn = sidebar.add_buttons(("Login",))

        content = Placeholder("Catalogo")

        self.lyt = QHBoxLayout(self)
        self.lyt.addWidget(sidebar)
        self.lyt.addWidget(content)

        self.connect_buttons()

    def connect_buttons(self):
        from .login import Login
        self.btn["Login"].clicked.connect(lambda: self.parent().change_view(Login(self.parent())))
