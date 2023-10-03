import threading
import time
from datetime import datetime

from PySide6.QtWidgets import QMessageBox

from abstract import Controller
from model.prenotazioni_posti import ModelPrenotazioniPosti
from utils.auth import auth
from utils.strings import *
from view.operatore.conferma_posto import ConfermaPostoView
from view.utente.posti_prenotati import PostiPrenotatiView
from view.utente.scegli_aula import ScegliAulaView
from view.utente.scegli_posto_singolo import ScegliPostoSingoloView
from view.utente.scegli_quando import ScegliQuandoView


class ControllerPosti(Controller):
    def __init__(self,
                 model_prenotazioni_posti: ModelPrenotazioniPosti):
        self.model_prenotazioni_posti = model_prenotazioni_posti
        self.flag_thread_exit = threading.Event()
        self.thread_cancella_prenotazioni_posti_non_attivate_in_tempo = threading.Thread(
            target=self.cancella_prenotazioni_posti_non_attivate_in_tempo
        )
        self.thread_cancella_prenotazioni_posti_non_attivate_in_tempo.start()

        # cancella le prenotazioni posti scadute
        self.model_prenotazioni_posti.cancella_prenotazioni_posti_scadute()
        super().__init__()

    def prenota_aula(self, codice_aula: str, ora_inizio: datetime, ora_fine: datetime):
        self.model_prenotazioni_posti.crea_prenotazione_aula(auth.user,
                                                             codice_aula,
                                                             ora_inizio,
                                                             ora_fine)
        self.alert(title=ALERT_TITLE_PRENOTAZIONE_AULA,
                   message=ALERT_MESSAGE_PRENOTAZIONE_AULA.format(codice_aula))
        self.redirect(PostiPrenotatiView())

    def prenota_posto_singolo(self, codice_posto_singolo: str, ora_inizio: datetime, ora_fine: datetime):
        self.model_prenotazioni_posti.crea_prenotazione_posto_singolo(auth.user,
                                                                      codice_posto_singolo,
                                                                      ora_inizio,
                                                                      ora_fine)
        self.alert(title=ALERT_TITLE_PRENOTAZIONE_POSTO_SINGOLO,
                   message=ALERT_MESSAGE_PRENOTAZIONE_POSTO_SINGOLO.format(codice_posto_singolo))
        self.redirect(PostiPrenotatiView())

    def scegli_aula(self, metodo: str, ora_inizio: datetime, ora_fine: datetime):
        has_prenotazione_in_fascia_oraria = self.model_prenotazioni_posti.has_prenotazione_in_fascia_oraria(auth.user,
                                                                                                            ora_inizio,
                                                                                                            ora_fine)
        if has_prenotazione_in_fascia_oraria:
            self.alert(title=ALERT_TITLE_PRENOTAZIONE_POSTO,
                       message=ALERT_MESSAGE_PRENOTAZIONE_POSTO_FASCIA_ORARIA)
            self.redirect(ScegliQuandoView(metodo))
        else:
            self.redirect(ScegliAulaView(metodo, ora_inizio, ora_fine))

    def scegli_posto_singolo(self, codice_aula: str, ora_inizio: datetime, ora_fine: datetime):
        self.redirect(ScegliPostoSingoloView(codice_aula, ora_inizio, ora_fine))

    def cancella_prenotazione_posto_singolo(self, id_prenotazione_posto_singolo: int):
        response = self.confirm(title=CONFIRM_TITLE_CANCELLA_PRENOTAZIONE_POSTO,
                                message=CONFIRM_MESSAGE_CANCELLA_PRENOTAZIONE_POSTO)
        if response == QMessageBox.StandardButton.Yes:
            self.model_prenotazioni_posti.cancella_prenotazione_posto_singolo(id_prenotazione_posto_singolo)
            self.redirect(PostiPrenotatiView())

    def cancella_prenotazione_aula(self, id_prenotazione_aula: int):
        response = self.confirm(title=CONFIRM_TITLE_CANCELLA_PRENOTAZIONE_POSTO,
                                message=CONFIRM_MESSAGE_CANCELLA_PRENOTAZIONE_POSTO)
        if response == QMessageBox.StandardButton.Yes:
            self.model_prenotazioni_posti.cancella_prenotazione_aula(id_prenotazione_aula)
            self.redirect(PostiPrenotatiView())

    def registra_prenotazione_posto_singolo(self, id_prenotazione: int, view: ConfermaPostoView):
        response = self.confirm(title=CONFIRM_TITLE_ATTIVA_PRENOTAZIONE_POSTO,
                                message=CONFIRM_MESSAGE_ATTIVA_PRENOTAZIONE_POSTO)
        if response == QMessageBox.StandardButton.Yes:
            self.model_prenotazioni_posti.attiva_prenotazione_posto_singolo(id_prenotazione)

            view.search(view.searchbar.text())

    def registra_prenotazione_aula(self, id_prenotazione: int, view: ConfermaPostoView):
        response = self.confirm(title=CONFIRM_TITLE_ATTIVA_PRENOTAZIONE_POSTO,
                                message=CONFIRM_MESSAGE_ATTIVA_PRENOTAZIONE_POSTO)
        if response == QMessageBox.StandardButton.Yes:
            self.model_prenotazioni_posti.attiva_prenotazione_aula(id_prenotazione)

            view.search(view.searchbar.text())

    def cancella_prenotazioni_posti_non_attivate_in_tempo(self):
        while not self.flag_thread_exit.is_set():
            # print(f"{datetime.now()}: esecuzione thread cancella prenotazioni posti non attivate in tempo ...")
            self.model_prenotazioni_posti.cancella_prenotazioni_posti_non_attivate_in_tempo()
            time.sleep(1)

    def _fill_view_scegli_aula(self, view: ScegliAulaView):
        if view.metodo == "posto_singolo":
            aule = self.model_prenotazioni_posti.get_aule()
            for aula in aule:
                view.add_aula(aula.nome)
        elif view.metodo == "aula":
            aule_disponibili = self.model_prenotazioni_posti.get_aule_disponibili(view.ora_inizio, view.ora_fine)
            for aula in aule_disponibili:
                view.add_aula(aula.nome)
        else:
            raise ValueError("metodo view scegli aula errato!")

    def _fill_view_scegli_posto_singolo(self, view: ScegliPostoSingoloView):
        posti_disponibili = self.model_prenotazioni_posti.get_posti_disponibili(view.codice_aula, view.ora_inizio,
                                                                                view.ora_fine)
        for posto in posti_disponibili:
            view.add_posto_singolo(posto.nome)

    def _fill_table_posti_prenotati(self, view: PostiPrenotatiView):
        prenotazioni_posti_singoli = self.model_prenotazioni_posti.posti_singoli_by_username(auth.user.username)
        prenotazioni_aule = self.model_prenotazioni_posti.aule_by_username(auth.user.username)
        for pps in prenotazioni_posti_singoli:
            view.add_row_posti_singoli(pps.id,
                                       pps.ora_inizio,
                                       pps.ora_fine,
                                       pps.codice_posto)
        for pa in prenotazioni_aule:
            view.add_row_aule(pa.id,
                              pa.ora_inizio,
                              pa.ora_fine,
                              pa.codice_aula)

    def _fill_view_conferma_posto(self, view: ConfermaPostoView, text: str):
        # utenti con prenotazioni posti singoli oggi
        utenti_posti_singoli_oggi = self.model_prenotazioni_posti.get_utenti_con_prenotazioni_posti_singoli_oggi(text)
        for utente in utenti_posti_singoli_oggi:
            posti_singoli_oggi = self.model_prenotazioni_posti.get_prenotazioni_posti_singoli_oggi_by_utente(utente)
            dati = [{"metodo": "posto_singolo",
                     "id_prenotazione": prenotazione_posto_singolo.id,
                     "codice": prenotazione_posto_singolo.codice_posto,
                     "ora_inizio": prenotazione_posto_singolo.ora_inizio,
                     "ora_fine": prenotazione_posto_singolo.ora_fine}
                    for prenotazione_posto_singolo in posti_singoli_oggi]
            view.add_dati(utente.username, utente.nome, utente.cognome, dati)

        # utenti con prenotazioni aule oggi
        utenti_aule_oggi = self.model_prenotazioni_posti.get_utenti_con_prenotazioni_aule_oggi(text)
        for utente in utenti_aule_oggi:
            aule_oggi = self.model_prenotazioni_posti.get_prenotazioni_aule_oggi_by_utente(utente)
            dati = [{"metodo": "aula",
                     "id_prenotazione": prenotazione_aula.id,
                     "codice": prenotazione_aula.codice_aula,
                     "ora_inizio": prenotazione_aula.ora_inizio,
                     "ora_fine": prenotazione_aula.ora_fine}
                    for prenotazione_aula in aule_oggi]
            view.add_dati(utente.username, utente.nome, utente.cognome, dati)
