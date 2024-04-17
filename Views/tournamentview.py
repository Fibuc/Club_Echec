from typing import Callable

import config
import helpers


class TournamentView:

    @staticmethod
    def show_menu(
        menu_function: Callable,
        menu_name: str,
        options_menu: list,
        participants: list
    ):
        """
        Affiche le menu des tournois formaté.

        Args:
            menu_function (Callable): Fonction comprenant le menu.
            menu_name (str): Nom du menu.
            options_menu (list): Liste des options du menu.
            participants (list): Liste des participants.
        """
        decoration = helpers.decorative_menu_element(
            function=menu_function, description=participants
            )
        full_menu = decoration(menu_name, options_menu)
        print(full_menu)

    def get_menu_user_choice(self) -> str:
        """
        Récupère et retourne le choix de l'utilisateur.

        Returns:
            str: Choix de l'utilisateur
        """
        return input("Quel est votre choix ? : ")

    @staticmethod
    def show_error_message_choice(user_choice: str):
        """
        Affiche un message d'erreur indiquant que le choix de l'utilisateur
        est incorrect.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(
            f"Erreur: La valeur \"{user_choice}\" n'est pas "
            f"une commande valide."
        )

    @staticmethod
    def get_tournament_name() -> str:
        """
        Récupère et retourne le nom du tournoi.

        Returns:
            str: Nom du tournoi.
        """
        return input("Quel est le nom du tournois ? : ")

    @staticmethod
    def get_tournament_location() -> str:
        """
        Récupère et retourne le lieu du tournoi.

        Returns:
            str: Lieu du tournoi
        """
        return input("Quel est le lieu du tournois ? : ")

    @staticmethod
    def show_tournament_created(name: str, location: str):
        """Affiche un message indiquant que le tournoi à bien été créé.

        Args:
            name (str): Nom du tournoi.
            location (str): Lieu du tournoi.
        """
        print(f"Le tournois \"{name}\" de {location} a bien été créé")

    @staticmethod
    def show_tournament(tournament, current_tournament: int = -1):
        """
        Affiche les informations du tournoi. Si l'option current_tournament
        est utilisée, cela permet la numération des tournois.

        Args:
            tournament (TournamentModel): Instance de TournamentModel
            current_tournament (int, optional): Option de numération. Défaut -1.
        """
        message = ""
        if current_tournament != -1:
            message += f"Tournois {current_tournament}:\n"
        tournament = "\n".join(
            "\t" + "- " + line for line in str(tournament).split("\n")
        )
        message += f"{tournament}\n"
        print(message)

    @staticmethod
    def show_number_of_tournaments_found(number_of_tournament: int):
        """Affiche un message indiquant le nombre de tournois trouvés.

        Args:
            number_of_tournament (int): Nombre de tournois
        """
        plural_choice = (
            f"{'s trouvés.' if number_of_tournament > 1 else ' trouvé.'}"
        )
        print(f"Résultat: {number_of_tournament} tournoi{plural_choice} ")

    @staticmethod
    def _show_border():
        """Affiche une bordure."""
        print(config.BORDER)

    def show_winner(self, winner_name: str, winner_points: int | float):
        """
        Affiche le message indiquant le nom du vainqueur.

        Args:
            winner_name (str): Nom du vainqueur.
            winner_points (int | float): Points du vainqueur.
        """
        print(config.SPACE)
        self._show_border()
        print(
            f"Fin du tournoi - Vainqueur: {winner_name} avec "
            f"{winner_points} points"
        )
        self._show_border()

    @staticmethod
    def show_classification(player_name: str, player_points: int | float):
        """
        Affiche le résultat du joueur.

        Args:
            player_name (str): Nom du joueur.
            player_points (int | float): Points du joueur.
        """
        print(f"{player_name} - {player_points} points")

    def get_description(self) -> str:
        """
        Récupère et retourne les remarques du tournoi.

        Returns:
            str: Remarques du tournoi.
        """
        self._show_border()
        return input("Ecrivez des remarques générales de ce tournois : ")

    @staticmethod
    def prompt_resume_tournament(name: str, location: str) -> str:
        """
        Demande à l'utilisateur s'il veut reprendre le tournoi non terminé.

        Args:
            name (str): Nom du tournoi.
            location (str): Lieu du tournoi.

        Returns:
            str: Choix de l'utilisateur.
        """
        return input(
            f"Voulez-vous reprendre le tournoi "
            f"\"{name}\" de {location} ? (o/n) : "
        )

    @staticmethod
    def show_no_player_matching(player_name: str):
        """
        Affiche un message d'erreur indiquant qu'il n'y a pas de joueur
        correspondant à la recherche.

        Args:
            player_name (str): Nom du joueur.
        """
        print(
            f"Il n'y a aucun joueur existant ayant pour nom "
            f"\"{player_name}\" dans la base de données"
        )

    @staticmethod
    def get_confirm_choice() -> str:
        """
        Demande à l'utilisateur une confirmation pour ne pas laisser
        de remarques pour le tournoi.

        Returns:
            str: Choix de l'utilisateur.
        """
        return input("Êtes-vous sûr de ne pas laisser de remarques ? (o/n) : ")

    @staticmethod
    def show_error_characteres_name():
        print(
            "Erreur: Le nom d'un tournois ou le lieu ne peuvent pas "
            "contenir de caractères spéciaux."
        )

    @staticmethod
    def show_error_empty_name():
        """
        Affiche un message d'erreur indiquant que le nom ou le lieu du
        tournoi de peuvent pas être vides.
        """
        print("Erreur: Le nom du tournois ou le lieu ne peuvent pas être vides.")

    @staticmethod
    def show_not_enough_participants(number_of_participants: int):
        """
        Affiche un message d'erreur indiquant que le nombre minimum de
        joueur pour lancer le tournoi n'est pas atteint.

        Args:
            number_of_participants (int): Nombre de participants.
        """
        print(
            f"Erreur: Il faut minimum {config.MINIMUM_PLAYER_FOR_TOURNAMENT} "
            f"participants pour lancer un tournoi. Actuellement "
            f"{number_of_participants} participants.")
