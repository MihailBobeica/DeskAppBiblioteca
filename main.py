import database
from database import Session
from database import Utente

db_session = Session()

un_utente = Utente(nome='nome', cognome='cognome', username='username', password='password')
un2_utente = Utente(nome='nome2', cognome='cognome', username='username', password='password')

db_session.add_all([un_utente, un2_utente])
db_session.commit()
