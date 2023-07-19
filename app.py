from controller.first import FirstController
from controller.login import LoginController
from controller.logout import LogoutController
from database.seed import UTENTI
from model.utente import Utente
from view.main import MainWindow

# instantiate the main window
main_window = MainWindow()

# instantiate all the models
model_utente = Utente()

# seeding
model_utente.seed_db(UTENTI)

# instantiate all controllers
controller_first = FirstController()
controller_login = LoginController({"utente": model_utente})  # TODO : sistemare il type hinting; priorità minima
controller_logout = LogoutController()
