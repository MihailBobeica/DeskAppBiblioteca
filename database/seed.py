from utils import hash_password

UTENTI = [{"nome": "Mario",
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

LIBRI = [{"titolo": "Pensiero Positivo",
          "autore": "Marta Lowen",
          "isbn": "isbn",
          "immagine": "pensiero_positivo.webp"}]
