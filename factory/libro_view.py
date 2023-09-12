from typing import Type

from abstract import Factory
from database import BoundedDbModel
from utils.key import KeyAuth, KeyDb
from view.scaffold import LibroViewScaffold


class LibroViewFactory(Factory):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        self.data = data

        super().__init__()

        from view.libro import LibroViewGuest
        from view.libro import LibroViewUtente

        self.type: dict[KeyAuth, Type[LibroViewScaffold]] = dict()

        self.type[KeyAuth.GUEST] = LibroViewGuest
        self.type[KeyAuth.UTENTE] = LibroViewUtente

    def create(self, key: KeyAuth) -> LibroViewScaffold:
        libro_view = self.type.get(key)
        if libro_view:
            return libro_view(data=self.data)
        raise ValueError("Invalid libro view type")
