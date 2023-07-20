from typing import Dict

from abstract.model import Model


class Libro(Model):
    def inserisci(self, dati: Dict[str, str]):
        pass

    def __init__(self):
        super().__init__()
