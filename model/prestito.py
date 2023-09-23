import uuid
from datetime import datetime,timedelta
from typing import Dict, Type
from abstract.model import Model
from database import Session, PrenotazioneLibro as db_prenotazione_libro, Prestito as DbPrestito
from view.component.view_errore import view_errore
from .libro import Libro
from sqlalchemy import or_, and_
from model.sanzione import Sanzione
from database import Utente as DbUtente
from database import Libro as DbLibro



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
        prestito = DbPrestito(data_inizio = datetime.now(), data_scadenza=datetime.now() + timedelta(days=21), libro_id=dati["libro"], utente_id=dati["utente"], codice =str(uuid.uuid4())[:12])
        db_session.add(prestito)
        db_session.commit()
        db_session.close()

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
            Sanzione.new_sanzione(prestito)
            
        db_session.merge(prestito)
        libro = Libro.by_id(self,prestito.libro_id)
        libro.disponibili += 1
        db_session.merge(libro)
        db_session.commit()
        db_session.close()

    def by_utente(self, utente_id):
        db_session = Session()
        prestiti = db_session.query(DbPrestito).filter(DbPrestito.utente_id == utente_id)
        db_session.close()
        return prestiti

    def da_restituire(self, id):
        db_session = Session()
        prestiti = db_session.query(DbPrestito).filter(and_(DbPrestito.utente_id == id), (DbPrestito.data_restituzione == None)).all()
        print(prestiti)
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
            cont+=1
        print(cont)
        if cont>3:
            return False
        else:
            return True



