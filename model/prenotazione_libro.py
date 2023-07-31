from abstract.model import Model
from database import PrenotazioneLibro as db_prenotazione_libro
from database import Session
from utils.auth import Auth
from datetime import datetime,timedelta
from database import Libro as db_libro

class PrenotazioneLibro(Model):
    def inserisci(self, libro : db_libro):
        db_session = Session()
        prenotazione_libro = db_prenotazione_libro(libro = libro.isbn, utente = Auth.user.username, data_prenotazione = datetime.utcnow(), data_scadenza = datetime.utcnow() + timedelta(days=3))
        if self.sospensione():
            pass
        if self.max_prenotazioni():
            pass
        if self.libro_non_disponibile():
            pass
        else:
            db_session.add(prenotazione_libro)
            print(prenotazione_libro.utente)
            print(prenotazione_libro.data_prenotazione)
            print(prenotazione_libro.data_scadenza)
            print(prenotazione_libro.libro)
            db_session.commit()
            db_session.close()


    def __init__(self):
        super().__init__()

    def sospensione(self):
        pass

    def max_prenotazioni(self):
        pass

    def libro_non_disponibile(self):
        pass
