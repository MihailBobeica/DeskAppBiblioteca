import threading
from datetime import timedelta, datetime
from utils.backend import POSTI_PER_AULA

from sqlalchemy import null
from sqlalchemy.orm import session
from sqlalchemy import and_

from abstract.controller import Controller
from database import PrenotazioneAula, PrenotazionePosto, Session, Aula, Posto
from model.prenotazione_posto import prenotazione_posto
from model.prenotazione_aula import prenotazione_aula
from utils.auth import auth


class PrenotazioneController(Controller):
    def __init__(self):
        super().__init__()  # Chiamata al costruttore della classe padre

        # Configura i modelli per le prenotazioni
        self.prenotazione_aula_model = prenotazione_aula()
        self.prenotazione_posto_model = prenotazione_posto()

        # Avvia il thread per la cancellazione delle prenotazioni scadute senza ora_attivazione
        thread = threading.Thread(target=self.cancella_prenotazioni_scadute_thread)
        thread.start()

        # Avvia il thread per la cancellazione delle prenotazioni scadute in base all'ora di fine
        thread_ora_fine = threading.Thread(target=self.cancella_prenotazioni_scadute_per_ora_fine)
        thread_ora_fine.start()

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

    def get_all_prenotazioni_aula_senza_attivazione(self):
        db_session = Session()
        prenotazioni_aula_senza_attivazione = db_session.query(PrenotazioneAula).filter(
            PrenotazioneAula.ora_attivazione == null()).all()
        db_session.close()
        return prenotazioni_aula_senza_attivazione

    def get_all_prenotazioni_posto_senza_attivazione(self):
        db_session = Session()
        prenotazioni_posto_senza_attivazione = db_session.query(PrenotazionePosto).filter(
            PrenotazionePosto.ora_attivazione == null()).all()
        db_session.close()
        return prenotazioni_posto_senza_attivazione

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
        return auth.user.username if auth.user else None

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

            # Intervallo di 30 minuto
            intervallo = timedelta(minutes=30)

            # Attendi l'intervallo prima di eseguire il controllo successivo
            threading.Event().wait(intervallo.total_seconds())

    def cancella_prenotazioni_scadute_senza_ora_attivazione(self):
        data_limite = datetime.now() - timedelta(minutes=30)

        db_session = Session()

        # Cancellazione delle prenotazioni delle aule
        prenotazioni_aula_da_cancellare = db_session.query(PrenotazioneAula).filter_by(ora_attivazione=None).filter(
            PrenotazioneAula.data_prenotazione <= data_limite
        ).all()

        for prenotazione_aula in prenotazioni_aula_da_cancellare:
            data_inizio_aula = prenotazione_aula.ora_inizio
            minuti_trascorsi_aula = (datetime.now() - data_inizio_aula).total_seconds() / 60

            # Se sono trascorsi almeno 30 minuto dalla data di inizio, cancella la prenotazione
            if minuti_trascorsi_aula >= 30:
                db_session.delete(prenotazione_aula)

        # Cancellazione delle prenotazioni dei posti
        prenotazioni_posto_da_cancellare = db_session.query(PrenotazionePosto).filter_by(ora_attivazione=None).filter(
            PrenotazionePosto.data_prenotazione <= data_limite
        ).all()

        for prenotazione_posto in prenotazioni_posto_da_cancellare:
            data_inizio_posto = prenotazione_posto.ora_inizio
            minuti_trascorsi_posto = (datetime.now() - data_inizio_posto).total_seconds() / 60

            # Se sono trascorsi almeno 30 minuto dalla data di inizio, cancella la prenotazione
            if minuti_trascorsi_posto >= 30:
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



    def cancella_prenotazioni_scadute_per_ora_fine(self):
        db_session = Session()

        # Cancellazione delle prenotazioni delle aule in base all'ora di fine
        prenotazioni_aula_scadute = db_session.query(PrenotazioneAula).filter(
            PrenotazioneAula.ora_fine <= datetime.now()
        ).all()

        for prenotazione_aula in prenotazioni_aula_scadute:
            db_session.delete(prenotazione_aula)

        # Cancellazione delle prenotazioni dei posti in base all'ora di fine
        prenotazioni_posto_scadute = db_session.query(PrenotazionePosto).filter(
            PrenotazionePosto.ora_fine <= datetime.now()
        ).all()

        for prenotazione_posto in prenotazioni_posto_scadute:
            db_session.delete(prenotazione_posto)

        db_session.commit()
        db_session.close()

    # def is_aula_disponibile(self,ora_inizio, ora_fine):
    #     # Interroga il database per ottenere le prenotazioni sovrapposte
    #     prenotazioni_sovrapposte = session.query(PrenotazioneAula).filter(
    #         and_(
    #             PrenotazioneAula.data_prenotazione <= ora_inizio,
    #             PrenotazioneAula.ora_fine >= ora_fine
    #         )
    #     ).all()
    #
    #     # Ottieni l'elenco degli id delle aule prenotate in modo da poter escluderle dalle aule disponibili
    #     id_aule_prenotate = [prenotazione.codice_aula for prenotazione in prenotazioni_sovrapposte]
    #
    #     # Ottieni l'elenco delle aule disponibili escludendo quelle già prenotate
    #     aule_disponibili = session.query(Aula).filter(Aula.id.notin_(id_aule_prenotate)).all()
    #
    #     return aule_disponibili

    def has_prenotazione_in_fascia_oraria(self,username, data_prenotazione, ora_inizio, ora_fine):
        db_session = Session()

        # Controlla se esistono prenotazioni sovrapposte per l'utente nella data specificata
        prenotazioni_esistenti_aula = db_session.query(PrenotazioneAula).filter(
            and_(
                PrenotazioneAula.codice_utente == username,
                PrenotazioneAula.data_prenotazione == data_prenotazione,
                PrenotazioneAula.ora_fine > ora_inizio,
                PrenotazioneAula.ora_inizio < ora_fine
            )
        ).all()

        prenotazioni_esistentia_posto = db_session.query(PrenotazionePosto).filter(
            and_(
                PrenotazionePosto.codice_utente == username,
                PrenotazionePosto.data_prenotazione == data_prenotazione,
                PrenotazionePosto.ora_fine > ora_inizio,
                PrenotazionePosto.ora_inizio < ora_fine
            )
        ).all()

        db_session.close()
        return prenotazioni_esistentia_posto+prenotazioni_esistenti_aula

        # def modifica_prenotazione_data(self, id_prenotazione, posto, aula, data, utente_id, durata, ora_inizio, ora_fine):
        #db_session = Session()

        # # Cerca la prenotazione esistente per l'ID specificato
        # prenotazione_posto = db_session.query(PrenotazionePosto).filter_by(id=id_prenotazione).first()
        # prenotazione_aula = db_session.query(PrenotazioneAula).filter_by(id=id_prenotazione).first()

        #if prenotazione_posto:
        #   # Modifica i campi della prenotazione del posto
        #  prenotazione_posto.codice_posto = posto
        #  prenotazione_posto.data_prenotazione = data
        # prenotazione_posto.codice_utente = utente_id
        # prenotazione_posto.durata = durata
        #  prenotazione_posto.ora_inizio = ora_inizio
        #  prenotazione_posto.ora_fine = ora_fine

        # if prenotazione_aula:
        #  # Modifica i campi della prenotazione dell'aula
        #  prenotazione_aula.codice_aula = aula
        #  prenotazione_aula.data_prenotazione = data
        # prenotazione_aula.codice_utente = utente_id
        # prenotazione_aula.durata = durata
        #  prenotazione_aula.ora_inizio = ora_inizio
        #  prenotazione_aula.ora_fine = ora_fine

        # db_session.commit()
        # db_session.close()

    def get_all_aule(self):
        db_session = Session()
        aule = db_session.query(Aula).all()
        db_session.close()
        return aule


    def is_posto_disponibile(self,nome_aula, data_prenotazione, ora_inizio, ora_fine):
        db_session = Session()

        # Ottieni tutti i posti
        # tutti_posti = db_session.query(Posto).filter_by(aula=nome_aula).limit(POSTI_PER_AULA).all()
        tutti_posti = db_session.query(Posto).filter_by(aula=nome_aula).all()


        # Controlla quali posti sono disponibili nella fascia oraria specificata
        posti_disponibili = []
        for posto in tutti_posti:
            prenotazioni_posto = db_session.query(PrenotazionePosto).filter(
                and_(
                    PrenotazionePosto.codice_posto == posto.nome,
                    # PrenotazionePosto.data_prenotazione == data_prenotazione,
                    PrenotazionePosto.ora_fine >= ora_inizio,
                    PrenotazionePosto.ora_inizio <= ora_fine
                )
            ).all()
            if not prenotazioni_posto:
                posti_disponibili.append(posto)

        db_session.close()
        return posti_disponibili

    def is_aula_disponibile(self, data_prenotazione, ora_inizio, ora_fine):
        db_session = Session()

        # Ottieni tutte le aule
        tutte_aule = db_session.query(Aula).all()

        # Controlla quali aule sono disponibili nella fascia oraria specificata
        aule_disponibili = []
        for aula in tutte_aule:
            prenotazioni_aula = db_session.query(PrenotazioneAula).filter(
                and_(
                    PrenotazioneAula.codice_aula == aula.nome,
                    # PrenotazioneAula.data_prenotazione == data_prenotazione,
                    PrenotazioneAula.ora_fine >= ora_inizio,
                    PrenotazioneAula.ora_inizio <= ora_fine
                )
            ).all()

            if not prenotazioni_aula:
                # aule_disponibili.append(aula)

                posti_aula = db_session.query(Posto).filter(Posto.aula == aula.nome).all()
                posti_disponibili = []
                for posto in posti_aula:
                    prenotazioni_posto = db_session.query(PrenotazionePosto).filter(
                        and_(
                            PrenotazionePosto.codice_posto == posto.nome,
                            # PrenotazionePosto.data_prenotazione == data_prenotazione,
                            PrenotazionePosto.ora_fine >= ora_inizio,
                            PrenotazionePosto.ora_inizio <= ora_fine
                        )
                    ).all()
                    if not prenotazioni_posto:
                        posti_disponibili.append(posto)

                if len(posti_disponibili) == len(posti_aula):
                    aule_disponibili.append(aula)

        db_session.close()
        return aule_disponibili

