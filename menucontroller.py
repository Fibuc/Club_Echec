from typing import Union

from menumodel import MenuModel
from menuview import MenuView
from Controllers.clubcontroller import ClubController
from Controllers.playercontroller import PlayerController
from tournamentcontroller import TournamentController
import helpers

MENU_NAME_KEY = "menu_name"
MENU_OPTIONS_KEY = "menu_options"

class MenuController():
    """Classe contrôleur des menus."""
    def __init__(self):
        self.view = MenuView(self)
        self.user_choice = ""
        self.club = ClubController()
        self.player = PlayerController()
        self.tournament = TournamentController()

    @staticmethod
    def select_menu(
        menu_name: str,
        options_menu: list,
        first_display: bool=False
    ) -> list:
        """Génération du menu souhaité à partir du model et envoie pour
        formatage par la vue.

        Args:
            menu_name (str): Nom du menu.
            options_menu (list): Liste des options du menu.
            first_display (bool, optional): Indique s'il s'agit du premier
            affichage. Défaut = False.

        Returns:
            list: Retourne la liste des options
        """
        model = MenuModel()
        menu_function = model.create_menu
        MenuView.show_menu(
            menu_function,
            menu_name,
            options_menu,
            first_display
        )
        return options_menu

    def check_user_choice(
            self,
            user_choice: str,
            menu_option_list: list
        ) -> Union[str, bool, bool]:
        """Vérifie le choix de l'utilisateur et en retourne la validité.
        Affiche le résultat à l'utilisateur.

        Args:
            user_choice (str): Input de l'utilisateur.
            menu_option_list (list): Liste des options disponibles.

        Returns:
            str: Retourne la chaîne de caractères liée au choix 
            de l'utilisateur.
            bool: Retourne False si le choix de l'utilisateur est 
            une chaîne de caractères.
            bool: Retourne False si l'utilisateur rentre un nombre
            qui n'est pas dans la liste.
        """
        choice_number = 0
        validity_user_choice = []
        for _ in menu_option_list:
            choice_number += 1
            validity_user_choice.append(choice_number)
        try:
            user_choice_number = int(user_choice)
            index_choose_option = user_choice_number - 1
            if user_choice_number in validity_user_choice:
                user_option = menu_option_list[index_choose_option]
                return user_option
            else:
                first_option = 1
                last_option = len(menu_option_list)
                self.view.show_index_error_message_choice(
                    user_choice,
                    first_option,
                    last_option
                )
                helpers.sleep_a_few_seconds()
                return False
            
        except ValueError:
            self.view.show_error_message_choice(user_choice)
            helpers.sleep_a_few_seconds()
            return False

    def main_menu(self):
        """Récupération du menu principal et envoi pour génération."""
        launch = True
        first_display = True
        while launch:
            current_menu = helpers.MAIN_MENU
            current_menu_name = current_menu[MENU_NAME_KEY]
            current_menu_option = current_menu[MENU_OPTIONS_KEY]
            if type(current_menu_option) == dict:
                options = list(current_menu_option.keys())
            else:
                options = current_menu_option

            if not first_display:
                helpers.SPACE
                
            menu_option_list = self.select_menu(
                current_menu_name,
                options,
                first_display
            )
            user_choice = self.view.get_menu_user_choice()
            user_option = self.check_user_choice(user_choice, menu_option_list)
            if not user_option:
                first_display = False
                continue
            if user_option == options[-1]:
                launch = False
                break

            sub_menu = current_menu_option[user_option]
            self.sub_menu(sub_menu)
            first_display = False

    def sub_menu(self, sub_menu: dict):
        """Récupération du sous-menu et envoi pour génération.

        Args:
            sub_menu (dict): Dictionnaire du sous-menu.
        """
        launch = True
        while launch:
            current_menu_name = sub_menu[MENU_NAME_KEY]
            current_menu_options = sub_menu[MENU_OPTIONS_KEY]
            menu_option_list = self.select_menu(
                current_menu_name,
                current_menu_options
            )
            current_menu_options.append(next(iter(helpers.ACTION_CHOICE_MENU)))
            # Ajout de l'option revenir au menu précédent.
            user_choice = self.view.get_menu_user_choice()
            user_option = self.check_user_choice(user_choice, menu_option_list)
            if not user_option:
                current_menu_options.pop()
                continue
            elif user_option == current_menu_options[-1]:
                launch = False
            else:
                eval(helpers.ACTION_CHOICE_MENU[user_option])
                
            current_menu_options.pop()