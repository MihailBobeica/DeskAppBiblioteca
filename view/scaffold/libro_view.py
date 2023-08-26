from database import BoundedDbModel
from utils.key import KeyDb
from view.component import CatalogoComponent
from view.scaffold.libro import LibroScaffold


class LibroViewScaffold(LibroScaffold):
    def __init__(self, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(catalogo=None,
                         data=data,
                         box_size=(640, 480),
                         fullscreen=True)
