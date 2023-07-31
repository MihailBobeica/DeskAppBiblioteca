import uuid
from datetime import datetime

HISTORY_LIMIT = 5
POSTI_PER_AULA = 20


def is_empty(string: str) -> bool:
    return (string is None) or (len(string) == 0)


def get_label(label: str):
    if (label is None) or (len(label) == 0):
        return uuid.uuid4()
    return label


def to_year(year: str) -> datetime:
    datetime_format = "%Y"
    datetime_year = datetime.strptime(year, datetime_format)
    return datetime_year
