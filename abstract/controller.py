from abc import abstractmethod
from typing import Dict, Optional, Iterable

from abstract.model import Model
from abstract.view import View
from protocol.observer import Observer


class Controller:
    def __init__(self, models: Optional[Dict[str, Model]] = None, views: Optional[Dict[str, View]] = None):
        self.models = models
        self.views = views

        self.controllers: Optional[Iterable[Observer]] = None
        # self.instantiated_views: Dict[str, View] = {label: view() for label, view in self.views.items()}
        from app import main_window
        self.main_window = main_window

    def set_observer_controllers(self, controllers: Iterable[Observer]):
        self.controllers = controllers

    @abstractmethod
    def update(self, message: str, data: dict):
        pass

