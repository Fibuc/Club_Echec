from typing import Callable

import config
import helpers


class ClubView:
    """Classe vue du club"""
    @staticmethod
    def show_menu(
        menu_function: Callable, menu_name: str, options_menu: list
    ):
        """
        Affiche le menu club formaté.

        Args:
            menu_function (Callable): Fonction comprenant le menu.
            menu_name (str): Nom du menu.
            options_menu (list): Liste des options du menu.
        """
        decoration = helpers.decorative_menu_element(function=menu_function)
        full_menu = decoration(menu_name, options_menu)
        print(full_menu)

    @staticmethod
    def get_menu_user_choice() -> str:
        """
        Récupère et retourne le choix de l'utilisateur.

        Returns:
            str: Choix de l'utilisateur
        """
        return input("Quel est votre choix ? : ")

    @staticmethod
    def show_error_message_choice(user_choice: str):
        """
        Affiche un message d'erreur lorsque le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(
            f"Erreur: La valeur \"{user_choice}\" n'est "
            f"pas une commande valide."
        )

    @staticmethod
    def show_border():
        """Affiche une bordure."""
        print(config.BORDER)

    def get_club_informations(self) -> tuple[str, str]:
        """
        Récupère et retourne le nom et l'identifiant du club.

        Returns:
            tuple: Informations du club
        """
        self.show_border()
        club_name = input("Quel est le nom du club ? : ")
        national_chest_id = input("Quel est sont identifiant national ? : ")
        return club_name, national_chest_id

    @staticmethod
    def show_created_club(club_name: str):
        """
        Affiche que le club a bien été créé.

        Args:
            club_name (str): Nom du club.
        """
        print(f"Le club \"{club_name}\" a bien été créé.")

    @staticmethod
    def show_error_national_chest_id(national_chest_id: str):
        """
        Affiche une erreur indiquant que le identifiant national du club
        est invalide.

        Args:
            national_chest_id (str): Identifiant national du club.
        """
        print(
            f"Le numéro d'identifiant national \"{national_chest_id}\" "
            f"n'est pas correct."
        )

    @staticmethod
    def show_error_empty_name():
        """
        Affiche une erreur indiquant que le nom du club ne peut pas être vide.
        """
        print("Erreur: Le nom du club ne peut pas être vide.")

    @staticmethod
    def show_club(
        club_name: str, national_chest_id: str, current_club: int = -1
    ):
        """
        Affiche le nom et l'identifiant national du club.
        L'option current_club permet d'afficher les numéros des clubs.

        Args:
            club_name (str): Le nom du club.
            national_chest_id (str): L'identifiant national du club.
            current_club (int, optional): Le numéro du club actuel.
            Défaut -1.
        """
        message = ""
        if current_club != -1:
            message += f"Club {current_club}: "
        message += f"Nom: {club_name}\tID: {national_chest_id}"
        print(message)

    @staticmethod
    def show_empty_club_list():
        """Affiche un message indiquant que la liste des clubs est vide."""
        print("La liste des clubs est vide.")

    def get_new_club_name(self) -> str:
        """
        Récupère et retourne le nouveau nom du club.

        Returns:
            str: Nouveau nom du club.
        """
        self.show_border()
        return input("Quel est son nouveau nom ? : ")

    @staticmethod
    def show_modified_club(new_name: str):
        """
        Affiche un message indiquant que le nom du club a été changé avec
        succès.

        Args:
            new_name (str): Nouveau nom du club.
        """
        print(f"Le nom du club a bien été changé en \"{new_name}\".")

    @staticmethod
    def show_club_exist(national_chest_id: str):
        """
        Affiche une erreur indiquant que la création du club est impossible
        car il existe déjà dans la base de données.

        Args:
            national_chest_id (str): Identifiant national du club.
        """
        print(
            f"Création impossible: Un club ayant pour identifiant "
            f"\"{national_chest_id}\" existe déjà dans la base de données."
        )

    def get_club_player(self) -> str:
        """
        Retourne le numéro correspondant au club du joueur.

        Returns:
            str: Le numéro correspondant au club du joueur.
        """
        return self._get_user_input(
            "Quel est le numéro correspondant au club du joueur ? : "
        )

    def get_club_to_modify(self) -> str:
        """
        Retourne le numéro du club à modifier.

        Returns:
            str: Le numéro du club à modifier.
        """
        return self._get_user_input(
            "Quel est le numéro du club à modifier ? : "
        )

    def _get_user_input(self, message: str) -> str:
        """
        Formate l'affichage et retourne le choix de l'utilisateur.

        Args:
            message (str): Message à afficher pour l'entrée utilisateur.

        Returns:
            str: L'entrée utilisateur.
        """
        self.show_border()
        self._show_empty_to_back()
        return input(message)

    @staticmethod
    def _show_empty_to_back():
        """
        Affiche un message indiquant de laisser vide pour revenir au menu.
        """
        print("(Laissez vide pour revenir au menu)")
