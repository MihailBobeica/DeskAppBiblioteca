from strategy import SearchStrategy, CercaLibriCatalogo, CercaPrenotazioniValide
from utils.backend import *


class SearchStrategyFactory:
    def create_search_strategy(self, context: str) -> SearchStrategy:
        if context in [CONTEXT_CATALOGO_LIBRI_GUEST,
                       CONTEXT_CATALOGO_LIBRI_UTENTE,
                       CONTEXT_CATALOGO_LIBRI_OPERATORE,
                       CONTEXT_CATALOGO_LIBRI_ADMIN]:
            return CercaLibriCatalogo()
        elif context == "":
            return CercaPrenotazioniValide()
        else:
            raise ValueError("Invalid search strategy type")
