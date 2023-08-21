from typing import Optional, TypedDict, Type

from abstract import BoundedView, Factory
from utils import KeyAuth


class KwargsDict(TypedDict):
    displayed_view: Type[BoundedView]


class HomepageFactory(Factory):
    def __init__(self):
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

    def create(self, key: KeyAuth, **kwargs) -> Optional[BoundedView]:
        kwargs: KwargsDict
        displayed_view = kwargs.get("displayed_view")
        homepage: Type[BoundedView] = self.type.get(key)
        if displayed_view:
            if isinstance(type(displayed_view), homepage):
                return None
        return homepage()


homepage_factory = HomepageFactory()
