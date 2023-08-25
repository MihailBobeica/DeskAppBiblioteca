from abc import ABC, abstractmethod
from enum import Enum


class Factory(ABC):
    @abstractmethod
    def create(self, key: Enum):
        ...
