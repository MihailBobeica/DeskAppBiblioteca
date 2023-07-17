from abstract.view import View


class Controller:
    def receive_message(self, message: str, data: dict) -> None:
        pass

    def __init__(self):
        from app import main_window
        self.main_window = main_window

    def redirect(self, view: View) -> None:
        self.main_window.set_view(view)
