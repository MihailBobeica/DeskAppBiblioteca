from abstract import Controller
from database import Libro, PrenotazioneLibro, Prestito
from view.admin.aggiungi_modifica_libro import AggiungiModificaLibroView
from view.admin.aggiungi_modifica_operatore import AggiungiModificaOperatoreView
from view.admin.gestione_libri import GestioneLibriView
from view.admin.gestione_operatori import GestioneOperatoriView
from view.admin.gestione_utenti import GestioneUtentiView
from view.admin.statistiche import StatisticheView
from view.auth import LoginView
from view.catalogo import LibriPrenotatiView, ListaDiOsservazioneView, LibriInPrestitoView
from view.common.cronologia_prestiti import CronologiaPrestitiView
from view.libro import DettagliLibroGuestView, DettagliLibroUtenteView, DettagliPrenotazioneLibroView, \
    DettagliPrestitoView
from view.operatore.conferma_posto import ConfermaPostoView
from view.operatore.registra_prestito import RegistraPrestitoView
from view.operatore.registra_restituzione import RegistraRestituzioneView
from view.utente.posti_prenotati import PostiPrenotatiView
from view.utente.sanzioni import SanzioniView
from view.utente.scegli_quando import ScegliQuandoView


class RouterController(Controller):
    def __init__(self):
        super().__init__()

    def go_to_login(self):
        self.redirect(LoginView())

    def go_to_registra_prestito(self):
        self.redirect(RegistraPrestitoView())

    def go_to_registra_restituzione(self):
        self.redirect(RegistraRestituzioneView())

    def go_to_conferma_posto(self):
        self.redirect(ConfermaPostoView())

    def go_to_aggiungi_libro(self):
        self.redirect(AggiungiModificaLibroView(metodo="aggiungi"))

    def go_to_gestione_libri(self):
        self.redirect(GestioneLibriView())

    def go_to_aggiungi_operatore(self):
        self.redirect(AggiungiModificaOperatoreView(metodo="aggiungi"))

    def go_to_gestione_operatori(self):
        self.redirect(GestioneOperatoriView())

    def go_to_gestione_utenti(self):
        self.redirect(GestioneUtentiView())

    def go_to_statistiche(self):
        self.redirect(StatisticheView())

    def go_to_dettagli_libro_guest(self, libro: Libro):
        self.redirect(DettagliLibroGuestView(libro))

    def go_to_dettagli_libro_utente(self, libro: Libro):
        self.redirect(DettagliLibroUtenteView(libro))

    def go_to_libri_in_prestito(self):
        self.redirect(LibriInPrestitoView())

    def go_to_libri_prenotati(self):
        self.redirect(LibriPrenotatiView())

    def go_to_lista_di_osservazione(self):
        self.redirect(ListaDiOsservazioneView())

    def go_to_dettagli_prenotazione_libro(self, libro: Libro, prenotazione_libro: PrenotazioneLibro):
        self.redirect(DettagliPrenotazioneLibroView(libro, prenotazione_libro))

    def go_to_dettagli_prestito(self, libro: Libro, prestito: Prestito):
        self.redirect(DettagliPrestitoView(libro, prestito))

    def go_to_posti_prenotati(self):
        self.redirect(PostiPrenotatiView())

    def go_to_prenota_posto_singolo(self):
        self.redirect(ScegliQuandoView("posto_singolo"))

    def go_to_prenota_aula(self):
        self.redirect(ScegliQuandoView("aula"))

    def go_to_cronologia(self, id_utente):
        self.redirect(CronologiaPrestitiView(id_utente))

    def go_to_sanzioni(self, id_utente):
        self.redirect(SanzioniView(id_utente))
