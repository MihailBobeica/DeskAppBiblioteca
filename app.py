from controller import FirstController, LoginController, LogoutController
from database.seed import UTENTI, LIBRI, AULE, POSTI, PRESTITI
from model.aula import Aula
from model.libro import Libro
from model.posto import Posto
from model.utente import Utente
from model.prestito import Prestito
from view.main import MainWindow

# instantiate the main window
main_window = MainWindow()

# instantiate all the models
model_utente = Utente()
model_libro = Libro()
model_aula = Aula()
model_posto = Posto()
model_prestito = Prestito()
# seeding
model_utente.seed_db(UTENTI)

model_libro.seed_db(LIBRI)
model_aula.seed_db(AULE)
model_posto.seed_db(POSTI)
model_prestito.seed_db(PRESTITI)

# instantiate all controllers
controller_first = FirstController()
controller_login = LoginController({"utente": model_utente})
controller_logout = LogoutController()
