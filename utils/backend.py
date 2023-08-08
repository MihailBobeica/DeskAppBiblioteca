import uuid
from datetime import datetime

HISTORY_LIMIT = 5
POSTI_PER_AULA = 20
DURATA_PRENOTAZIONE = 3  # in giorni
MAX_PRENOTAZIONI = 3
CATALOGO = "catalogo"

# TODO maybe put context in a separate file
CONTEXT_CATALOGO_PRENOTAZIONI = "catalogo_prenotazioni"

CONTEXT_CATALOGO_LIBRI_GUEST = "context_catalogo_libri_guest"
CONTEXT_CATALOGO_LIBRI_UTENTE = "context_catalogo_libri_utente"
CONTEXT_CATALOGO_LIBRI_OPERATORE = "context_catalogo_libri_operatore"
CONTEXT_CATALOGO_LIBRI_ADMIN = "context_catalogo_libri_admin"

DATE_FORMAT = "%d %B %Y %H:%M"

MODEL_LIBRO = "libri"
MODEL_PRENOTAZIONE_LIBRO = "prenotazioni_libri"

LABEL_LIBRO = "libro"
LABEL_PRENOTAZIONE_LIBRO = "prenotazione_libro"

OBJ_NAME_SEARCHBAR = "searchbar"

REQUEST_GO_TO_LOGIN = "go_to_login"
REQUEST_LOGIN = "login"


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
