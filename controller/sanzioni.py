from abstract import Controller
from model import ModelSanzioni
from utils.auth import auth
from view.common import SanzioniView


class ControllerSanzioni(Controller):
    def __init__(self,
                 model_sanzioni: ModelSanzioni):
        self.model_sanzioni = model_sanzioni
        super().__init__()

        self.model_sanzioni.cancella_sanzioni_terminate()
        self.model_sanzioni.check_libri_non_restituiti()
        self.model_sanzioni.check_libri_prenotati_ma_non_ritirati()

    def _fill_view_sanzioni(self, view: SanzioniView):
        id_utente = auth.user.id
        if view.id_utente:
            id_utente = view.id_utente
        ha_sanzioni = self.model_sanzioni.ha_sanzioni(id_utente)
        if ha_sanzioni:
            fine_sanzione = self.model_sanzioni.get_fine_sanzione(id_utente)
            if fine_sanzione:
                view.change_label(f"Sanzionato fino al: {fine_sanzione.strftime('%d %B %Y')}")
            else:
                view.change_label("Sanzione a tempo indeterminato!")
        else:
            view.change_label("Nessuna sanzione!")
