from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout

from abstract.view import View
from view.component import SidebarComponent


class HomeOperatoreView(View):
    def create_layout(self):
        self.sidebar.set_button("Registra prestito").clicked.connect(self.go_to_registra_prestito)
        self.sidebar.set_button("Registra restituzione").clicked.connect(self.go_to_registra_restituzione)
        self.sidebar.set_button("Conferma posto").clicked.connect(self.go_to_conferma_posto)
        self.sidebar.set_button("Logout").clicked.connect(self.logout)
        self.sidebar.layout().addStretch()

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.sidebar)

    def attach_controllers(self) -> None:
        from app import controller_router, controller_logout
        self.attach(controller_router)
        self.attach(controller_logout)

    def __init__(self):
        self.sidebar = SidebarComponent()
        super().__init__()

    def go_to_registra_prestito(self):
        self.notify("go_to_registra_prestito")

    def go_to_registra_restituzione(self):
        self.notify("go_to_registra_restituzione")

    def go_to_conferma_posto(self):
        self.notify("go_to_conferma_posto")

    def logout(self):
        self.notify("logout")
