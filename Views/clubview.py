from typing import Callable

import config
import helpers

class ClubView:

    @staticmethod
    def show_menu(
        menu_function: Callable,
        menu_name: str,
        options_menu: list
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
    def show_error_message_choice(user_choice: str):
        """Affiche un message d'erreur lorsque le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(f"Erreur: La valeur \"{user_choice}\" n'est pas une commande valide.")

    @staticmethod
    def show_border():
        print(config.BORDER)

    @staticmethod
    def back_to_line():
        print(config.BACK_TO_LINE)

    def get_club_informations(self):
        self.show_border()
        club_name = input("Quel est le nom du club ? : ")
        national_chest_id = input("Quel est sont identifiant national ? : ")
        return club_name, national_chest_id

    @staticmethod
    def show_created_club(club_name: str):
        print(f"Le club \"{club_name}\" a bien été créé.")


    @staticmethod
    def show_error_national_chest_id(national_chest_id: str):
        print(f"Le numéro d'identifiant national \"{national_chest_id}\" n'est pas correct.")

    @staticmethod
    def show_error_empty_name():
        print("Erreur: Le nom du club ne peut pas être vide.")


    @staticmethod
    def show_no_club_matching(information: str):
        print(f"Aucun club ayant pour information \"{information}\" existe dans la base.")

    @staticmethod
    def show_club(club_name: str, national_chest_id: str, current_club: int=-1):
        message = ""
        if current_club != -1:
            message += f"Club {current_club}: "
        message += f"Nom: {club_name}\tID: {national_chest_id}"
        print(message)

    @staticmethod
    def show_empty_club_list():
        print("La liste des clubs est vide.")

    def get_new_club_name(self):
        self.show_border()
        return input("Quel est son nouveau nom ? : ")

    def get_confirm_choice(self, name, id):
        self.show_border()
        return input(f"S'agit-il bien du club \"{name} - {id}\" ? (O/N) : ").capitalize()

    @staticmethod
    def show_modified_club(new_name: str):
        print(f"Le nom du club a bien été changé en \"{new_name}\".")

    @staticmethod
    def show_club_exist(national_chest_id):
        print(f"Création impossible: Un club ayant pour identifiant \"{national_chest_id}\" existe déjà dans la base de données.")

    @staticmethod
    def show_no_club_exist_with_name(club_name):
        print(f"Aucun club ayant pour nom \"{club_name}\" existe dans la base de données.")


    def get_club_player(self):
        return self._get_user_input(
            "Quel est le numéro correspondant au club du joueur ? : "
        )
    
    def get_club_to_modify(self):
        return self._get_user_input(
            "Quel est le numéro du club à modifier ? : "
        )
    
    def _get_user_input(self, message):
        self.show_border()
        self._show_empty_to_back()
        return input(message)
    
    @staticmethod
    def _show_empty_to_back():
        print("(Laissez vide pour revenir au menu)")