from PySide6.QtWidgets import QVBoxLayout

from abstract.view import View
from utils import Auth, ADMIN, OPERATORE, UTENTE
from view.first import FirstView
from view.home_admin import HomeAdminView
from view.home_operatore import HomeOperatoreView
from view.home_utente import HomeUtenteView


class HomePageView(View):
    def create_layout(self) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        if Auth.is_logged():
            if Auth.is_logged_as(ADMIN):
                layout.addWidget(HomeAdminView())
            elif Auth.is_logged_as(OPERATORE):
                layout.addWidget(HomeOperatoreView())
            elif Auth.is_logged_as(UTENTE):
                layout.addWidget(HomeUtenteView())
        else:
            layout.addWidget(FirstView())

        self.setLayout(layout)

    def __init__(self):
        super().__init__()
