from enum import Enum


class KeyDb(Enum):
    LIBRO = "DB_LIBRO"
    PRENOTAZIONE_LIBRO = "DB_PRENOTAZIONE_LIBRO"


class KeyModel(Enum):
    LIBRO = "MODEL_LIBRI"
    PRENOTAZIONE_LIBRO = "MODEL_PRENOTAZIONI_LIBRI"


class Key(Enum):
    CATALOGO = "CATALOGO"
    TEXT = "TEXT"
    CONTESTO = "CONTESTO"

