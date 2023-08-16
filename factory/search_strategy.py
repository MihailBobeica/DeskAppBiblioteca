from strategy import SearchStrategy, CercaLibriCatalogo, CercaPrenotazioniValide
from utils.context import *


class SearchStrategyFactory:
    @staticmethod
    def create_search_strategy(context: str) -> SearchStrategy:
        if context in [CONTEXT_CATALOGO_LIBRI_GUEST,
                       CONTEXT_CATALOGO_LIBRI_UTENTE,
                       CONTEXT_CATALOGO_LIBRI_OPERATORE,
                       CONTEXT_CATALOGO_LIBRI_ADMIN]:
            return CercaLibriCatalogo()
        elif context == CONTEXT_CATALOGO_PRENOTAZIONI_LIBRI:
            return CercaPrenotazioniValide()
        else:
            raise ValueError("Invalid search strategy type")
