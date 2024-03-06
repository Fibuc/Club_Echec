import helpers


INDEX_MENU_NAME = 0
INDEX_MENU_OPTIONS = 1
INDEX_MENU_DESCRIPTION = 2

class View:
    """Classe vue principale."""
    def __init__(self, controller):
        self.controller = controller
        
    @staticmethod
    def show_welcome_message():
        """Affiche le message de bienvenue."""
        message = (
            f"{helpers.BACK_TO_LINE}"
            f"{helpers.BORDER}{helpers.BACK_TO_LINE}"
            f"{helpers.WELCOME_MESSAGE}"
        )
        print(message)

    @staticmethod
    def say_goodbye():
        """Affiche le message de fermeture de l'application."""
        print("Fermeture de l'application.")