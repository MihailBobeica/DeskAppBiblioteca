from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from utils import ADMIN, OPERATORE, UTENTE

db_engine = create_engine('sqlite:///./database/db.sqlite')

Session = sessionmaker(bind=db_engine)

Base = declarative_base()


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
    autori = Column(String)
    immagine = Column(String)
    editore = Column(String)
    isbn = Column(String)
    anno_edizione = Column(DateTime)
    anno_pubblicazione = Column(DateTime)
    disponibili = Column(Integer)
    dati = Column(String)


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


Base.metadata.drop_all(db_engine)  # cancella tutte le tabelle
Base.metadata.create_all(db_engine)  # crea tutte le tabelle
