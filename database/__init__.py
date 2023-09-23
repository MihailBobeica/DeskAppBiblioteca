import uuid
from typing import TypeVar

from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from utils.role import *

db_engine = create_engine('sqlite:///./database/db.sqlite')

Session = sessionmaker(bind=db_engine)

Base = declarative_base()

BoundedDbModel = TypeVar("BoundedDbModel", bound=Base)


# Single Table Inheritance (STI):
class Utente(Base):
    __tablename__ = 'utenti'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cognome = Column(String)
    ruolo = Column(String)
    username = Column(String)
    password = Column(String)

    __mapper_args__ = {
        'polymorphic_on': ruolo,
        'polymorphic_identity': 'utente_generico'
    }


class Studente(Utente):
    __mapper_args__ = {
        'polymorphic_identity': 'utente'
    }


class Operatore(Utente):
    __mapper_args__ = {
        'polymorphic_identity': 'operatore'
    }


class Amministratore(Utente):
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }


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
    ora_inizio = Column(DateTime)
    ora_fine = Column(DateTime)
    ora_attivazione = Column(DateTime)
    durata = Column(Integer)
    codice_posto = Column(String)
    codice_utente = Column(String)


class PrenotazioneAula(Base):
    __tablename__ = 'prenotazioni_aule'

    id = Column(Integer, primary_key=True)
    data_prenotazione = Column(DateTime)
    ora_inizio = Column(DateTime)
    ora_fine = Column(DateTime)
    ora_attivazione = Column(DateTime)
    durata = Column(Integer)
    codice_aula = Column(String)
    codice_utente = Column(String)

    # aula_id = Column(Integer, ForeignKey('aule.id'))
    # utente_id = Column(Integer, ForeignKey('utenti.id'))
    #
    # aula = relationship("Aula")
    # utente = relationship("Utente")


class PrenotazioneLibro(Base):
    __tablename__ = 'prenotazioni_libri'

    id = Column(Integer, primary_key=True)
    data_prenotazione = Column(DateTime)
    data_scadenza = Column(DateTime)
    data_cancellazione = Column(DateTime, nullable=True)
    codice = Column(String)

    utente_id = Column(Integer, ForeignKey('utenti.id'))
    libro_id = Column(Integer, ForeignKey('libri.id', ondelete="CASCADE"))

    utente = relationship("Utente")
    libro = relationship("Libro")


class Prestito(Base):
    __tablename__ = 'prestiti'

    id = Column(Integer, primary_key=True)
    data_inizio = Column(DateTime)
    data_scadenza = Column(DateTime)
    data_restituzione = Column(DateTime, nullable=True)
    codice = Column(String)
    utente_id = Column(Integer, ForeignKey('utenti.id'))
    libro_id = Column(Integer, ForeignKey('libri.id', ondelete="CASCADE"))

    utente = relationship("Utente")
    libro = relationship("Libro")


class Sanzione(Base):
    __tablename__ = "sanzioni"

    id = Column(Integer, primary_key=True)
    data_fine = Column(DateTime, nullable=True)
    durata = Column(DateTime, nullable=True)
    tipo = Column(String)
    utente_id = Column(Integer, ForeignKey('utenti.id'))
    prestito_id = Column(Integer, ForeignKey('prestiti.id'), nullable=True)
    prenotazione_id = Column(Integer, ForeignKey('prenotazioni_libri.id'), nullable=True)

    utente = relationship("Utente")
    prestito = relationship("Prestito")
    prenotazione = relationship("PrenotazioneLibro")


class OsservaLibro(Base):
    __tablename__ = "osservazioni"

    id = Column(Integer, primary_key=True)

    utente_id = Column(Integer, ForeignKey('utenti.id'))
    libro_id = Column(Integer, ForeignKey('libri.id', ondelete="CASCADE"))

    utente = relationship("Utente")
    libro = relationship("Libro")


Base.metadata.drop_all(db_engine)  # cancella tutte le tabelle
Base.metadata.create_all(db_engine)  # crea tutte le tabelle
