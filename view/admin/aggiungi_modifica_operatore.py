from typing import Optional

from abstract import View
from database import Operatore


class AggiungiModificaOperatoreView(View):
    def create_layout(self) -> None:
        pass

    def __init__(self, metodo: str, operatore: Optional[Operatore] = None):
        self.metodo = metodo
        self.operatore = operatore
        super().__init__()
