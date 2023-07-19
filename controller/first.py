from typing import Optional, Dict, Type

from abstract.controller import Controller
from abstract.model import Model
from view.first import FirstView


class FirstController(Controller):
    def __init__(self, models: Optional[Dict[str, Type[Model]]] = None):
        super().__init__(models)

        self.redirect(FirstView())
