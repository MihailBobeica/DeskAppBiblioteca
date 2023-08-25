from typing import Type, TypedDict

from abstract import factory
from database import BoundedDbModel
from utils import KeyAuth
from view.scaffold import LibroViewScaffold


class KwargsDict(TypedDict):
    data: dict[str, BoundedDbModel]


class LibroViewFactory(Factory):
    def __init__(self):
        super().__init__()

        from view.libro import LibroViewGuest
        from view.libro import LibroViewUtente

        self.type: dict[KeyAuth, Type[LibroViewScaffold]] = dict()

        self.type[KeyAuth.GUEST] = LibroViewGuest
        self.type[KeyAuth.UTENTE] = LibroViewUtente

    def create(self, key: KeyAuth, **kwargs) -> LibroViewScaffold:
        kwargs: KwargsDict
        data = kwargs.get("data")
        libro_view = self.type.get(key)
        if libro_view:
            return libro_view(data=data)
        raise ValueError("Invalid libro view type")


libro_view_factory = LibroViewFactory()
