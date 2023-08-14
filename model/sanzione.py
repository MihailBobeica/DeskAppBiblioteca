import uuid

from abstract.model import Model
from database import Sanzione as db_Sanzione
from datetime import datetime, timedelta
from database import Session,Prestito as db_Prestito
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






