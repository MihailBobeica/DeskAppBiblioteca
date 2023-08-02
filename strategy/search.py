from abc import abstractmethod
from typing import Type

from database import Libro as DbLibro
from model.libro import Libro
from utils.auth import Auth
from utils.backend import is_empty


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


class CercaLibriPrenotati(CercaLibriStrategy):
    def search(self, model: Libro, text: str) -> list[Type[DbLibro]]:
        if is_empty(text):
            return model.get_prenotati(utente=Auth.user)
        return model.search_prenotati(utente=Auth.user,
                                      text=text)

    def __init__(self):
        super().__init__()
