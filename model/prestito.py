import uuid
from datetime import datetime,timedelta
from typing import Dict
from abstract.model import Model
from database import Session, PrenotazioneLibro as db_prenotazione_libro, Prestito as db_prestito
from view.component.view_errore import view_errore
from .libro import Libro
from model.sanzione import Sanzione


class Prestito(Model):

    '''def inserisci(self, codice_prenotazione):
        db_session = Session()
        prenotazione = db_session.query(db_prenotazione_libro).filter_by(codice=codice_prenotazione).first()
        if prenotazione:
            if prenotazione.data_scadenza<=datetime.now():
                view_errore.create_layout(self,"ERRORE","La prenotazione è scaduta")
            else:
                prestito = db_prestito(libro= prenotazione.libro, utente=prenotazione.utente)
                db_session.add(prestito)
                db_session.commit()
                db_session.close()
        else:
            view_errore.create_layout(self, "ERRORE", "Prenotaione non trovata")'''

    def inserisci(self, dati:Dict):
        db_session = Session()
        prestito = db_prestito(data_inizio = datetime.now(), data_scadenza= datetime.now() + timedelta(days=21),libro_id=dati["libro"], utente_id=dati["utente"],codice = str(uuid.uuid4())[:12])
        db_session.add(prestito)
        print(prestito.codice)
        db_session.commit()
        db_session.close()




    def restituzione(self, prestito):

        db_session = Session()
        prestito.data_restituzione = datetime.now()
       
        if prestito.data_restituzione > prestito.data_scadenza:
            Sanzione.new_sanzione(prestito)
            
        db_session.merge(prestito)
        libro = Libro.by_id(self,prestito.libro_id)
        libro.disponibili += 1
        db_session.merge(libro)
        db_session.commit()
        db_session.close()

    def by_utente(self, id):
        db_session = Session()
        prestiti = db_session.query(db_prestito).filter_by(utente_id=id).all()
        db_session.close()
        return prestiti