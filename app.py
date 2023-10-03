from controller import LoginController, LogoutController, CatalogoController, gestione_operatore, \
    gestione_utenti, statistiche, prenotazioni_libri, prestiti, ControllerLibriOsservati, \
    ControllerPrenotazioniLibri, ControllerPosti
from controller.libri import ControllerLibri
from controller.notifica import ControllerNotifica
from controller.operatori import ControllerOperatori
from controller.prestiti import ControllerPrestiti
from controller.router import RouterController
from controller.sanzioni import ControllerSanzioni
from controller.statistiche import StatisticheController
from model import ModelLibriOsservati, ModelUsers
from model import ModelPrenotazioniLibri
from database.seed import *
from model.aule import ModelAule
from model.libri import ModelLibri
from model.operatori import ModelOperatori
from model.posti import ModelPosti
from model.prenotazioni_posti import ModelPrenotazioniPosti
from model.sanzioni import ModelSanzioni
from model.utenti import ModelUtenti
from model.prestiti import ModelPrestiti
from model.prenotazione_aula import prenotazione_aula
from view.homepage import HomeGuestView
from view.main import MainWindow
from model.prestiti import ModelPrestiti
from model.OperatoreModel import OperatoreModel

# instantiate the main window
main_window = MainWindow()

# instantiate all the models
model_users = ModelUsers()
model_utenti = ModelUtenti()
model_libri = ModelLibri()
model_libri_osservati = ModelLibriOsservati()
model_aule = ModelAule()
model_posti = ModelPosti()
model_prenotazione_aula = prenotazione_aula()
model_prenotazioni_libri = ModelPrenotazioniLibri()
model_prestiti = ModelPrestiti()
model_sanzioni = ModelSanzioni()
model_operatore = OperatoreModel()
model_prenotazioni_posti = ModelPrenotazioniPosti()
model_operatori = ModelOperatori()

# seeding
model_users.seed_db(UTENTI)
model_libri.seed_db(LIBRI)
model_aule.seed_db(AULE)
model_posti.seed_db(POSTI)
model_prestiti.seed_db(PRESTITI)
model_prenotazioni_libri.seed_db(PRENOTAZIONI_LIBRI)
# model_prenotazione_aula.seed_db(PRENOTAZIONI_AULE)

# instantiate all controllers
controller_notifica = ControllerNotifica(model_libri_osservati, model_prenotazioni_libri)
controller_libri_osservati = ControllerLibriOsservati(model_libri_osservati, model_prenotazioni_libri, model_prestiti)
controller_libri = ControllerLibri(model_libri)
controller_router = RouterController()
controller_statistiche = StatisticheController()
controller_catalogo = CatalogoController({"libri": model_libri,
                                          "prenotazioni_libri": model_prenotazioni_libri,
                                          "osserva_libri": model_libri_osservati,
                                          "sanzioni": model_sanzioni,
                                          "prestiti": model_prestiti})
controller_login = LoginController(model_users)
controller_logout = LogoutController()
# controller_admin = AdminController.AdminController()
controller_crud_operatore = gestione_operatore.CRUD_operatore()
controller_gestione_utenti = gestione_utenti.GestioneUtentiController()
controller_sanzioni = ControllerSanzioni(model_sanzioni)
controller_prenotazioni_libri = ControllerPrenotazioniLibri(model_prenotazioni_libri, model_sanzioni, model_prestiti)
controller_prestiti = ControllerPrestiti(model_prestiti, model_libri, model_utenti, model_prenotazioni_libri, model_sanzioni)
controller_posti = ControllerPosti(model_prenotazioni_posti)
controller_operatori = ControllerOperatori(model_operatori, model_users)

main_window.set_view(HomeGuestView())
