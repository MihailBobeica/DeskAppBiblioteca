from PySide6.QtWidgets import QHBoxLayout

from abstract.view import View
from utils.key import KeyContext
from view.component import SidebarComponent, CatalogoComponent


class HomeGuestView(View):
    def create_layout(self):
        # content
        btn_login = self.sidebar.set_button("Login")
        btn_login.clicked.connect(self.go_to_login)

        catalogo = CatalogoComponent(context=KeyContext.CATALOGO_LIBRI_GUEST)

        # layout
        layout = QHBoxLayout(self)
        layout.addWidget(self.sidebar)
        layout.addWidget(catalogo)

    def __init__(self):
        self.sidebar = SidebarComponent()
        super().__init__()

    def attach_controllers(self) -> None:
        from app import controller_router
        self.attach(controller_router)

    def go_to_login(self):
        self.notify("go_to_login")
