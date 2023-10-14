from controller import *
from database.seed import *
from model import *
from view.homepage import HomeGuestView
from view.main import MainWindow

# instantiate the main window
main_window = MainWindow()

# instantiate all the models
model_users = ModelUsers()
model_utenti = ModelUtenti()
model_libri = ModelLibri()
model_libri_osservati = ModelLibriOsservati()
model_aule = ModelAule()
model_posti = ModelPosti()
model_prenotazioni_libri = ModelPrenotazioniLibri()
model_prestiti = ModelPrestiti()
model_sanzioni = ModelSanzioni()
model_prenotazioni_posti = ModelPrenotazioniPosti()
model_operatori = ModelOperatori()
model_statistiche = ModelStatistiche()

# seeding
model_users.seed_db(UTENTI)
model_libri.seed_db(LIBRI)
model_aule.seed_db(AULE)
model_posti.seed_db(POSTI)
model_prestiti.seed_db(PRESTITI)
model_prenotazioni_libri.seed_db(PRENOTAZIONI_LIBRI)
# model_prenotazione_aula.seed_db(PRENOTAZIONI_AULE)

# instantiate all controllers
controller_utenti = ControllerUtenti(model_utenti)
controller_notifica = ControllerNotifiche(model_libri_osservati,
                                          model_prenotazioni_libri)
controller_libri_osservati = ControllerLibriOsservati(model_libri_osservati,
                                                      model_prenotazioni_libri,
                                                      model_prestiti)
controller_libri = ControllerLibri(model_libri)
controller_router = ControllerRouter(model_libri, model_operatori)
controller_statistiche = ControllerStatistiche(model_statistiche)
controller_catalogo = CatalogoController({"libri": model_libri,
                                          "prenotazioni_libri": model_prenotazioni_libri,
                                          "osserva_libri": model_libri_osservati,
                                          "sanzioni": model_sanzioni,
                                          "prestiti": model_prestiti})
controller_login = LoginController(model_users)
controller_logout = ControllerLogout()
controller_sanzioni = ControllerSanzioni(model_sanzioni)
controller_prenotazioni_libri = ControllerPrenotazioniLibri(model_prenotazioni_libri,
                                                            model_sanzioni,
                                                            model_prestiti)
controller_prestiti = ControllerPrestiti(model_prestiti,
                                         model_libri,
                                         model_utenti,
                                         model_prenotazioni_libri,
                                         model_sanzioni)
controller_posti = ControllerPrenotazioniPosti(model_prenotazioni_posti)
controller_operatori = ControllerOperatori(model_operatori,
                                           model_users)

# go_to_home_guest
main_window.set_view(HomeGuestView())
