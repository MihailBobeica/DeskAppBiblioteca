from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from utils.key import KeyContext
from utils.request import Request
from view.component import SidebarComponent, CatalogoComponent


class HomeGuestView(View):
    def create_layout(self):
        # content
        sidebar = SidebarComponent()
        btn_login = sidebar.set_button("Login")
        btn_login.clicked.connect(self.go_to_login)

        catalogo = CatalogoComponent(context=KeyContext.CATALOGO_LIBRI_GUEST)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(sidebar)
        layout.addWidget(catalogo)

    def __init__(self):
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_login
        self.attach(controller_login)

    def go_to_login(self):
        self.notify(Request.GO_TO_LOGIN)
