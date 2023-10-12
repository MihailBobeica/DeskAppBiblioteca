from abc import ABC, abstractmethod
from typing import Any


class Factory(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def create(self, key: Any):
        pass
