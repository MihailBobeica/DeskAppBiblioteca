from database import BoundedDbModel
from utils.key import KeyDb
from view.component import CatalogoComponent
from view.scaffold.libro import LibroScaffold


class LibroComponentScaffold(LibroScaffold):
    def __init__(self, catalogo: CatalogoComponent, data: dict[KeyDb, BoundedDbModel]):
        super().__init__(catalogo=catalogo,
                         data=data,
                         box_size=(400, 240),
                         fullscreen=False)
