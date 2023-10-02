from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from view.component import SidebarComponent


class HomeAdminView(View):
    def create_layout(self):
        self.sidebar.set_button("Aggiungi libro").clicked.connect(self.go_to_aggiungi_libro)
        self.sidebar.set_button("Gestione libri").clicked.connect(self.go_to_gestione_libri)
        self.sidebar.set_button("Aggiungi operatore").clicked.connect(self.go_to_aggiungi_operatore)
        self.sidebar.set_button("Gestione operatori").clicked.connect(self.go_to_gestione_operatori)
        self.sidebar.set_button("Gestione utenti").clicked.connect(self.go_to_gestione_utenti)
        self.sidebar.set_button("Statistiche").clicked.connect(self.go_to_statistiche)
        self.sidebar.set_button("Logout").clicked.connect(self.logout)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(self.sidebar)

    def attach_controllers(self) -> None:
        from app import controller_router, controller_logout
        self.attach(controller_router)
        self.attach(controller_logout)

    def __init__(self):
        self.sidebar = SidebarComponent()
        super().__init__()

    def go_to_aggiungi_libro(self):
        self.notify("go_to_aggiungi_libro")

    def go_to_gestione_libri(self):
        self.notify("go_to_gestione_libri")

    def go_to_aggiungi_operatore(self):
        self.notify("go_to_aggiungi_operatore")

    def go_to_gestione_operatori(self):
        self.notify("go_to_gestione_operatori")

    def go_to_gestione_utenti(self):
        self.notify("go_to_gestione_utenti")

    def go_to_statistiche(self):
        self.notify("go_to_statistiche")

    def logout(self):
        self.notify("logout")
