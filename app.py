from controller.first import FirstController
from controller.login import LoginController
from controller.logout import LogoutController
from database.seed import UTENTI, LIBRI,AULE,POSTI
from model.libro import Libro
from model.utente import Utente
from view.main import MainWindow
from model.aula import Aula
from model.posto import Posto

# instantiate the main window
main_window = MainWindow()

# instantiate all the models
model_utente = Utente()
model_libro = Libro()
model_aula = Aula()
model_posto = Posto()

# seeding
model_utente.seed_db(UTENTI)
model_libro.seed_db(LIBRI)
model_aula.seed_db(AULE)
model_posto.seed_db(POSTI)

# instantiate all controllers
controller_first = FirstController()
controller_login = LoginController({"utente": model_utente})  # TODO : sistemare il type hinting; priorità minima
controller_logout = LogoutController()
