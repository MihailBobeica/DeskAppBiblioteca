from abstract import BoundedView
from utils.context import *


class LibroComponentFactory:
    @staticmethod
    def create_libro_component(catalog: BoundedView, context: str, data: dict[str, object]) -> BoundedView:
        from view.component.libro import LibroComponentGuest, LibroComponentUtente, LibroPrenotatoComponent

        if context == CONTEXT_CATALOGO_LIBRI_GUEST:
            return LibroComponentGuest(catalog, data)
        elif context == CONTEXT_CATALOGO_LIBRI_UTENTE:
            return LibroComponentUtente(catalog, data)
        elif context == CONTEXT_CATALOGO_PRENOTAZIONI_LIBRI:
            return LibroPrenotatoComponent(catalog, data)
        else:
            raise ValueError("Invalid libro component type")
