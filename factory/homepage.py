from typing import Optional, Type

from abstract import BoundedView, Factory
from utils.key import KeyAuth


class HomepageFactory(Factory):
    def __init__(self, displayed_view: Optional[BoundedView] = None):
        self.displayed_view = displayed_view

        super().__init__()

        from view.homepage import HomeAdminView
        from view.homepage import HomeOperatoreView
        from view.homepage import HomeUtenteView
        from view.homepage import HomeGuestView

        self.type: dict[KeyAuth, Type[BoundedView]] = dict()

        self.type[KeyAuth.ADMIN] = HomeAdminView
        self.type[KeyAuth.OPERATORE] = HomeOperatoreView
        self.type[KeyAuth.UTENTE] = HomeUtenteView
        self.type[KeyAuth.GUEST] = HomeGuestView

    def create(self, key: KeyAuth) -> Optional[BoundedView]:
        homepage: Type[BoundedView] = self.type.get(key)
        if self.displayed_view:
            if isinstance(self.displayed_view, homepage):
                return None
        return homepage()
