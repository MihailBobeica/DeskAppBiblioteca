from abstract import Factory
from strategy import CercaLibriCatalogo
from strategy import CercaPrenotazioniValide
from strategy import SearchStrategy
from utils import KeyContext


class SearchStrategyFactory(Factory):
    def __init__(self):
        super().__init__()

        self.type: dict[KeyContext, SearchStrategy] = dict()

        self.type[KeyContext.CATALOGO_LIBRI] = CercaLibriCatalogo()
        self.type[KeyContext.CATALOGO_PRENOTAZIONI_LIBRI] = CercaPrenotazioniValide()

    def create(self, key: KeyContext, **kwargs) -> SearchStrategy:
        search_strategy = self.type.get(key)
        if search_strategy:
            return search_strategy
        raise ValueError("Invalid search strategy type")


search_strategy_factory = SearchStrategyFactory()
