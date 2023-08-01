from abc import abstractmethod
from typing import Type, TYPE_CHECKING

from utils.backend import is_empty

from model.libro import Libro
from database import Libro as DbLibro
# if TYPE_CHECKING:


class CercaLibriStrategy:
    def __init__(self):
        pass

    @abstractmethod
    def search(self, model: Libro, text: str) -> list[Type[DbLibro]]:
        pass


class CercaLibriCatalogo(CercaLibriStrategy):
    def search(self, model: Libro, text: str) -> list[Type[DbLibro]]:
        if is_empty(text):
            return model.get()
        return model.search(text)

    def __init__(self):
        super().__init__()
