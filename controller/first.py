from typing import Dict, Optional

from abstract.controller import Controller
from abstract.model import Model
from abstract.view import View
from view.first import FirstView


class FirstController(Controller):
    def __init__(self, models: Optional[Dict[str, Model]] = None, views: Optional[Dict[str, View]] = None):
        super().__init__(models, views)

        self.main_window.set_view(FirstView())
