from typing import Callable

import helpers


class RoundView:
    """Classe vue des Rounds."""
    @staticmethod
    def show_menu(
        menu_function: Callable,
        menu_name: str,
        options_menu: list,
        current_round: int,
        can_undo: bool
    ):
        """
        Affiche le menu des rounds formaté.

        Args:
            menu_function (Callable): Fonction comprenant le menu.
            menu_name (str): Nom du menu.
            options_menu (list): Liste des options du menu.
            current_round (int): Numéro du round en cours.
            can_undo (bool): Possibilité de l'utilisateur à revenir en
            arrière.
        """
        decoration = helpers.decorative_menu_element(
            function=menu_function,
            description=current_round
        )
        full_menu = decoration(menu_name, options_menu, can_undo)
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
            f"Erreur: La commande \"{user_choice}\" n'est pas une "
            f"commande valide."
        )

    def show_round(
        self, current_round: int, start_date: str,
        end_date: str, matches: list, player_bye: str
    ):
        """
        Affiche les informations du round.

        Args:
            current_round (int): Numéro du round actuel.
            start_date (str): Date de début du round.
            end_date (str): Date de fin du round.
            matches (list): Liste des matchs.
            player_bye (str): Joueur bye dans le round.
        """
        print(
            f"Round {current_round}:\n\tDébut: {start_date}"
            f"\n\tFin: {end_date}"
            f"{f"\n\tJoueur bye: {player_bye}" if player_bye else ""}"
            f"\n\tMatchs:"
        )
        self._show_matches(matches)

    @staticmethod
    def _show_matches(matches: list):
        """
        Formate et affiche les matches du round.

        Args:
            matches (list): Liste des matchs.
        """
        for i, match in enumerate(matches, start=1):
            print(
                f"\t\t{i} - {match[0][0]} ({match[0][1]} pts) contre "
                f"{match[1][0]} ({match[1][1]} pts)"
            )
        print()
