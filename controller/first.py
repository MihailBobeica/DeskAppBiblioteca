from abstract.controller import Controller
from view.first import FirstView


class FirstController(Controller):
    def __init__(self):
        super().__init__()

        self.redirect(FirstView())
