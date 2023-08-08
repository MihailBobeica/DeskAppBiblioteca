
from controller import LoginController, LogoutController, CatalogoController, AdminController, gestione_operatore ,gestione_libri, gestione_utenti
from database.seed import UTENTI, LIBRI, AULE, POSTI, PRESTITI
from model import PrenotazioneLibro
from database.seed import UTENTI, LIBRI, AULE, POSTI, PRESTITI, PRENOTAZIONI_AULE
from model.aula import Aula
from model.libro import Libro
from model.posto import Posto
from model.utente import Utente
from model.prestito import Prestito
from model.prenotazione_aula import prenotazione_aula
from view.homepage import HomeGuestView
from view.main import MainWindow

# instantiate the main window
main_window = MainWindow()

# instantiate all the models
model_utente = Utente()
model_libro = Libro()
model_aula = Aula()
model_posto = Posto()
model_prenotazione_aula = prenotazione_aula()
model_prenotazione_libro = PrenotazioneLibro()

# seeding
model_utente.seed_db(UTENTI)

model_libro.seed_db(LIBRI)
model_aula.seed_db(AULE)
model_posto.seed_db(POSTI)
model_prenotazione_aula.seed_db(PRENOTAZIONI_AULE)
# instantiate all controllers
controller_catalogo = CatalogoController({"libri": model_libro,
                                          "prenotazioni_libri": model_prenotazione_libro})
controller_login = LoginController({"utente": model_utente})
controller_logout = LogoutController()
controller_gestione_operatori = AdminController.Gestione_Op_Controller()
controller_crud_operatore = gestione_operatore.CRUD_operatore()
controller_gestione_libri = gestione_libri.GestioneLibriController()
controller_gestione_utenti = gestione_utenti.GestioneUtentiController()

main_window.set_view(HomeGuestView())
