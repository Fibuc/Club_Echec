from typing import Callable

import config
import helpers

EDITABLE_INFORMATIONS_PLAYER = [
        "Le prénom",
        "Le nom de famille",
        "La date de naissance",
        "Le club"
]


class PlayerView:
    """Classe vue du Joueur"""
    @staticmethod
    def get_menu_user_choice() -> str:
        """
        Retourne le choix de l'utilisateur.

        Returns:
            str: Choix de l'utilisateur
        """
        return input("Quel est votre choix ? : ")

    @staticmethod
    def get_new_player_name() -> tuple[str, str]:
        """
        Récupère et retourne le prénom et le nom de famille du joueur.

        Returns:
            tuple[str, str]: Prénom du joueur, Nom de famille du joueur.
        """
        first_name = input("Quel est le prénom du joueur ? : ").capitalize()
        last_name = input("Quel est le nom de famille du joueur ? : ").capitalize()
        return first_name, last_name

    @staticmethod
    def get_new_player_birth_date() -> str:
        """
        Récupère et retourne la date de naissance du joueur.

        Returns:
            str: Date de naissance du joueur.
        """
        return input("Quelle est sa date de naissance ? (JJ/MM/AAAA): ")

    @staticmethod
    def get_new_player_participation() -> str:
        """
        Récupère et retourne la participation du joueur au prochain
        tournoi.

        Returns:
            str: Participation au prochain tournoi.
        """
        return input("Participera-t-il au prochain tournois ? (O/N) : ")

    def get_first_name(self) -> str:
        """
        Récupère et retourne le prénom du joueur.

        Returns:
            str: Prénom du joueur.
        """
        self._show_border()
        return input(
            "(Laissez vide pour afficher tous les joueurs)\n"
            "Quel est le prénom du joueur ? : "
        )

    @staticmethod
    def get_index_player_to_modify() -> str:
        """
        Récupère et retourne le numéro du joueur à modifier.

        Returns:
            str: Numéro du joueur.
        """
        return input(
            "(Laissez vide pour revenir au menu)\n"
            "Quel est le numéro du joueur à modifier ? : "
        )

    def get_information_to_modify(self) -> str:
        """
        Récupère et retourne l'information du joueur à modifier.

        Returns:
            str: Information du joueur.
        """
        self._show_border()
        return input("Quel est l'information du joueur à modifier ? : ")

    @staticmethod
    def get_new_value() -> str:
        """
        Récupère et retourne la nouvelle valeur de l'information du joueur
        pour la modification.

        Returns:
            str: Nouvelle valeur de l'information du joueur.
        """
        return input("Quelle est la nouvelle valeur ? : ")

    @staticmethod
    def show_menu(
        menu_function: Callable, menu_name: str, options_menu: list
    ):
        """
        Affiche le menu joueur formaté.

        Args:
            menu_function (Callable): Fonction comprenant le menu.
            menu_name (str): Nom du menu.
            options_menu (list): Liste des options du menu.
        """
        decoration = helpers.decorative_menu_element(function=menu_function)
        full_menu = decoration(menu_name, options_menu)
        print(full_menu)

    @staticmethod
    def show_error_message_choice(user_choice: str):
        """
        Affiche un message d'erreur indiquant que le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(f"Erreur: La commande \"{user_choice}\" n'est pas une commande valide.")

    def show_players(self, players: list, numbering: bool = False):
        """
        Affiche les information des joueurs.
        L'option numbering permet la numération des joueurs.

        Args:
            players (list): Liste des joueurs.
            numbering (bool, optional): Numération des joueurs. Défaut False.
        """
        self._show_number_of_player_found(players)
        self._show_border()
        current_player = 0
        for player in players:
            if numbering:
                current_player += 1
                print(f"Joueur {current_player}: {player}")
            else:
                print(player)

        self._show_border()

    @staticmethod
    def show_new_player_created(player_name: str):
        """
        Affiche un message indiquant que le joueur a été créé.

        Args:
            player_name (str): Nom du joueur.
        """
        print(f"Le nouveau joueur \"{player_name}\" a bien été créé.")

    @staticmethod
    def show_no_match_player_found(first_name: str):
        """
        Affiche un message d'erreur indiquant qu'il n'y a aucun joueur ayant
        ce prénom dans la base de données.

        Args:
            first_name (str): Prénom du joueur.
        """
        print(f"Il n'y a aucun joueur ayant pour prénom \"{first_name}\" dans la base de données.")

    @staticmethod
    def show_informations_type():
        """Affiche la liste des informations modifiables du joueur."""
        print("Liste des informations :")
        for i, information in enumerate(EDITABLE_INFORMATIONS_PLAYER, start=1):
            print(f"{i} - {information}")

    def show_title_players(self):
        self._show_border()
        print("Liste des joueurs")
        self._show_border()

    def show_valid_modifications(self):
        """Affiche un message indiquant que la modification est un succès."""
        self._show_border()
        print("Validé! Le joueur à bien été modifié.")

    @staticmethod
    def show_error_date(birth_date: str):
        """
        Affiche un message d'erreur indiquant que la date de naissance n'est
        pas au bon format.

        Args:
            birth_date (str): Date de naissance du joueur.
        """
        print(f"Date \"{birth_date}\" invalide. Le format doit être en JJ/MM/AAAA.")

    @staticmethod
    def _show_number_of_player_found(result_list: list):
        """
        Affiche un message indiquant le nombre de joueurs trouvés.

        Args:
            result_list (list): Liste des joueurs.
        """
        result_numer = len(result_list)
        plural_choice = (
            f"{'s ont été trouvés.' if result_numer > 1 else ' a été trouvé.'}"
        )
        print(f"Résultat: {result_numer} joueur{plural_choice} ")

    @staticmethod
    def _show_border():
        """Affiche une bordure."""
        print(config.BORDER)

    @staticmethod
    def show_error_empty_names():
        print("Erreur: Le prénom ou le nom de famille ne peuvent pas être vides.")

    @staticmethod
    def show_error_characteres_names():
        print(
            "Erreur: Le nom ou prénom d'un joueur ne peuvent pas "
            "contenir de chiffres ou de caractères spéciaux."
        )
