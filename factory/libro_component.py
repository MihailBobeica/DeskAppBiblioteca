from typing import Type

from abstract import Factory
from database import BoundedDbModel
from utils.key import KeyContext


class LibroComponentFactory(Factory):
    def __init__(self, catalogo, dati: dict[str, BoundedDbModel]):
        self.catalogo = catalogo
        self.dati = dati

        super().__init__()

        from view.scaffold import LibroComponentScaffold
        from view.component.libro import LibroComponentGuest
        from view.component.libro import LibroComponentUtente
        from view.component.libro import LibroPrenotatoComponent
        from view.component.libro import LibroOsservatoComponent
        from view.component.libro import LibroInPrestitoComponent

        self.type: dict[KeyContext, Type[LibroComponentScaffold]] = dict()

        self.type[KeyContext.CATALOGO_LIBRI_GUEST] = LibroComponentGuest
        self.type[KeyContext.CATALOGO_LIBRI_UTENTE] = LibroComponentUtente
        self.type[KeyContext.CATALOGO_PRENOTAZIONI_LIBRI] = LibroPrenotatoComponent
        self.type[KeyContext.CATALOGO_LIBRI_OSSERVATI] = LibroOsservatoComponent
        self.type[KeyContext.CATALOGO_LIBRI_IN_PRESTITO] = LibroInPrestitoComponent

    def create(self, key: KeyContext):
        libro_component = self.type.get(key)
        if libro_component:
            return libro_component(catalogo=self.catalogo,
                                   dati=self.dati)
        raise ValueError("Invalid libro component type")
