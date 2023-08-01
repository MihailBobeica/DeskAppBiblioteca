import threading
from datetime import timedelta, datetime

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

        # Avvia il thread per la cancellazione delle prenotazioni scadute senza ora_attivazione
        thread = threading.Thread(target=self.cancella_prenotazioni_scadute_thread)
        thread.start()

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

    def get_all_prenotazioni_aula(self):
        db_session = Session()
        prenotazioni_aula = db_session.query(PrenotazioneAula).all()
        db_session.close()
        return prenotazioni_aula

    def get_all_prenotazioni_posto(self):
        db_session = Session()
        prenotazioni_posto = db_session.query(PrenotazionePosto).all()
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

    def cancella_prenotazione_aula(self, prenotazione_id):
        db_session = Session()
        prenotazione_aula = db_session.query(PrenotazioneAula).get(prenotazione_id)
        if prenotazione_aula:
            db_session.delete(prenotazione_aula)
            db_session.commit()
        db_session.close()

    def cancella_prenotazione_posto(self, prenotazione_id):
        db_session = Session()
        prenotazione_posto = db_session.query(PrenotazionePosto).get(prenotazione_id)
        if prenotazione_posto:
            db_session.delete(prenotazione_posto)
            db_session.commit()
        db_session.close()

    def cancella_prenotazioni_scadute_thread(self):
        while True:
            self.cancella_prenotazioni_scadute_senza_ora_attivazione()

            # Intervallo di 1 minuto
            intervallo = timedelta(minutes=1)

            # Attendi l'intervallo prima di eseguire il controllo successivo
            threading.Event().wait(intervallo.total_seconds())

    def cancella_prenotazioni_scadute_senza_ora_attivazione(self):
        data_limite = datetime.now() - timedelta(minutes=1)

        db_session = Session()

        # Cancellazione delle prenotazioni delle aule
        prenotazioni_aula_da_cancellare = db_session.query(PrenotazioneAula).filter_by(ora_attivazione=None).filter(
            PrenotazioneAula.data_prenotazione <= data_limite
        ).all()

        for prenotazione_aula in prenotazioni_aula_da_cancellare:
            data_inizio_aula = prenotazione_aula.ora_inizio
            minuti_trascorsi_aula = (datetime.now() - data_inizio_aula).total_seconds() / 60

            # Se sono trascorsi almeno 1 minuto dalla data di inizio, cancella la prenotazione
            if minuti_trascorsi_aula >= 1:
                db_session.delete(prenotazione_aula)

        # Cancellazione delle prenotazioni dei posti
        prenotazioni_posto_da_cancellare = db_session.query(PrenotazionePosto).filter_by(ora_attivazione=None).filter(
            PrenotazionePosto.data_prenotazione <= data_limite
        ).all()

        for prenotazione_posto in prenotazioni_posto_da_cancellare:
            data_inizio_posto = prenotazione_posto.ora_inizio
            minuti_trascorsi_posto = (datetime.now() - data_inizio_posto).total_seconds() / 60

            # Se sono trascorsi almeno 1 minuto dalla data di inizio, cancella la prenotazione
            if minuti_trascorsi_posto >= 1:
                db_session.delete(prenotazione_posto)

        db_session.commit()
        db_session.close()

    def conferma_prenotazione_aula(self, prenotazione_id):
            db_session = Session()
            prenotazione_aula = db_session.query(PrenotazioneAula).get(prenotazione_id)
            if prenotazione_aula:
                prenotazione_aula.ora_attivazione = datetime.now()
                db_session.commit()
            db_session.close()

    def conferma_prenotazione_posto(self, prenotazione_id):
            db_session = Session()
            prenotazione_posto = db_session.query(PrenotazionePosto).get(prenotazione_id)
            if prenotazione_posto:
                prenotazione_posto.ora_attivazione = datetime.now()
                db_session.commit()
            db_session.close()
