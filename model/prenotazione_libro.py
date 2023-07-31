import uuid

from PySide6.QtWidgets import QApplication, QMessageBox

from abstract.model import Model
from database import PrenotazioneLibro as db_prenotazione_libro
from database import Session
from utils.auth import Auth
from datetime import datetime,timedelta
from database import Libro as db_libro
from sqlalchemy import and_
from view.component.view_errore import view_errore

class PrenotazioneLibro(Model):

    def max_prenotazioni_singolo(self, prenotazione: db_prenotazione_libro):
        db_session = Session()
        num = db_session.query(db_prenotazione_libro).filter(and_(db_prenotazione_libro.utente == prenotazione.utente, db_prenotazione_libro.libro == prenotazione.libro )).count()
        db_session.close()
        if num>=1:
            view_errore.create_layout(self,"ERRORE", "Hai già effettuato una prenotazione per questo libro")
            return True
        else :
            return False


    def max_prenotazioni(self, prenotazione: db_prenotazione_libro):
        db_session = Session()
        num = db_session.query(db_prenotazione_libro).filter_by(utente=prenotazione.utente).count()
        if num>=3:
            view_errore.create_layout(self,"ERRORE","hai già effettuato il massimo numero(3) di prenotazioni")
            return True



    def inserisci(self, libro : db_libro):
        db_session = Session()
        prenotazione_libro = db_prenotazione_libro(libro = libro.isbn, utente = Auth.user.username, data_prenotazione = datetime.now(), data_scadenza = datetime.now() + timedelta(days=3), codice=str(uuid.uuid4())[:10])

        if PrenotazioneLibro.max_prenotazioni_singolo(self,prenotazione_libro):
            pass
        if PrenotazioneLibro.max_prenotazioni(self,prenotazione_libro):
            pass
        else:
            db_session.add(prenotazione_libro)
            print(prenotazione_libro.utente)
            print(prenotazione_libro.data_prenotazione)
            print(prenotazione_libro.data_scadenza)
            print(prenotazione_libro.libro)
            print(prenotazione_libro.codice)
            db_session.commit()
            db_session.close()


    def __init__(self):
        super().__init__()

    def sospensione(self):
        pass





    def libro_non_disponibile(self):
        pass
