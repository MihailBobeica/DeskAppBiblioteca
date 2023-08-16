from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from utils.context import CONTEXT_CATALOGO_LIBRI_GUEST
from utils.request import REQUEST_GO_TO_LOGIN
from utils.strings import BUTTON_LABEL_LOGIN
from view.component import SidebarComponent, CatalogoComponent


class HomeGuestView(View):
    def create_layout(self):
        # content
        sidebar = SidebarComponent()
        sidebar.set_buttons(labels=(BUTTON_LABEL_LOGIN,))
        sidebar.button[BUTTON_LABEL_LOGIN].clicked.connect(self.send_go_to_login_view_request)

        catalogo = CatalogoComponent(context=CONTEXT_CATALOGO_LIBRI_GUEST)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(catalogo)

    def __init__(self):
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_login
        self.attach(controller_login)

    def send_go_to_login_view_request(self):
        self.notify(REQUEST_GO_TO_LOGIN)
