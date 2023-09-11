from datetime import datetime, timedelta

from sqlalchemy import and_, or_

from abstract.model import Model
from database import Sanzione as DbSanzione
from database import Session, Prestito as DbPrestito
from database import PrenotazioneLibro as DbPrenotazioneLibro
from database import Utente as DbUtente
from utils.backend import DURATA_PRENOTAZIONE


class Sanzione(Model):
    def new_sanzione(self, prestito: DbPrestito):
        db_session = Session()
        ''' ricerca vecchie sospensioni ?'''

        giorni = (prestito.data_restituzione - prestito.data_scadenza)
        sanzione = DbSanzione(durata=datetime.now() + timedelta(giorni.days),
                              tipo="sospensione", utente_id=prestito.utente_id)
        db_session.add(sanzione)
        db_session.commit()
        db_session.close()

    def check_sanzioni(self):
        db_session = Session
        scaduti = db_session.query(DbPrestito).filter(
            and_(DbPrestito.data_scadenza < datetime.now(),
                 DbPrestito.data_restituzione == None)
        ).all()
        for scaduto in scaduti:
            sanzione_attiva = db_session.query(DbSanzione).filter_by(
                or_(and_(DbSanzione.durata < datetime.now()), DbSanzione.utente_id == scaduto.utente_id),
                DbSanzione.utente_id != scaduto.utente_id).first()
            if not sanzione_attiva:
                self.new_sanzione(scaduto)
        db_session.commit()
        db_session.close()

    def inserisci(self, dati: dict[str, str]):
        pass

    def from_cancella_prenotazione(self, utente: DbUtente, data_fine: datetime):
        db_session = Session()

        sospensione = DbSanzione(data_fine=data_fine,
                                 utente_id=utente.id,
                                 tipo="sospensione",
                                 durata=None)

        db_session.add(sospensione)
        db_session.commit()
        db_session.close()

    def from_libro_non_restituito(self, utente: DbUtente, prestito: DbPrestito):
        db_session = Session()

        sospensione = DbSanzione(utente_id=utente.id,
                                 prestito_id=prestito.id,
                                 tipo="sospensione")

        db_session.add(sospensione)
        db_session.commit()
        db_session.close()

    def from_libro_non_ritirato(self, utente: DbUtente, prenotazione: DbPrenotazioneLibro):
        db_session = Session()

        data_fine = datetime.now() + timedelta(days=DURATA_PRENOTAZIONE)

        sospensione = DbSanzione(data_fine=data_fine,
                                 utente_id=utente.id,
                                 prenotazione_id=prenotazione.id,
                                 tipo="sospensione")

        db_session.add(sospensione)
        db_session.commit()
        db_session.close()

    def is_sanzionato(self, utente: DbUtente) -> bool:
        db_session = Session()
        sanzioni_valide = db_session.query(DbSanzione).filter(
            and_(DbSanzione.utente_id == utente.id,
                 or_(DbSanzione.data_fine == None,
                     DbSanzione.data_fine >= datetime.now())
                 )
        ).all()

        db_session.close()
        return len(sanzioni_valide) >= 1

    def prestito_is_registered(self, utente: DbUtente, prestito: DbPrestito) -> bool:
        db_session = Session()
        sanzione = db_session.query(DbSanzione).filter(
            and_(DbSanzione.utente_id == utente.id,
                 DbSanzione.prestito_id == prestito.id)
        ).all()
        db_session.close()
        return len(sanzione) >= 1  # >= just in case

    def prenotazione_is_registered(self, utente: DbUtente, prenotazione: DbPrenotazioneLibro) -> bool:
        db_session = Session()
        sanzione = db_session.query(DbSanzione).filter(
            and_(DbSanzione.utente_id == utente.id,
                 DbSanzione.prestito_id == prenotazione.id)
        ).all()
        db_session.close()
        return len(sanzione) >= 1  # >= just in case
