from typing import Callable

import helpers

WELCOME_MESSAGE = "BIENVENUE DANS L'APPLICATION DE TOURNOIS"
INDEX_MENU_NAME = 0
INDEX_MENU_OPTIONS = 1
INDEX_MENU_DESCRIPTION = 2

class MenuView:
    """Classe vue des menus."""
    def __init__(self, controller):
        self.controller = controller

    def get_menu_user_choice(self) -> str:
        """Récupère et retourne le choix de l'utilisateur.

        Returns:
            str: Choix de l'utilisateur
        """
        return input("Quel est votre choix ? : ")

    @staticmethod
    def show_first_display(first_display: bool) -> str:
        """Ajoute un espace s'il ne s'agit pas du premier affichage
        du menu principal.

        Args:
            first_display (bool): Indique l'état de l'affichage

        Returns:
            str: Espace selon l'état.
        """
        if not first_display:
            space = helpers.SPACE
        else:
            space = ""
        return space

    @staticmethod
    def decorative_menu_element(function: Callable, first_display: bool) -> Callable:
        """Enveloppe pour formater le menu désiré pour affichage.

        Args:
            function (Callable): Fonction comportant le menu.
            first_display (bool): Etat du premier affichage.

        Returns:
            Callable: Retourne l'enveloppe du menu décoré.
        """
        def wrapper(*args, **kwargs):
            menu_name = args[INDEX_MENU_NAME]
            border_menu_size = (helpers.BORDER_SIZE - len(menu_name)) // 2
            try:
                file_name = args[INDEX_MENU_DESCRIPTION]
            except IndexError:
                file_name = ""
            if file_name != "":
                file_name = f"{helpers.BACK_TO_LINE}Nom : {file_name}"

            centered_menu = f"{border_menu_size * " "}{menu_name}{file_name}"
            if menu_name != helpers.MAIN_MENU_NAME:
                space = helpers.SPACE
            else:
                space = MenuView.show_first_display(first_display)
            
            top_menu = (
                f"{space}{helpers.BORDER}{helpers.BACK_TO_LINE}{centered_menu}"
                f"{helpers.BACK_TO_LINE}{helpers.BORDER}{helpers.BACK_TO_LINE}"
            )
            menu_option = function(*args, **kwargs)
            bottom_menu = f"{helpers.BACK_TO_LINE}{helpers.BORDER}"
            all_menu = f"{top_menu}{menu_option}{bottom_menu}"

            return all_menu
        
        return wrapper
    
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
        decoration = MenuView.decorative_menu_element(function=menu_function, first_display=first_display)
        full_menu = decoration(menu_name, options_menu)
        print(full_menu)
        return options_menu
    
    @staticmethod
    def show_error_message_choice(user_choice: str):
        """Affiche un message d'erreur lorsque le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(f"Erreur: La valeur \"{user_choice}\" n'est pas une commande valide.")

    @staticmethod
    def show_index_error_message_choice(user_choice: str, first_option, last_option):
        """Affiche un message d'erreur lorsque le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(f"Erreur: Votre choix \"{user_choice}\" n'est pas compris entre {first_option} et {last_option}.")