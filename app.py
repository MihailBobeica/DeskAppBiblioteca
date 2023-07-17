from controller.first import FirstController
from controller.login import LoginController
from model.utente import Utente
from view.main import MainWindow

# instantiate all models
model_utente = Utente()

# instantiate the main window
main_window = MainWindow()

# instantiate all controllers

controller_first = FirstController({"utente": model_utente}, dict())
controller_login = LoginController({"utente": model_utente}, dict())
