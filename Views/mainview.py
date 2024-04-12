from typing import Callable

import config
import helpers
import menus

class MainView:
    """Classe vue principale."""

    @staticmethod
    def show_welcome_message():
        """Affiche le message de bienvenue."""
        welcome_message = menus.WELCOME_MESSAGE
        border_menu_size = (config.BORDER_SIZE - len(welcome_message)) // 2
        centered_menu = f"{border_menu_size * ' '}{welcome_message}"
        message = (
            f"{config.BACK_TO_LINE}"
            f"{config.BORDER}{config.BACK_TO_LINE}"
            f"{centered_menu}"
        )
        print(message)

    def get_menu_user_choice(self) -> str:
            """Récupère et retourne le choix de l'utilisateur.

            Returns:
                str: Choix de l'utilisateur
            """
            return input("Quel est votre choix ? : ")

    @staticmethod
    def show_error_message_choice(user_choice: str):
        """Affiche un message d'erreur lorsque le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(f"Erreur: La valeur \"{user_choice}\" n'est pas une commande valide.")

    @staticmethod
    def say_goodbye():
        """Affiche le message de fermeture de l'application."""
        print("Fermeture de l'application.")


    @staticmethod
    def show_menu(
        menu_function: Callable,
        menu_name: str,
        options_menu: list,
        first_display: bool
    ) -> list:
        """Affiche le menu formaté.

        Args:
            menu_function (Callable): Fonction comprenant le menu.
            menu_name (str): Nom du menu.
            options_menu (list): Liste des options du menu.
            first_display (bool): Etat du premier affichage.

        Returns:
            list: Retourne la liste des options.
        """
        decoration = helpers.decorative_menu_element(function=menu_function, first_display=first_display)
        full_menu = decoration(menu_name, options_menu)
        print(full_menu)
        return options_menu