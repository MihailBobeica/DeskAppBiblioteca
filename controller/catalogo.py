from typing import Optional

from abstract import Controller, BoundedModel
from model.libro import Libro
from view.component.catalogo import CatalogoComponent


class CatalogoController(Controller):
    def __init__(self, models: Optional[dict[str, BoundedModel]] = None):
        super().__init__(models=models)

    def receive_message(self, message: str, data: Optional[dict] = None) -> None:
        if message == "search":
            catalogo: CatalogoComponent = data["catalogo"]
            text = data["text"]
            model_libri: Libro = self.models["libri"]
            db_libri = catalogo.cerca_libri_strategy.search(model_libri, text)
            catalogo.load_grid(db_libri)
