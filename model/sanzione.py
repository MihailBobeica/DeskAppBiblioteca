import uuid

from abstract.model import Model
from database import Sanzione as db_Sanzione
from datetime import datetime, timedelta
from database import Session,Prestito as db_Prestito,Sanzione as db_Sanzione
from sqlalchemy import and_, or_



class Sanzione(Model):

    def new_sanzione(prestito: db_Prestito):
        db_session = Session()
        ''' ricerca vecchie sospensioni ?'''
        
        giorni = (prestito.data_restituzione - prestito.data_scadenza)
        sanzione = db_Sanzione(id = str(uuid.uuid4())[:12], durata = datetime.now() + timedelta(giorni.days), tipo = "sospensione", utente_id = prestito.utente_id)
        db_session.add(sanzione)
        db_session.commit()
        db_session.close()


    def check_sansiozioni(self):
        db_session = Session
        scaduti = db_session.query(db_Prestito).filter(and_(db_Prestito.data_scadenza < datetime.now()),db_Prestito.data_restituzione == None).all()
        for scaduto in scaduti:
            sanzione_attiva = db_session.query(db_Sanzione).filter_by(or_(and_(db_Sanzione.durata < datetime.now()),db_Sanzione.utente_id == scaduto.utente_id),db_Sanzione.utente_id != scaduto.utente_id).first()
            if not sanzione_attiva:
                self.new_sanzione(scaduto)
        db_session.commit()
        db_session.close()








