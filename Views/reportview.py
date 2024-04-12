from typing import Callable

import config
import helpers

class ReportView:

    @staticmethod
    def show_menu(
        menu_function: Callable, menu_name: str, options_menu: list
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
        decoration = helpers.decorative_menu_element(function=menu_function)
        full_menu = decoration(menu_name, options_menu)
        print(full_menu)
        return options_menu

    def get_menu_user_choice(self) -> str:
            """Récupère et retourne le choix de l'utilisateur.

            Returns:
                str: Choix de l'utilisateur
            """
            return input("Quel est votre choix ? : ")

    @staticmethod
    def waiting_user_continuation():
        input("Appuyez sur une touche pour continuer : ")

    @staticmethod
    def get_tournament_to_show():
         print(config.BORDER)
         print("(Laisser vide pour annuler)")
         return input("Quel est le tournois que vous voulez afficher ? : ")
    
    @staticmethod
    def show_error_message_choice(user_choice: str):
        """Affiche un message d'erreur lorsque le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(f"Erreur: La commande \"{user_choice}\" n'est pas une commande valide.")

    @staticmethod
    def menu_tournament_report(
        menu_function: Callable, menu_name: str, options_menu: list,
        tournament_informations: list
    ):
        decoration = helpers.decorative_menu_element(function=menu_function, description=tournament_informations)
        full_menu = decoration(menu_name, options_menu)
        print(full_menu)
        return options_menu
         