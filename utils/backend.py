import uuid
from datetime import datetime

HISTORY_LIMIT = 5
POSTI_PER_AULA = 20
DURATA_PRENOTAZIONE = 3  # in giorni
MAX_PRENOTAZIONI = 3
CATALOGO = "catalogo"
CONTEXT_CATALOGO_PRENOTAZIONI = "catalogo_prenotazioni"
CONTEXT_CATALOGO = "context_catalogo"
DATE_FORMAT = "%d %B %Y %H:%M"

MODEL_LIBRO = "libri"
MODEL_PRENOTAZIONE_LIBRO = "prenotazioni_libri"

LABEL_LIBRO = "libro"
LABEL_PRENOTAZIONE_LIBRO = "prenotazione_libro"


def is_empty(string: str) -> bool:
    return (string is None) or (len(string) == 0)


def get_label(label: str) -> str:
    if is_empty(label):
        return str(uuid.uuid4())
    return label


def to_year(year: str) -> datetime:
    datetime_format = "%Y"
    datetime_year = datetime.strptime(year, datetime_format)
    return datetime_year


def get_codice() -> str:
    return str(uuid.uuid4())[:13]