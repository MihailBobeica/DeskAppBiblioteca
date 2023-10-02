from database import BoundedDbModel
from view.component import CatalogoComponent
from view.scaffold.libro import DettagliScaffold


class LibroComponentScaffold(DettagliScaffold):
    def __init__(self, catalogo: CatalogoComponent, dati: dict[str, BoundedDbModel]):
        super().__init__(catalogo=catalogo,
                         dati=dati,
                         box_size=(400, 240),
                         fullscreen=False)
