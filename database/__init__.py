import os
from os import path
from typing import TypeVar

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Interval
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker


RESEED_DB = True  # flag per ricreare le tabelle del database e rifare il seed

base_dir_name = "DeskAppBiblioteca"
project_dir = os.getcwd().rsplit(base_dir_name)[0]
app_dir = path.join(project_dir, base_dir_name)
database_absolute_path = path.join(app_dir, "database/db.sqlite")
if not os.path.exists(database_absolute_path):
    with open(database_absolute_path, "w") as file:
        print("Il database (file) non era presente ed è stato creato.")
db_engine = create_engine(f"sqlite:///{database_absolute_path}")

Session = sessionmaker(bind=db_engine)

Base = declarative_base()

BoundedDbModel = TypeVar("BoundedDbModel", bound=Base)


# Single Table Inheritance (STI):
class User(Base):
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


class Utente(User):
    __mapper_args__ = {
        'polymorphic_identity': 'utente'
    }


class Operatore(User):
    __mapper_args__ = {
        'polymorphic_identity': 'operatore'
    }


class Amministratore(User):
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }


class Libro(Base):
    __tablename__ = 'libri'

    id = Column(Integer, primary_key=True)
    titolo = Column(String)
    autori = Column(String)
    immagine = Column(String, default="default.jpg")
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
    durata = Column(Integer, nullable=True)
    codice_posto = Column(String)
    codice_utente = Column(String)


class PrenotazioneAula(Base):
    __tablename__ = 'prenotazioni_aule'

    id = Column(Integer, primary_key=True)
    data_prenotazione = Column(DateTime)
    ora_inizio = Column(DateTime)
    ora_fine = Column(DateTime)
    ora_attivazione = Column(DateTime)
    durata = Column(Integer, nullable=True)
    codice_aula = Column(String)
    codice_utente = Column(String)


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
    durata = Column(Interval, nullable=True)
    tipo = Column(String, nullable=True)
    utente_id = Column(Integer, ForeignKey('utenti.id'))
    prestito_id = Column(Integer, ForeignKey('prestiti.id'), nullable=True)
    prenotazione_id = Column(Integer, ForeignKey('prenotazioni_libri.id'), nullable=True)

    utente = relationship("Utente")
    prestito = relationship("Prestito")
    prenotazione = relationship("PrenotazioneLibro")


class LibroOsservato(Base):
    __tablename__ = "osservazioni"

    id = Column(Integer, primary_key=True)

    utente_id = Column(Integer, ForeignKey('utenti.id'))
    libro_id = Column(Integer, ForeignKey('libri.id', ondelete="CASCADE"))

    utente = relationship("Utente")
    libro = relationship("Libro")


if RESEED_DB:
    # reset database
    Base.metadata.drop_all(db_engine)  # cancella tutte le tabelle
    Base.metadata.create_all(db_engine)  # crea tutte le tabelle
