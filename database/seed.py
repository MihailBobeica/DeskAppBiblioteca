from datetime import datetime

from utils.auth import hash_password
from utils.backend import to_year, POSTI_PER_AULA

UTENTI = [
    {"nome": "Mario",
     "cognome": "Rossi",
     "ruolo": "admin",
     "username": "S001",
     "password": hash_password("admin")},
    {"nome": "Giulio",
     "cognome": "Bianchi",
     "ruolo": "operatore",
     "username": "S002",
     "password": hash_password("operatore")},
    {"nome": "Dario",
     "cognome": "Verdi",
     "ruolo": "utente",
     "username": "S003",
     "password": hash_password("utente")},
]

LIBRI = [
    {"titolo": "Fisica. Vol. 1: Meccanica, termodinamica",
     "autori": "Paolo Mazzoldi, Massimo Nigro, Cesare Voci",
     "immagine": "fisica_1.jpg",
     "editore": "Edises",
     "isbn": "0471958697",
     "anno_edizione": to_year("2000"),
     "anno_pubblicazione": to_year("2000"),
     "disponibili": 3,
     "dati": "583 p., ill., 2 ed."},
    {"titolo": "Fisica. Vol. 2: Elettromagnetismo, onde",
     "autori": "Paolo Mazzoldi, Massimo Nigro, Cesare Voci",
     "immagine": "fisica_2.jpg",
     "editore": "Edises",
     "isbn": "0306406152",
     "anno_edizione": to_year("1998"),
     "anno_pubblicazione": to_year("1998"),
     "disponibili": 4,
     "dati": "792 p., ill., brossura, 2 ed."},
    {"titolo": "Sistemi operativi",
     "autori": "Abraham Silberschatz, Peter Baer Galvin, Greg Gagne",
     "immagine": "sistemi_operativi.jpg",
     "editore": "Pearson",
     "isbn": "123456789X",
     "anno_edizione": to_year("2019"),
     "anno_pubblicazione": to_year("2019"),
     "disponibili": 2,
     "dati": "1 voll., XXXIV-860 p., 10 ed."},
    {"titolo": "Ricerca operativa",
     "autori": "Massimo Pappalardo, Mauro Passacantando",
     "immagine": "ricerca_operativa.jpg",
     "editore": "Pisa University Press",
     "isbn": "0123456789X",
     "anno_edizione": to_year("2013"),
     "anno_pubblicazione": to_year("2013"),
     "disponibili": 0,
     "dati": "374 p., brossura, 2 ed."},
    {"titolo": "Piccole abitudini per grandi cambiamenti",
     "autori": "James Clear",
     "immagine": "atomic_habits.jpg",
     "editore": "De Agostini",
     "isbn": "1234567890X",
     "anno_edizione": to_year("2019"),
     "anno_pubblicazione": to_year("2019"),
     "disponibili": 3,
     "dati": "332 p., ill., brossura"},
]
AULE = [
    {"nome": "Acquario_1"},
    {"nome": "Acquario_2"},
    {"nome": "Acquario_3"},
    {"nome": "Salone"}
]

POSTI = []
for aula in AULE:
    nome_aula = aula["nome"]
    for numero_posto in range(1, POSTI_PER_AULA + 1):
        posto = {"nome": f"{numero_posto}{nome_aula}", "aula": nome_aula}
        POSTI.append(posto)

PRESTITI = [
    {
        "data_restituzione": None,
        "utente": 3,
        "libro": 1
    }, {
        "data_restituzione": None,
        "utente": 3,
        "libro": 2
    }
]

PRENOTAZIONI_AULE = [
    {
        "id": "1",
        "data_prenotazione": datetime(2023, 8, 1),
        "ora_inizio": datetime(2023, 8, 3, 21, 50),
        "ora_fine": datetime(2023, 8, 3, 23, 57),
        "ora_attivazione": None,
        "durata": 120,
        "codice_aula": "Acquario_1",
        "codice_utente": "S001"
    },
    {
        "id": "2",
        "data_prenotazione": datetime(2023, 8, 1),
        "ora_inizio": datetime(2023, 8, 3, 22, 0),
        "ora_fine": datetime(2023, 8, 3, 21, 55),
        "ora_attivazione": None,
        "durata": 120,
        "codice_aula": "Acquario_2",
        "codice_utente": "S002"
    },
    {
        "id": "3",
        "data_prenotazione": datetime(2023, 8, 3),
        "ora_inizio": datetime(2023, 8, 3, 21, 24),
        "ora_fine": datetime(2023, 8, 3, 23, 24),
        "ora_attivazione": datetime(2023, 8, 3, 21, 24),
        "durata": 120,
        "codice_aula": "Acquario_2",
        "codice_utente": "S002"
    }
]
