from enum import Enum

REQUEST_GO_TO_LOGIN = "go_to_login"
REQUEST_GO_TO_LIBRI_PRENOTATI = "go_to_libri_prenotati"

REQUEST_LOGIN = "login"
REQUEST_LOGOUT = "logout"

REQUEST_VISUALIZZA_LIBRO = "visualizza_libro"
REQUEST_VISUALIZZA_DETTAGLI_PRENOTAZIONE_LIBRO = "visualizza_dettagli_prenotazione_libro"
REQUEST_PRENOTA_LIBRO = "prenota_libro"
REQUEST_OSSERVA_LIBRO = "osserva_libro"
REQUEST_CANCELLA_PRENOTAZIONE_LIBRO = "cancella_prenotazione_libro"


class Request(Enum):
    SEARCH = "search"
    GO_TO_LOGIN = "go_to_login"
    LOGOUT = "logout"
    LOGIN = "login"
    GO_TO_LIBRI_IN_PRESTITO = "go_to_libri_in_prestito"
    GO_TO_LIBRI_PRENOTATI = "go_to_libri_prenotati"
    GO_TO_LISTA_DI_OSSERVAZIONE = "go_to_lista_di_osservazione"
    GO_TO_PRENOTA_POSTO = "go_to_prenota_posto"
    GO_TO_POSTI_PRENOTATI = "go_to_posti_prenotati"
    GO_TO_CRONOLOGIA = "go_to_cronologia"
    GO_TO_SANZIONI = "go_to_sanzioni"
    GO_TO_VISUALIZZA_LIBRO = "go_to_visualizza_libro"
    GO_TO_STATISTICHE = "go_to_visualizza_statistiche"
    PRENOTA_LIBRO = "prenota_libro"
    OSSERVA_LIBRO = "osserva_libro"
    GO_TO_DETTAGLI_PRENOTAZIONE_LIBRO = "go_to_visualizza_dettagli_prenotazione_libro"
    CANCELLA_PRENOTAZIONE_LIBRO = "cancella_prenotazione_libro"
    RIMUOVI_LIBRO_OSSERVATO = "RIMUOVI_LIBRO_OSSERVATO"
    CHECK_LIBRI_OSSERVATI = "CHECK_LIBRI_OSSERVATI"
    CHECK_SCADENZA_PRENOTAZIONI = "CHECK_SCADENZA_PRENOTAZIONI"
