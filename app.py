from controller.first import FirstController
from controller.login import LoginController
from controller.logout import LogoutController
from view.main import MainWindow

# instantiate the main window
main_window = MainWindow()

# instantiate all controllers
controller_first = FirstController()
controller_login = LoginController()
controller_logout = LogoutController()
