from controller import FirstController, LoginController, LogoutController, CatalogoController
from database.seed import UTENTI, LIBRI, AULE, POSTI
from model.aula import Aula
from model.libro import Libro
from model.posto import Posto
from model.utente import Utente
from view.main import MainWindow

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
controller_catalogo = CatalogoController({"libri": model_libro})
controller_first = FirstController({"libri": model_libro})
controller_login = LoginController({"utente": model_utente})
controller_logout = LogoutController()
