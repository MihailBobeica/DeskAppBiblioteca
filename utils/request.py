from enum import Enum

REQUEST_GO_TO_LOGIN = "go_to_login"
REQUEST_GO_TO_LIBRI_PRENOTATI = "go_to_libri_prenotati"

REQUEST_LOGIN = "login"
REQUEST_LOGOUT = "logout"

class Request(Enum):
    LOGOUT = "logout"
