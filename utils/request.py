from enum import Enum

REQUEST_GO_TO_LOGIN = "go_to_login"
REQUEST_GO_TO_LIBRI_PRENOTATI = "go_to_libri_prenotati"

REQUEST_LOGIN = "login"
REQUEST_LOGOUT = "logout"


class Request(Enum):
    LOGOUT = "logout"
    SEARCH = "search"
    PRENOTA_LIBRO = "prenota_libro"
    OSSERVA_LIBRO = "osserva_libro"
    CANCELLA_PRENOTAZIONE_LIBRO = "cancella_prenotazione_libro"

    GO_TO_DETTAGLI_LIBRO = "go_to_dettagli_libro"
    GO_TO_DETTAGLI_PRENOTAZIONE_LIBRO = "go_to_dettagli_prenotazione_libro"

