from datetime import datetime

from PySide6.QtWidgets import QMessageBox

from abstract import Controller
from model.prenotazioni_posti import ModelPrenotazioniPosti
from utils.auth import auth
from utils.strings import *
from view.utente.posti_prenotati import PostiPrenotatiView
from view.utente.scegli_aula import ScegliAulaView
from view.utente.scegli_posto_singolo import ScegliPostoSingoloView
from view.utente.scegli_quando import ScegliQuandoView


class ControllerPosti(Controller):
    def __init__(self,
                 model_prenotazioni_posti: ModelPrenotazioniPosti):
        self.model_prenotazioni_posti = model_prenotazioni_posti
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

    def _fill_view_scegli_aula(self, view: ScegliAulaView):
        aule_disponibili = self.model_prenotazioni_posti.get_aule_disponibili(view.ora_inizio, view.ora_fine)
        for aula in aule_disponibili:
            view.add_aula(aula.nome)

    def _fill_view_scegli_posto_singolo(self, view: ScegliPostoSingoloView):
        posti_disponibili = self.model_prenotazioni_posti.get_posti_disponibili(view.codice_aula, view.ora_inizio, view.ora_fine)
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
