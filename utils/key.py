from enum import Enum

KEY_DB_LIBRO = "db_libro"
KEY_DB_PRENOTAZIONE_LIBRO = "db_prenotazione_libro"
# KEY_DB_ = "db_"

KEY_LABEL_COMPONENT_TITOLO = "key_label_component_title"
KEY_LABEL_COMPONENT_AUTORI = "key_label_component_autori"
KEY_LABEL_COMPONENT_DISPONIBILI = "key_label_component_disponibili"
KEY_LABEL_COMPONENT_SCADENZA_PRENOTAZIONE_LIBRO = "key_label_component_scadenza_prenotazione_libro"
KEY_LABEL_COMPONENT_ANNO_EDIZIONE = "key_label_component_edizione"
KEY_LABEL_COMPONENT_ANNO_PUBBLICAZIONE = "key_label_component_anno_pubblicazione"
KEY_LABEL_COMPONENT_EDITORE = "key_label_component_editore"
# KEY_LABEL_COMPONENT_ = "key_label_component_"

KEY_BUTTON_COMPONENT_VISUALIZZA_LIBRO = "key_button_component_visualizza_libro"
KEY_BUTTON_COMPONENT_PRENOTA_LIBRO = "key_button_component_prenota_libro"
KEY_BUTTON_COMPONENT_OSSERVA_LIBRO = "key_button_component_osserva_libro"
KEY_BUTTON_COMPONENT_DETTAGLI_PRENOTAZIONE_LIBRO = "key_button_component_dettagli_prenotazione_libro"
KEY_BUTTON_COMPONENT_CANCELLA_PRENOTAZIONE_LIBRO = "key_button_component_cancella_prenotazione_libro"
KEY_BUTTON_COMPONENT_GO_TO_LIBRI_PRENOTATI = "key_button_component_go_to_libri_prenotati"
# KEY_BUTTON_COMPONENT_ = "key_button_component_"
# KEY_BUTTON_COMPONENT_ = "key_button_component_"
# KEY_BUTTON_COMPONENT_ = "key_button_component_"
# KEY_BUTTON_COMPONENT_ = "key_button_component_"

KEY_AUTH_GUEST = "auth_guest"
KEY_AUTH_UTENTE = "auth_utente"
KEY_AUTH_OPERATORE = "auth_operatore"
KEY_AUTH_ADMIN = "auth_admin"
# KEY_AUTH_VIEW_ = "auth_"

KEY_CONTEXT_CATALOGO_LIBRI = "context_catalogo_libri"
KEY_CONTEXT_CATALOGO_LIBRI_GUEST = "context_catalogo_libri_guest"
KEY_CONTEXT_CATALOGO_LIBRI_UTENTE = "context_catalogo_libri_utente"
KEY_CONTEXT_CATALOGO_PRENOTAZIONI_LIBRI = "context_catalogo_prenotazioni_libri"


# KEY_CONTEXT_CATALOGO_LIBRI_OPERATORE = "context_catalogo_libri_operatore"
# KEY_CONTEXT_CATALOGO_LIBRI_ADMIN = "context_catalogo_libri_admin"


class KeyDb(Enum):
    LIBRO = "db_libro"
    PRESTITO = "db_prestito"
    PRENOTAZIONE_LIBRO = "db_prenotazione_libro"


class KeyAuth(Enum):
    ADMIN = "auth_admin"
    OPERATORE = "auth_operatore"
    UTENTE = "auth_utente"
    GUEST = "auth_guest"


class KeyLabelComponent(Enum):
    TITOLO = "key_label_component_title"
    AUTORI = "key_label_component_autori"
    DISPONIBILI = "key_label_component_disponibili"
    ANNO_EDIZIONE = "key_label_component_anno_edizione"
    ANNO_PUBBLICAZIONE = "key_label_component_anno_pubblicazione"
    EDITORE = "key_label_component_editore"
    SCADENZA_PRENOTAZIONE_LIBRO = "key_label_component_scadenza_prenotazione_libro"
    DATI = "KEY_LABEL_COMPONENT_DATI"
    ISBN = "KEY_LABEL_COMPONENT_ISBN"
    DATA_PRENOTAZIONE_LIBRO = "KEY_LABEL_COMPONENT_DATA_PRENOTAZIONE_LIBRO"
    CODICE_PRENOTAZIONE_LIBRO = "KEY_LABEL_COMPONENT_CODICE_PRENOTAZIONE_LIBRO"
    INIZIO_PRESTITO = "KEY_LABEL_COMPONENT_INIZIO_PRESTITO"
    FINE_PRESTITO = "KEY_LABEL_COMPONENT_FINE_PRESTITO"


class KeyButtonComponent(Enum):
    VISUALIZZA_LIBRO = "key_button_component_visualizza_libro"
    PRENOTA_LIBRO = "key_button_component_prenota_libro"
    OSSERVA_LIBRO = "key_button_component_osserva_libro"
    DETTAGLI_PRENOTAZIONE_LIBRO = "key_button_component_dettagli_prenotazione_libro"
    CANCELLA_PRENOTAZIONE_LIBRO = "key_button_component_cancella_prenotazione_libro"
    GO_TO_LIBRI_PRENOTATI = "key_button_component_go_to_libri_prenotati"
    GO_TO_LIBRI_IN_PRESTITO = "key_button_component_go_to_libri_in_prestito"
    RIMUOVI_LIBRO_OSSERVATO = "KEY_BUTTON_RIMUOVI_LIBRO_OSSERVATO"
    DETTAGLI_PRESTITO = "DETTAGLI_PRESTITO"


class KeyContext(Enum):
    CATALOGO_LIBRI_GUEST = "context_catalogo_libri_guest"
    CATALOGO_LIBRI_UTENTE = "context_catalogo_libri_utente"
    CATALOGO_PRENOTAZIONI_LIBRI = "context_catalogo_prenotazioni_libri"
    CATALOGO_LIBRI_OSSERVATI = "context_catalogo_libri_osservati"
    CATALOGO_LIBRI_IN_PRESTITO = "context_catalogo_libri_in_prestito"
