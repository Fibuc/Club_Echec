from typing import Callable

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
        print(helpers.BORDER)

    @staticmethod
    def back_to_line():
        print(helpers.BACK_TO_LINE)

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
    def show_no_club_matching(information: str):
        print(f"Aucun club ayant pour information \"{information}\" existe dans la base.")

    @staticmethod
    def show_club_informations(club_name: str, national_chest_id: str):
        print(f"ID : {national_chest_id} - Nom du club : {club_name}")

    @staticmethod
    def show_empty_club_list():
        print("La liste des clubs est vide.")


    def get_club_to_modify(self):
        self.show_border()
        return input("Quel est le nom ou l'ID du club à modifier ? : ")

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