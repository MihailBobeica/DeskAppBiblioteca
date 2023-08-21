from typing import Type, TypedDict

from abstract import Factory
from database import BoundedDbModel
from utils import KeyContext
from view.component import CatalogoComponent
from view.scaffold import LibroComponentScaffold


class KwargsDict(TypedDict):
    catalogo: CatalogoComponent
    data: dict[str, BoundedDbModel]


class LibroComponentFactory(Factory):
    def __init__(self):
        super().__init__()

        from view.component.libro import LibroComponentGuest
        from view.component.libro import LibroComponentUtente
        from view.component.libro import LibroPrenotatoComponent

        self.type: dict[KeyContext, Type[LibroComponentScaffold]] = dict()

        self.type[KeyContext.CATALOGO_LIBRI_GUEST] = LibroComponentGuest
        self.type[KeyContext.CATALOGO_LIBRI_UTENTE] = LibroComponentUtente
        self.type[KeyContext.CATALOGO_PRENOTAZIONI_LIBRI] = LibroPrenotatoComponent

    def create(self, key: KeyContext, **kwargs) -> LibroComponentScaffold:
        kwargs: KwargsDict
        catalogo = kwargs.get("catalogo")
        data = kwargs.get("data")
        libro_component = self.type.get(key)
        if libro_component:
            return libro_component(catalogo=catalogo,
                                   data=data)
        raise ValueError("Invalid libro component type")


libro_component_factory = LibroComponentFactory()
