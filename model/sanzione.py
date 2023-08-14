from abstract.model import Model
from database import Sanzione as db_Sanzione
from datetime import datetime
from sqlalchemy import and_, or_


class Sanzione(Model):

    def new_sanzione(prestito: Prestito):
        db_session = Session()
        ''' ricerca vecchie sospensioni ?'''
        
        giorni = (prestito.data_restituzione - prestito.data_scadenza).days
        sanzione = Sanzione(id = str(uuid.uuid4())[:10], durata = datetime.now() + timedelta(giorni), tipo = "sospensione", utente_id = prestito.utente_id)
        db_session.add(sanzione)
        db_session.commit()
        db_session.close()






