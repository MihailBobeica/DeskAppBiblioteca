# TODO: da spostare nel model


from abstract.controller import Controller
from database import PrenotazioneAula, PrenotazionePosto, Session
from model.prenotazione_posto import prenotazione_posto
from model.prenotazione_aula import prenotazione_aula
from utils.auth import Auth


class PrenotazioneController(Controller):
    def __init__(self):
        super().__init__()  # Chiamata al costruttore della classe padre

        # Configura i modelli per le prenotazioni
        self.prenotazione_aula_model = prenotazione_aula()
        self.prenotazione_posto_model = prenotazione_posto()

    def crea_prenotazione_aula(self, aula, data, utente_id, durata, ora_inizio, ora_fine):
        db_session = Session()
        prenotazione_aula = PrenotazioneAula(
            codice_aula=aula,
            data_prenotazione=data,
            codice_utente=utente_id,
            durata=durata,
            ora_inizio=ora_inizio,
            ora_fine=ora_fine
        )
        db_session.add(prenotazione_aula)
        db_session.commit()
        db_session.close()

    def crea_prenotazione_posto(self, posto, data, utente_id, durata, ora_inizio, ora_fine):
        db_session = Session()
        prenotazione_posto = PrenotazionePosto(
            codice_posto=posto,
            data_prenotazione=data,
            codice_utente=utente_id,
            durata=durata,
            ora_inizio=ora_inizio,
            ora_fine=ora_fine
        )
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

    def by_utente(self, codice_utente):
        db_session = Session()
        prenotazioni_utente = db_session.query(PrenotazioneAula).filter_by(codice_utente=codice_utente).all()
        db_session.close()
        return prenotazioni_utente

    def search_by_utente(self, utente_id):
        db_session = Session()
        prenotazioni_utente = db_session.query(PrenotazionePosto).filter_by(codice_utente=utente_id).all()
        db_session.close()
        return prenotazioni_utente

    def get_username_utente_loggato(self):
        return Auth.user.username if Auth.user else None
