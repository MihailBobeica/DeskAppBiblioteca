from typing import Optional, Dict

from abstract import Controller, BoundedModel
from view.homepage import HomePageView


class FirstController(Controller):
    def __init__(self, models: Optional[Dict[str, BoundedModel]] = None):
        super().__init__(models)

        self.redirect(HomePageView())
