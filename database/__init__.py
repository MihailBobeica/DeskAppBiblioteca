from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from utils import hash_password

db_engine = create_engine('sqlite:///./database/db.sqlite')

Session = sessionmaker(bind=db_engine)

Base = declarative_base()

ADMIN = "admin"
OPERATORE = "operatore"
UTENTE = "utente"


class Utente(Base):
    __tablename__ = 'utenti'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cognome = Column(String)
    ruolo = Column(Enum(ADMIN, OPERATORE, UTENTE))
    username = Column(String)
    password = Column(String)


class Libro(Base):
    __tablename__ = 'libri'

    id = Column(Integer, primary_key=True)
    titolo = Column(String)
    autore = Column(String)
    isbn = Column(String)


class PrenotazionePosto(Base):
    __tablename__ = 'prenotazioni_posti'

    id = Column(Integer, primary_key=True)
    data_prenotazione = Column(DateTime)
    data_effettuazione = Column(DateTime)
    ora_inizio = Column(String)
    ora_fine = Column(String)
    ora_attivazione = Column(String)
    disponibilita = Column(Boolean)
    codice_posto = Column(String)


utenti = [{"nome": "Mario",
           "cognome": "Rossi",
           "ruolo": "admin",
           "username": "S001",
           "password": hash_password("admin")},
          {"nome": "Giulio",
           "cognome": "Bianchi",
           "ruolo": "operatore",
           "username": "S002",
           "password": hash_password("operatore")},
          {"nome": "Dario",
           "cognome": "Facchini",
           "ruolo": "utente",
           "username": "S003",
           "password": hash_password("utente")},
          ]

Base.metadata.drop_all(db_engine)  # cancella tutte le tabelle
Base.metadata.create_all(db_engine)  # crea tutte le tabelle

# seeding del database
db_session = Session()
for u in utenti:
    utente = Utente(nome=u["nome"],
                    cognome=u["cognome"],
                    ruolo=u["ruolo"],
                    username=u["username"],
                    password=u["password"])
    db_session.add(utente)
db_session.commit()

#  creare le tabelle nel database utilizzando la classe PrenotazionePosto
Base.metadata.create_all(db_engine)

# EsempioOoooOO di utilizzo di PrenotazionePosto
prenotazione = PrenotazionePosto(
    data_prenotazione="2023-07-18",
    data_effettuazione="2023-07-19",
    ora_inizio="09:00",
    ora_fine="12:00",
    ora_attivazione="08:45",
    disponibilita=True,
    codice_posto="A101"
)

# inserire la prenotazione nel database
db_session = Session()
db_session.add(prenotazione)
db_session.commit()

# ottenere tutte le prenotazioni dal database
prenotazioni = db_session.query(PrenotazionePosto).all()
for prenotazione in prenotazioni:
    prenotazione.stampa()
