from mainview import View
from menucontroller import MenuController

MENU_NAME_KEY = "menu_name"
MENU_OPTIONS_KEY = "menu_options"

class Controller:
    """Classe contrôleur principal"""
    def __init__(self):
        self.view = View(self)
        self.menu_controller = MenuController()

    def run(self):
        """Lance l'éxecution de l'application"""
        self.view.show_welcome_message()
        self.menu_controller.main_menu()
        self.view.say_goodbye()