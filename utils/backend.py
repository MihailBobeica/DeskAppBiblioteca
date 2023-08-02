import uuid
from datetime import datetime

HISTORY_LIMIT = 5
POSTI_PER_AULA = 20
DURATA_PRENOTAZIONE = 3  # in giorni
MAX_PRENOTAZIONI = 3
CATALOGO = "catalogo"
CATALOGO_PRENOTAZIONI = "catalogo_prenotazioni"
DATE_FORMAT = "%d %B %Y %H:00"


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
    return str(uuid.uuid4())
