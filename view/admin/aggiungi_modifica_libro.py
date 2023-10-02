from typing import Optional

from abstract import View
from database import Libro


class AggiungiModificaLibroView(View):
    def create_layout(self) -> None:
        pass

    def __init__(self, metodo: str, libro: Optional[Libro] = None):
        self.metodo = metodo
        self.libro = libro
        super().__init__()
