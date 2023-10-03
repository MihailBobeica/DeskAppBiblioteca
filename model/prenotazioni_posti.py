from datetime import datetime, timedelta

from sqlalchemy import and_, or_

from abstract import Model
from database import PrenotazionePosto, PrenotazioneAula, Session, Aula, Posto, Utente


class ModelPrenotazioniPosti(Model):
    def inserisci(self, dati: dict[str, str]):
        pass

    def __init__(self):
        super().__init__()

    def posti_singoli_by_username(self, username: str) -> list[PrenotazionePosto]:
        db_session = Session()
        prenotazioni_posti_singoli = db_session.query(PrenotazionePosto).filter(
            PrenotazionePosto.codice_utente == username
        ).all()
        db_session.close()
        return prenotazioni_posti_singoli

    def aule_by_username(self, username: str) -> list[PrenotazioneAula]:
        db_session = Session()
        prenotazioni_aule = db_session.query(PrenotazioneAula).filter(
            PrenotazioneAula.codice_utente == username
        ).all()
        db_session.close()
        return prenotazioni_aule

    def get_aule_disponibili(self, ora_inizio: datetime, ora_fine: datetime) -> list[Aula]:
        db_session = Session()

        # Ottieni tutte le aule
        tutte_aule = db_session.query(Aula).all()

        # Controlla quali aule sono disponibili nella fascia oraria specificata
        aule_disponibili = []
        for aula in tutte_aule:
            prenotazioni_aula = db_session.query(PrenotazioneAula).filter(
                and_(
                    PrenotazioneAula.codice_aula == aula.nome,
                    PrenotazioneAula.ora_fine >= ora_inizio,
                    PrenotazioneAula.ora_inizio <= ora_fine
                )
            ).all()

            if not prenotazioni_aula:
                posti_aula = db_session.query(Posto).filter(Posto.aula == aula.nome).all()
                posti_disponibili = []
                for posto in posti_aula:
                    prenotazioni_posto = db_session.query(PrenotazionePosto).filter(
                        and_(
                            PrenotazionePosto.codice_posto == posto.nome,
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

    def get_posti_disponibili(self, codice_aula: str, ora_inizio: datetime, ora_fine: datetime) -> list[Posto]:
        db_session = Session()

        # Ottieni tutti i posti
        tutti_posti = db_session.query(Posto).filter_by(aula=codice_aula).all()

        # Controlla quali posti sono disponibili nella fascia oraria specificata
        posti_disponibili: list[Posto] = list()
        for posto in tutti_posti:
            prenotazioni_posto = db_session.query(PrenotazionePosto).filter(
                and_(
                    PrenotazionePosto.codice_posto == posto.nome,
                    PrenotazionePosto.ora_fine >= ora_inizio,
                    PrenotazionePosto.ora_inizio <= ora_fine
                )
            ).all()
            if not prenotazioni_posto:
                posti_disponibili.append(posto)

        db_session.close()
        return posti_disponibili

    def crea_prenotazione_aula(self, utente: Utente, codice_aula: str, ora_inizio: datetime, ora_fine: datetime):
        db_session = Session()
        prenotazione_aula = PrenotazioneAula(
            codice_aula=codice_aula,
            data_prenotazione=datetime.now(),
            codice_utente=utente.username,
            ora_inizio=ora_inizio,
            ora_fine=ora_fine
        )
        db_session.add(prenotazione_aula)
        db_session.commit()
        db_session.close()

    def crea_prenotazione_posto_singolo(self, utente: Utente, codice_posto_singolo: str, ora_inizio: datetime,
                                        ora_fine: datetime):
        db_session = Session()
        prenotazione_posto_singolo = PrenotazionePosto(
            codice_posto=codice_posto_singolo,
            data_prenotazione=datetime.now(),
            codice_utente=utente.username,
            ora_inizio=ora_inizio,
            ora_fine=ora_fine
        )
        db_session.add(prenotazione_posto_singolo)
        db_session.commit()
        db_session.close()

    def has_prenotazione_in_fascia_oraria(self, utente: Utente, ora_inizio, ora_fine) -> bool:
        db_session = Session()

        # Controlla se esistono prenotazioni sovrapposte per l'utente nella data specificata
        prenotazioni_esistenti_aula = db_session.query(PrenotazioneAula).filter(
            and_(
                PrenotazioneAula.codice_utente == utente.username,
                PrenotazioneAula.ora_fine > ora_inizio,
                PrenotazioneAula.ora_inizio < ora_fine
            )
        ).all()

        prenotazioni_esistenti_posto_singolo = db_session.query(PrenotazionePosto).filter(
            and_(
                PrenotazionePosto.codice_utente == utente.username,
                PrenotazionePosto.ora_fine > ora_inizio,
                PrenotazionePosto.ora_inizio < ora_fine
            )
        ).all()

        prenotazioni_posti = prenotazioni_esistenti_aula + prenotazioni_esistenti_posto_singolo

        db_session.close()
        return len(prenotazioni_posti) > 0

    def cancella_prenotazione_posto_singolo(self, id_prenotazione_posto_singolo):
        db_session = Session()
        prenotazione_posto = db_session.query(PrenotazionePosto).get(id_prenotazione_posto_singolo)
        if prenotazione_posto:
            db_session.delete(prenotazione_posto)
            db_session.commit()
        db_session.close()

    def cancella_prenotazione_aula(self, id_prenotazione_aula):
        db_session = Session()
        prenotazione_aula = db_session.query(PrenotazioneAula).get(id_prenotazione_aula)
        if prenotazione_aula:
            db_session.delete(prenotazione_aula)
            db_session.commit()
        db_session.close()

    def get_utenti_con_prenotazioni_posti_singoli_oggi(self, text: str) -> list[Utente]:
        db_session = Session()
        adesso = datetime.now()
        utenti_con_prenotazioni_posti_singoli_oggi = db_session.query(Utente).join(
            PrenotazionePosto, Utente.username == PrenotazionePosto.codice_utente).filter(
            and_(
                # Utente.username == PrenotazionePosto.codice_utente,
                PrenotazionePosto.ora_attivazione == None,
                PrenotazionePosto.ora_inizio < adesso,
                PrenotazionePosto.ora_fine > adesso,
                or_(Utente.username.ilike(f"%{text}%"),
                    Utente.nome.ilike(f"%{text}%"),
                    Utente.cognome.ilike(f"%{text}%")))
        ).limit(3).all()
        db_session.close()
        return utenti_con_prenotazioni_posti_singoli_oggi

    def get_utenti_con_prenotazioni_aule_oggi(self, text: str) -> list[Utente]:
        db_session = Session()
        adesso = datetime.now()
        utenti_con_prenotazioni_aule_oggi = db_session.query(Utente).join(
            PrenotazioneAula, Utente.username == PrenotazioneAula.codice_utente).filter(
            and_(
                # Utente.username == PrenotazioneAula.codice_utente,
                PrenotazioneAula.ora_attivazione == None,
                PrenotazioneAula.ora_inizio < adesso,
                PrenotazioneAula.ora_fine > adesso,
                or_(Utente.username.ilike(f"%{text}%"),
                    Utente.nome.ilike(f"%{text}%"),
                    Utente.cognome.ilike(f"%{text}%"), ))
        ).limit(3).all()
        db_session.close()
        return utenti_con_prenotazioni_aule_oggi

    def get_prenotazioni_posti_singoli_oggi_by_utente(self, utente: Utente) -> list[PrenotazionePosto]:
        db_session = Session()
        adesso = datetime.now()
        prenotazioni_posti_singoli_oggi = db_session.query(PrenotazionePosto).filter(
            and_(PrenotazionePosto.codice_utente == utente.username,  # in un mondo ideale avrei potuto usare l'id.
                 PrenotazionePosto.ora_attivazione == None,
                 PrenotazionePosto.ora_inizio < adesso,
                 PrenotazionePosto.ora_fine > adesso)
        ).all()
        db_session.close()
        return prenotazioni_posti_singoli_oggi

    def get_prenotazioni_aule_oggi_by_utente(self, utente: Utente) -> list[PrenotazioneAula]:
        db_session = Session()
        adesso = datetime.now()
        prenotazioni_posti_singoli_oggi = db_session.query(PrenotazioneAula).filter(
            and_(PrenotazioneAula.codice_utente == utente.username,  # in un mondo ideale avrei potuto usare l'id.
                 PrenotazioneAula.ora_attivazione == None,
                 PrenotazioneAula.ora_inizio < adesso,
                 PrenotazioneAula.ora_fine > adesso)
        ).all()
        db_session.close()
        return prenotazioni_posti_singoli_oggi

    def attiva_prenotazione_posto_singolo(self, id_prenotazione: int) -> None:
        db_session = Session()
        prenotazione_posto_singolo: PrenotazionePosto = db_session.query(PrenotazionePosto).get(id_prenotazione)
        prenotazione_posto_singolo.ora_attivazione = datetime.now()
        db_session.commit()
        db_session.close()

    def attiva_prenotazione_aula(self, id_prenotazione: int) -> None:
        db_session = Session()
        prenotazione_aula: PrenotazioneAula = db_session.query(PrenotazioneAula).get(id_prenotazione)
        prenotazione_aula.ora_attivazione = datetime.now()
        db_session.commit()
        db_session.close()

    def get_aule(self) -> list[Aula]:
        db_session = Session()
        aule = db_session.query(Aula).all()
        db_session.close()
        return aule

    def cancella_prenotazioni_posti_non_attivate_in_tempo(self):
        db_session = Session()
        mia = timedelta(minutes=30)  # minuti_intervallo_attivazione (mia)
        adesso = datetime.now()

        # prenotazioni posti singoli (pps) non attivate in tempo da cancellare
        pps_da_cancellare: list[PrenotazionePosto] = db_session.query(PrenotazionePosto).filter(
            PrenotazionePosto.ora_attivazione == None
        ).all()
        for pps in pps_da_cancellare:
            if (pps.ora_inizio + mia) < adesso:
                print(f"cancellata la prenotazione posto singolo non attivata in tempo dell'utente {pps.codice_utente}")
                db_session.delete(pps)

        # prenotazioni aule (pa) non attivate in tempo
        pa_da_cancellare: list[PrenotazioneAula] = db_session.query(PrenotazioneAula).filter(
            PrenotazioneAula.ora_attivazione == None
        ).all()
        for pa in pa_da_cancellare:
            if (pa.ora_inizio + mia) < adesso:
                print(f"cancellata la prenotazione aula non attivata in tempo dell'utente {pa.codice_utente}")
                db_session.delete(pa)

        db_session.commit()
        db_session.close()

    def cancella_prenotazioni_posti_scadute(self) -> None:
        db_session = Session()
        adesso = datetime.now()

        # prenotazioni posti singoli (pps) scadute
        pps_scadute = db_session.query(PrenotazionePosto).filter(
            PrenotazionePosto.ora_fine < adesso
        ).all()
        for pps in pps_scadute:
            print("cancellata una prenotazione posto singolo scaduta")
            db_session.delete(pps)

        # prenotazioni aule (pa) scadute
        pa_scadute = db_session.query(PrenotazioneAula).filter(
            PrenotazioneAula.ora_fine < adesso
        ).all()
        for pa in pa_scadute:
            print("cancellata una prenotazione aula scaduta")
            db_session.delete(pa)
        db_session.close()
