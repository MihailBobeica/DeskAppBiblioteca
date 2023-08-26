from typing import Type

from abstract import Factory
from database import BoundedDbModel
from utils.key import KeyContext, KeyDb


class LibroComponentFactory(Factory):
    def __init__(self, catalogo, data: dict[KeyDb, BoundedDbModel]):
        self.catalogo = catalogo
        self.data = data

        super().__init__()

        from view.scaffold import LibroComponentScaffold
        from view.component.libro import LibroComponentGuest
        from view.component.libro import LibroComponentUtente
        from view.component.libro import LibroPrenotatoComponent

        self.type: dict[KeyContext, Type[LibroComponentScaffold]] = dict()

        self.type[KeyContext.CATALOGO_LIBRI_GUEST] = LibroComponentGuest
        self.type[KeyContext.CATALOGO_LIBRI_UTENTE] = LibroComponentUtente
        self.type[KeyContext.CATALOGO_PRENOTAZIONI_LIBRI] = LibroPrenotatoComponent

    def create(self, key: KeyContext):
        libro_component = self.type.get(key)
        if libro_component:
            return libro_component(catalogo=self.catalogo,
                                   data=self.data)
        raise ValueError("Invalid libro component type")
