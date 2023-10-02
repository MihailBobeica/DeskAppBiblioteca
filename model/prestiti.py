import uuid
from datetime import datetime, timedelta
from typing import Dict, Type, Any
from abstract.model import Model
from database import Session, PrenotazioneLibro as db_prenotazione_libro, Prestito as DbPrestito
from utils.backend import get_codice, DURATA_PRESTITO
# from view.component.view_errore import view_errore
from .libri import ModelLibri
from sqlalchemy import or_, and_
from model.sanzioni import ModelSanzioni
from database import User as DbUtente
from database import Libro as DbLibro


class ModelPrestiti(Model):
    def inserisci(self,
                  data_inizio: datetime,
                  data_restituzione: datetime,
                  utente_id: int,
                  libro_id: int):
        db_session = Session()
        prestito = DbPrestito(data_inizio=data_inizio,
                              data_scadenza=data_inizio + timedelta(days=DURATA_PRESTITO),
                              data_restituzione=data_restituzione,
                              codice=get_codice(),
                              utente_id=utente_id,
                              libro_id=libro_id)
        db_session.add(prestito)
        db_session.commit()
        db_session.close()

    def __init__(self):
        super().__init__()

    def valide(self, utente: DbUtente):
        db_session = Session()
        prestiti = db_session.query(DbPrestito).filter(
            and_(DbPrestito.utente_id == utente.id,
                 DbPrestito.data_restituzione == None,
                 DbPrestito.data_scadenza >= datetime.now())
        ).all()
        libri_in_prestito = [p.libro for p in prestiti]
        db_session.close()
        return prestiti, libri_in_prestito

    def valide_by_text(self, utente: DbUtente, text: str):
        db_session = Session()
        prestiti = db_session.query(DbPrestito).join(DbLibro).filter(
            and_(DbPrestito.utente_id == utente.id,
                 DbPrestito.data_restituzione == None,
                 DbPrestito.data_scadenza >= datetime.now(),
                 or_(DbLibro.titolo.ilike(f"%{text}%"),
                     DbLibro.autori.ilike(f"%{text}%"))
                 )
        ).all()
        libri_in_prestito = [p.libro for p in prestiti]
        db_session.close()
        return prestiti, libri_in_prestito

    def restituzione(self, prestito):

        db_session = Session()
        prestito.data_restituzione = datetime.now()

        if prestito.data_restituzione > prestito.data_scadenza:
            ModelSanzioni.new_sanzione(prestito)

        db_session.merge(prestito)
        libro = ModelLibri.by_id(self, prestito.libro_id)
        libro.disponibili += 1
        db_session.merge(libro)
        db_session.commit()
        db_session.close()

    def passati(self, id_utente: int) -> list[DbPrestito]:
        db_session = Session()
        prestiti = db_session.query(DbPrestito).filter(
            and_(DbPrestito.utente_id == id_utente,
                 DbPrestito.data_restituzione != None)
        ).order_by(DbPrestito.data_inizio.desc()).all()
        db_session.close()
        return prestiti

    def by_utente(self, utente_id):
        db_session = Session()
        prestiti = db_session.query(DbPrestito).filter(DbPrestito.utente_id == utente_id)
        db_session.close()
        return prestiti

    def da_restituire(self, id):
        db_session = Session()
        prestiti = db_session.query(DbPrestito).filter(and_(DbPrestito.utente_id == id),
                                                       (DbPrestito.data_restituzione == None)).all()
        # print(prestiti)
        db_session.close()
        return prestiti

    def scaduti(self, utente: DbUtente):
        db_session = Session()
        prestiti_scaduti = db_session.query(DbPrestito).filter(
            and_(DbPrestito.utente_id == utente.id,
                 DbPrestito.data_scadenza > datetime.now())
        ).all()
        db_session.close()
        return prestiti_scaduti

    def check_max(self, utente_id) -> bool:
        db_sesseion = Session()
        cont = 0
        prestiti = db_sesseion.query(DbPrestito).filter(and_(DbPrestito.utente_id == utente_id,
                                                             DbPrestito.data_scadenza < datetime.now(),
                                                             DbPrestito.data_restituzione is None)).all()
        db_sesseion.close()
        for i in prestiti:
            cont += 1
        print(cont)
        if cont > 3:
            return False
        else:
            return True
