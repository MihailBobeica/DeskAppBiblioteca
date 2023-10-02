from abstract import Controller, BoundedModel
from view.component.catalogo import CatalogoComponent


class CatalogoController(Controller):
    def __init__(self, models: dict[str, BoundedModel]):
        self.models = models
        super().__init__()

    def search(self, text: str, catalogo: CatalogoComponent):
        data_list = catalogo.search_strategy.search(self.models, text)
        catalogo.load_grid(data_list)
