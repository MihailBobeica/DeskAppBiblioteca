from abc import ABC, abstractmethod
from enum import Enum


class Factory(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def create(self, key: Enum):
        pass
