from view.scaffold.libro import DettagliScaffold


class DettagliViewScaffold(DettagliScaffold):
    def __init__(self, **kwargs):
        super().__init__(catalogo=None,
                         dati=kwargs,
                         box_size=(640, 480),
                         fullscreen=True)
