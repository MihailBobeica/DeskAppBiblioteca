class Controller:
    def __init__(self):
        from app import main_window
        self.main_window = main_window

    def receive_message(self, message: str, data: dict):
        pass
