from abc import abstractmethod

from abstract import BoundedModel
from model import ModelPrenotazioniLibri, ModelLibriOsservati
from model.libri import ModelLibri
from model.prestiti import ModelPrestiti
from utils.auth import auth
from utils.backend import is_empty, MODEL_PRENOTAZIONE_LIBRO, MODEL_LIBRO


class SearchStrategy:
    @abstractmethod
    def search(self, models: dict[str, BoundedModel], text: str) -> list[dict[str, object]]:
        pass


class CercaLibriCatalogo(SearchStrategy):
    def search(self, models: dict[str, BoundedModel], text: str) -> list[dict[str, object]]:
        model_libro: ModelLibri = models[MODEL_LIBRO]
        if is_empty(text):
            libri = model_libro.get()
        else:
            libri = model_libro.by_text(text)
        data = [{"libro": libro} for libro in libri]
        return data

    def __init__(self):
        super().__init__()


class CercaPrenotazioniValide(SearchStrategy):
    def search(self, models: dict[str, BoundedModel], text: str) -> list[dict[str, object]]:
        model_prenotazione_libro: ModelPrenotazioniLibri = models[MODEL_PRENOTAZIONE_LIBRO]
        model_libro: ModelLibri = models[MODEL_LIBRO]
        utente = auth.user
        if is_empty(text):
            prenotazioni_valide = model_prenotazione_libro.valide_by_utente(utente=utente)
        else:
            prenotazioni_valide = model_prenotazione_libro.ricerca_valide_by_text(utente=utente,
                                                                                  text=text)
        libri_prenotati = [model_libro.by_prenotazione(prenotazione) for prenotazione in prenotazioni_valide]
        data = [{"prenotazione_libro": prenotazione,
                 "libro": libro}
                for prenotazione, libro in zip(prenotazioni_valide, libri_prenotati)]
        return data

    def __init__(self):
        super().__init__()


class CercaLibriOsservati(SearchStrategy):
    def search(self, models: dict[str, BoundedModel], text: str) -> list[dict[str, object]]:
        model_libro_osservato: ModelLibriOsservati = models["osserva_libri"]

        if is_empty(text):
            libri_osservati = model_libro_osservato.by_utente(auth.user)
        else:
            libri_osservati = model_libro_osservato.by_text(auth.user, text)
        data = [{"libro": libro} for libro in libri_osservati]
        return data

    def __init__(self):
        super().__init__()


class CercaLibriInPrestito(SearchStrategy):
    def search(self, models: dict[str, BoundedModel], text: str) -> list[dict[str, object]]:
        model_prestito: ModelPrestiti = models["prestiti"]

        if is_empty(text):
            prestiti = model_prestito.validi_by_utente(auth.user)
        else:
            prestiti = model_prestito.validi_by_utente_and_text(auth.user, text)
        libri_in_prestito = [model_prestito.get_libro(prestito) for prestito in prestiti]
        data = [{"libro": libro, "prestito": prestito} for libro, prestito in zip(libri_in_prestito, prestiti)]
        return data

    def __init__(self):
        super().__init__()
