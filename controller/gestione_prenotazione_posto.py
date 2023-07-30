# TODO: da spostare nel model


from abstract.controller import Controller
from database import PrenotazioneAula, PrenotazionePosto, Session


class PrenotazioneController(Controller):
    def crea_prenotazione_aula(self, aula, data, utente_id):
        db_session = Session()
        prenotazione_aula = PrenotazioneAula(aula=aula, data=data, utente_id=utente_id)
        db_session.add(prenotazione_aula)
        db_session.commit()
        db_session.close()

    def crea_prenotazione_posto(self, posto, data, utente_id):
        db_session = Session()
        prenotazione_posto = PrenotazionePosto(posto=posto, data=data, utente_id=utente_id)
        db_session.add(prenotazione_posto)
        db_session.commit()
        db_session.close()

    def get_prenotazioni_aula(self, n):
        db_session = Session()
        prenotazioni_aula = PrenotazioneAula().get(n)
        db_session.close()
        return prenotazioni_aula

    def get_prenotazioni_posto(self, n):
        db_session = Session()
        prenotazioni_posto = PrenotazionePosto().get(n)
        db_session.close()
        return prenotazioni_posto

    def search_prenotazioni_aula_by_utente(self, utente_id):
        db_session = Session()
        prenotazioni_aula = PrenotazioneAula().search_by_utente(utente_id)
        db_session.close()
        return prenotazioni_aula

    def search_prenotazioni_posto_by_utente(self, utente_id):
        db_session = Session()
        prenotazioni_posto = PrenotazionePosto().search_by_utente(utente_id)
        db_session.close()
        return prenotazioni_posto

    def __init__(self):
        super().__init__()
