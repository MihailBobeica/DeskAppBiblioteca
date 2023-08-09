from abstract import BoundedView
from utils.auth import Auth
from utils.strings import UTENTE, OPERATORE, ADMIN
from view.homepage import HomeAdminView, HomeOperatoreView, HomeUtenteView, HomeGuestView


class HomepageFactory:
    def create_homepage(self) -> BoundedView:
        if Auth.is_logged_as(ADMIN):
            return HomeAdminView()
        elif Auth.is_logged_as(OPERATORE):
            return HomeOperatoreView()
        elif Auth.is_logged_as(UTENTE):
            return HomeUtenteView()
        else:
            return HomeGuestView()
