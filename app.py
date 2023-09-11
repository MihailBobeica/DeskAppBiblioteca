
from controller import LoginController, LogoutController, CatalogoController, AdminController, gestione_operatore ,gestione_libri, gestione_utenti, statistiche
from controller.notifica import NotificaController
from controller.router import RouterController
from controller.sanzione import SanzioneController
from controller.statistiche import StatisticheController
from model import LibroOsservato
from model import PrenotazioneLibro
from database.seed import UTENTI, LIBRI, AULE, POSTI, PRESTITI, PRENOTAZIONI_AULE
from model.aula import Aula
from model.libro import Libro
from model.posto import Posto
from model.sanzione import Sanzione
from model.utente import Utente
from model.prestito import Prestito
from model.prenotazione_aula import prenotazione_aula
from view.homepage import HomeGuestView
from view.main import MainWindow
from model.prestito import Prestito

# instantiate the main window
main_window = MainWindow()

# instantiate all the models
model_utente = Utente()
model_libro = Libro()
model_osserva_libro = LibroOsservato()
model_aula = Aula()
model_posto = Posto()
model_prenotazione_aula = prenotazione_aula()
model_prenotazione_libro = PrenotazioneLibro()
model_prestito = Prestito()
model_sanzioni = Sanzione()

# seeding
model_utente.seed_db(UTENTI)

model_libro.seed_db(LIBRI)
model_aula.seed_db(AULE)
model_posto.seed_db(POSTI)
model_prenotazione_aula.seed_db(PRENOTAZIONI_AULE)
model_prestito.seed_db(PRESTITI)

# instantiate all controllers
controller_notifica = NotificaController({"osserva_libri": model_osserva_libro,
                                          "prenotazioni_libri": model_prenotazione_libro})
controller_router = RouterController()
controller_statistiche = StatisticheController()
controller_catalogo = CatalogoController({"libri": model_libro,
                                          "prenotazioni_libri": model_prenotazione_libro,
                                          "osserva_libri": model_osserva_libro,
                                          "sanzioni": model_sanzioni})
controller_login = LoginController({"utente": model_utente})
controller_logout = LogoutController()
controller_gestione_operatori = AdminController.Gestione_Op_Controller()
controller_crud_operatore = gestione_operatore.CRUD_operatore()
controller_gestione_libri = gestione_libri.GestioneLibriController()
controller_gestione_utenti = gestione_utenti.GestioneUtentiController()
controller_sanzione = SanzioneController({"utenti": model_utente,
                                          "prestiti": model_prestito,
                                          "sanzioni": model_sanzioni})

main_window.set_view(HomeGuestView())
