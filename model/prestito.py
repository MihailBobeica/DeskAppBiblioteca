import uuid
from datetime import datetime,timedelta

from abstract.model import Model
from database import Session, PrenotazioneLibro as db_prenotazione_libro, Prestito as db_prestito
from view.component.view_errore import view_errore


class Prestito(Model):

    def inserisci(self, codice_prenotazione):
        db_session = Session()
        prenotazione = db_session.query(db_prenotazione_libro).filter_by(codice=codice_prenotazione).first()
        if prenotazione:
            if prenotazione.data_scadenza<=datetime.now():
                view_errore.create_layout(self,"ERRORE","La prenotazione è scaduta")
            else:
                prestito = db_prestito(data_inizio=datetime.now(),data_scadenza=datetime.now() + timedelta(days=21), codice=str(uuid.uuid4())[:10],libro= prenotazione.libro, utente=prenotazione.utente)
                db_session.add(prestito)
                db_session.commit()
                db_session.close()
        else:
            view_errore.create_layout(self, "ERRORE", "Prenotaione non trovata")


    def restituzione(self, prestito):
        db_session = Session()
        prestito.data_restituzione = datetime.now()
        db_session.merge(prestito)
        db_session.commit()
        db_session.close()

    def by_utente(self, username):
        db_session = Session()
        prestiti = db_session.query(db_prestito).filter_by(utente=username).all()
        db_session.close()
        return prestiti