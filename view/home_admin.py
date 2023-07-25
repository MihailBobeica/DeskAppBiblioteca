from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from component import Placeholder
from view.component import SidebarComponent


class HomeAdminView(View):
    def create_layout(self):
        sidebar = SidebarComponent()
        sidebar.add_buttons(labels=("Crea operatore",
                                    "Elimina operatore",
                                    "Logout",),
                            style="button")
        content = Placeholder("Home admin")

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(content)

    def connect_buttons(self):
        logout_button = self.get_button("Logout")
        logout_button.clicked.connect(self.send_logout_request)
        inserisci_button = self.get_button("Crea operatore")
        inserisci_button.clicked.connect(self.crea_operatore)
        elimina_button = self.get_button("Elimina operatore")
        elimina_button.clicked.connect(self.elimina_operatore)


    def attach_controllers(self) -> None:
        from app import controller_logout
        self.attach(controller_logout)

    def __init__(self):
        super().__init__()

    def crea_operatore(self):
        from view.operatore import ProvaView
        self.redirect(ProvaView())

    def elimina_operatore(self):
        from view.delete_operatore import DeleteOpView
        self.redirect(DeleteOpView())

