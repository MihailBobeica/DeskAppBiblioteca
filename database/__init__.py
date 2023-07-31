from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.strings import ADMIN, OPERATORE, UTENTE

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


class Aula(Base):
    __tablename__ = 'aule'

    id = Column(Integer, primary_key=True)
    nome = Column(String)


class Posto(Base):
    __tablename__ = 'posti'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    aula = Column(String)


class PrenotazionePosto(Base):
    __tablename__ = 'prenotazioni_posti'

    id = Column(Integer, primary_key=True)
    data_prenotazione = Column(DateTime)
    ora_inizio = Column(String)
    ora_fine = Column(String)
    ora_attivazione = Column(String)
    durata = Column(Integer)
    codice_posto = Column(String)
    codice_utente = Column(String)


class PrenotazioneAula(Base):
    __tablename__ = 'prenotazioni_aule'

    id = Column(Integer, primary_key=True)
    data_prenotazione = Column(DateTime)
    ora_inizio = Column(String)
    ora_fine = Column(String)
    ora_attivazione = Column(String)
    durata = Column(Integer)
    codice_aula = Column(String)
    codice_utente = Column(String)

class PrenotazioneLibro(Base):
    __tablename__ = "prenotazioni_libri"

    id = Column(Integer, primary_key=True)
    data_prenotazione = Column(DateTime)
    data_scadenza = Column(DateTime)
    libro = Column(String, ForeignKey('libri.isbn'))
    utente = Column(String, ForeignKey('utenti.username'))




Base.metadata.drop_all(db_engine)  # cancella tutte le tabelle
Base.metadata.create_all(db_engine)  # crea tutte le tabelle
