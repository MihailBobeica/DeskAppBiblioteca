import os
import shutil
import uuid
from datetime import datetime

HISTORY_LIMIT = 5
POSTI_PER_AULA = 20
DURATA_PRENOTAZIONE = 3  # in giorni
MINIMO_COPIE_DISPONIBILI = 1
MAX_PRENOTAZIONI = 2
MAX_OSSERVAZIONI = 5
DURATA_PRESTITO = 21  # giorni
CATALOGO = "catalogo"

# TODO maybe put context in a separate file
CONTEXT_CATALOGO_PRENOTAZIONI = "catalogo_prenotazioni"

DATE_FORMAT = "%d %B %Y %H:%M"
YEAR_FORMAT = "%Y"

MODEL_LIBRO = "libri"
MODEL_PRENOTAZIONE_LIBRO = "prenotazioni_libri"

KEY_LIBRO = "libro"
KEY_PRENOTAZIONE_LIBRO = "prenotazione_libro"

OBJ_NAME_SEARCHBAR = "searchbar"


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


def backup():
    source_file = os.path.join(os.getcwd(), "database/db.sqlite")  # Replace with the path to your source file
    t_name = datetime.now().strftime("%Y_%m_%d")
    destination_file = os.path.join(os.getcwd(), f"backup/{t_name}.sqlite")  # Replace with the path to your destination file

    try:
        shutil.copy(source_file, destination_file)
        print(f"File copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print("Source file not found.")
    except PermissionError:
        print("Permission denied. Check if you have write access to the destination directory.")
    except shutil.SameFileError:
        print("Source and destination files are the same.")
    except Exception as e:
        print(f"An error occurred: {e}")

# @staticmethod
# def create_search_strategy(context: str) -> SearchStrategy:
#     if context in [CONTEXT_CATALOGO_LIBRI_GUEST,
#                    CONTEXT_CATALOGO_LIBRI_UTENTE,
#                    CONTEXT_CATALOGO_LIBRI_OPERATORE,
#                    CONTEXT_CATALOGO_LIBRI_ADMIN]:
#         return CercaLibriCatalogo()
#     elif context == CONTEXT_CATALOGO_PRENOTAZIONI_LIBRI:
#         return CercaPrenotazioniValide()
#     else:
#         raise ValueError("Invalid search strategy type")
