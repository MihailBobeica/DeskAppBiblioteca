from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from view.component import SidebarComponent
from view.component.catalogo import CatalogoComponent


class HomeUtenteView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Catalogo",
                                    "Libri in prestito",
                                    "Libri prenotati",
                                    "Lista di osservazione",
                                    "Sanzioni",
                                    "Info",
                                    "Logout"),
                            style="button")
        catalogo = CatalogoComponent()

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(catalogo)

    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)

    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)

    def __init__(self):
        super().__init__()
