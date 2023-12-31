from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import and_, or_, delete

from abstract import Model
from database import Sanzione, Prestito, PrenotazioneLibro, Utente
from database import Session
from database import db_engine
from utils.backend import DURATA_PRENOTAZIONE


class ModelSanzioni(Model):
    def cancella_sanzioni_terminate(self) -> None:
        cancella_sanzioni_scadute = delete(Sanzione).where(
            and_(Sanzione.data_fine != None,
                 Sanzione.data_fine < datetime.now())
        )
        connection = db_engine.connect()
        result = connection.execute(cancella_sanzioni_scadute)
        connection.commit()
        connection.close()
        print(f"Deleted {result.rowcount} rows from table sanzioni.")

    def check_libri_non_restituiti(self) -> None:
        db_session = Session()
        prestiti_non_restituiti: list[Prestito] = db_session.query(Prestito).join(Utente).filter(
            and_(Prestito.utente_id == Utente.id,
                 Prestito.data_restituzione == None,
                 Prestito.data_scadenza < datetime.now(),
                 )
        ).all()
        for pnr in prestiti_non_restituiti:
            id_utente = pnr.utente_id
            id_prestito = pnr.id
            if not self._sanzione_esistente_associata_a_prestito(id_utente, id_prestito):
                self._aggiungi_sanzione_da_libro_non_restituito(id_utente, id_prestito)
                print(f"Aggiunta una sanzione associata a utente: {id_utente}; prestito: {id_prestito}.")
        db_session.close()

    def check_libri_prenotati_ma_non_ritirati(self) -> None:
        db_session = Session()
        prenotazioni_non_ritirate: list[PrenotazioneLibro] = db_session.query(PrenotazioneLibro).join(Utente).filter(
            and_(PrenotazioneLibro.utente_id == Utente.id,
                 PrenotazioneLibro.data_cancellazione == None,
                 PrenotazioneLibro.data_scadenza < datetime.now(),
                 )
        ).all()
        for pnr in prenotazioni_non_ritirate:
            id_utente = pnr.utente_id
            id_prenotazione = pnr.id
            data_fine = pnr.data_prenotazione + timedelta(days=2 * DURATA_PRENOTAZIONE)
            if not self._sanzione_esistente_associata_a_prestito(id_utente, id_prenotazione):
                self._aggiungi_sanzione_da_prenotazione_non_ritirata(id_utente, id_prenotazione, data_fine)
                print(f"Aggiunta una sanzione associata a utente: {id_utente}; prenotazione: {id_prenotazione}.")
        db_session.close()

    def _sanzione_esistente_associata_a_prestito(self, id_utente: int, id_prestito: int):
        db_session = Session()
        esistente = db_session.query(Sanzione).filter(
            and_(Sanzione.utente_id == id_utente,
                 Sanzione.prestito_id == id_prestito)
        ).first()
        db_session.close()
        return esistente is not None

    def _sanzione_esistente_associata_a_prenotazione(self, id_utente: int, id_prenotazione: int):
        db_session = Session()
        esistente = db_session.query(Sanzione).filter(
            and_(Sanzione.utente_id == id_utente,
                 Sanzione.prenotazione_id == id_prenotazione)
        ).first()
        db_session.close()
        return esistente is not None

    def _aggiungi_sanzione_da_libro_non_restituito(self, id_utente: int, id_prestito: int):
        db_session = Session()

        sanzione = Sanzione(utente_id=id_utente,
                            prestito_id=id_prestito)
        db_session.add(sanzione)
        db_session.commit()
        db_session.close()

    def _aggiungi_sanzione_da_prenotazione_non_ritirata(self, id_utente: int, id_prenotazione: int,
                                                        data_fine: datetime):
        db_session = Session()

        sanzione = Sanzione(utente_id=id_utente,
                            prenotazione_id=id_prenotazione,
                            data_fine=data_fine)
        db_session.add(sanzione)
        db_session.commit()
        db_session.close()

    def inserisci(self, dati: dict[str, str]):
        pass

    def da_cancella_prenotazione(self, utente: Utente, data_fine: datetime) -> None:
        db_session = Session()

        sospensione = Sanzione(data_fine=data_fine,
                               utente_id=utente.id,
                               tipo="sospensione",
                               durata=None)

        db_session.add(sospensione)
        db_session.commit()
        db_session.close()

    def is_sanzionato(self, utente: Utente) -> bool:
        db_session = Session()
        sanzioni_valide = db_session.query(Sanzione).filter(
            and_(Sanzione.utente_id == utente.id,
                 or_(Sanzione.data_fine == None,
                     Sanzione.data_fine >= datetime.now())
                 )
        ).all()

        db_session.close()
        return len(sanzioni_valide) >= 1

    def ha_sanzioni(self, id_utente: int) -> bool:
        db_session = Session()
        sanzioni_valide = db_session.query(Sanzione).filter(
            and_(Sanzione.utente_id == id_utente,
                 or_(Sanzione.data_fine == None,
                     Sanzione.data_fine >= datetime.now())
                 )
        ).all()

        db_session.close()
        return len(sanzioni_valide) >= 1

    def get_fine_sanzione(self, id_utente: int) -> Optional[datetime]:
        db_session = Session()
        sanzioni_valide: list[Sanzione] = db_session.query(Sanzione).filter(
            and_(Sanzione.utente_id == id_utente,
                 or_(Sanzione.data_fine == None,
                     Sanzione.data_fine >= datetime.now())
                 )
        ).all()
        db_session.close()

        fine_sanzioni = [sanzione_valida.data_fine for sanzione_valida in sanzioni_valide]
        if None in fine_sanzioni:
            return None
        fine_sanzioni_dates_only = [fine_sanzione for fine_sanzione in fine_sanzioni if fine_sanzione is not None]
        return max(fine_sanzioni_dates_only)

    def restituzione_in_ritardo(self, prestito: Prestito) -> None:
        db_session = Session()
        prestito: Prestito = db_session.query(Prestito).get(prestito.id)
        durata: timedelta = prestito.data_restituzione - prestito.data_scadenza
        data_fine = datetime.now() + durata
        sanzione = Sanzione(data_fine=data_fine,
                            durata=durata,
                            tipo="sospensione",
                            utente_id=prestito.utente_id,
                            prestito_id=prestito.id)
        db_session.add(sanzione)
        db_session.commit()
        db_session.close()
