from typing import Optional

from abstract import BoundedView
from utils.auth import Auth
from utils.strings import UTENTE, OPERATORE, ADMIN


class HomepageFactory:
    @staticmethod
    def create_homepage(displayed_view: Optional[BoundedView] = None) -> Optional[BoundedView]:
        from view.homepage import HomeAdminView, HomeOperatoreView, HomeUtenteView, HomeGuestView

        # controllo se mi trovo già nella home page
        if displayed_view:
            if any(isinstance(displayed_view, t) for t in [HomeAdminView,
                                                           HomeOperatoreView,
                                                           HomeUtenteView,
                                                           HomeGuestView]):
                return None

        if Auth.is_logged_as(ADMIN):
            return HomeAdminView()
        elif Auth.is_logged_as(OPERATORE):
            return HomeOperatoreView()
        elif Auth.is_logged_as(UTENTE):
            return HomeUtenteView()
        else:
            return HomeGuestView()
