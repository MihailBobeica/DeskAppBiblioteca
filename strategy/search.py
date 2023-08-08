from abc import abstractmethod

from abstract import BoundedModel
from model import PrenotazioneLibro
from model.libro import Libro
from utils.auth import Auth
from utils.backend import is_empty, MODEL_PRENOTAZIONE_LIBRO, MODEL_LIBRO, LABEL_PRENOTAZIONE_LIBRO, LABEL_LIBRO


class SearchStrategy:
    def __init__(self):
        pass

    @abstractmethod
    def search(self, models: dict[str, BoundedModel], text: str) -> list[dict[str, object]]:
        pass


class CercaLibriCatalogo(SearchStrategy):
    def search(self, models: dict[str, BoundedModel], text: str) -> list[dict[str, object]]:
        model_libro: Libro = models[MODEL_LIBRO]
        if is_empty(text):
            libri = model_libro.get()
        else:
            libri = model_libro.search(text)
        data = [{LABEL_LIBRO: libro} for libro in libri]
        return data

    def __init__(self):
        super().__init__()


class CercaPrenotazioniValide(SearchStrategy):
    def search(self, models: dict[str, BoundedModel], text: str) -> list[dict[str, object]]:
        model_prenotazione_libro: PrenotazioneLibro = models[MODEL_PRENOTAZIONE_LIBRO]
        model_libro: Libro = models[MODEL_LIBRO]
        utente = Auth.user
        if is_empty(text):
            prenotazioni_valide = model_prenotazione_libro.valide(utente=utente)
        else:
            prenotazioni_valide = model_prenotazione_libro.ricerca_valide(utente=utente,
                                                                          text=text)
        libri_prenotati = [model_libro.by_prenotazione(prenotazione) for prenotazione in prenotazioni_valide]
        data = [{LABEL_PRENOTAZIONE_LIBRO: prenotazione,
                 LABEL_LIBRO: libro}
                for prenotazione, libro in zip(prenotazioni_valide, libri_prenotati)]
        return data

    def __init__(self):
        super().__init__()
