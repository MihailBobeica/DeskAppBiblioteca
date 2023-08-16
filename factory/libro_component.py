from abstract import BoundedView
from utils.context import *
from view.component.libro import LibroComponentGuest, LibroComponentUtente, LibroComponentPrenotazione


class LibroComponentFactory:
    @staticmethod
    def create_libro_component(catalog: BoundedView, context:str, data: dict[str, object]) -> BoundedView:
        if context == CONTEXT_CATALOGO_LIBRI_GUEST:
            return LibroComponentGuest(catalog, context, data)
        elif context == CONTEXT_CATALOGO_LIBRI_UTENTE:
            return LibroComponentUtente(catalog, context, data)
        elif context == CONTEXT_CATALOGO_PRENOTAZIONI_LIBRI:
            return LibroComponentPrenotazione(catalog, context, data)
        else:
            raise ValueError("Invalid libro component type")
