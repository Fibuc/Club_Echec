from typing import Callable

import helpers

class TournamentView:

    @staticmethod
    def show_menu(
        menu_function: Callable,
        menu_name: str,
        options_menu: list,
        participants: list
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
        full_menu = decoration(menu_name, options_menu, participants)
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

    def get_tournament_name(self):
        return input("Quel est le nom du tournois ? : ")

    def get_tournament_location(self):
        return input("Quel est le lieu du tournois ? : ")

    def show_tournament_created(self, name, location):
        print(f"Le tournois \"{name}\" de {location} a bien été créé")

    def get_user_choice(self):
        return input("Quel est votre choix ? : ")

    def show_all_tournaments(self, result_list: list, numbering: bool=False):
        self._show_border()
        self._show_number_of_tournaments_found(result_list)
        self._show_border()
        current_tournament = 0
        for result in result_list:
            if numbering:
                current_tournament += 1
                print(f"Tournois {current_tournament}: \t{result}")
            else:
                print(result)

        self._show_border()

    @staticmethod
    def _show_number_of_tournaments_found(result_list: list):
        result_numer = len(result_list)
        plural_choice = (
            f"{'s ont été trouvés.' if result_numer > 1 else " a été trouvé."}"
        )
        print(f"Résultat: {result_numer} tournoi{plural_choice} ")

    @staticmethod
    def _show_border():
        print(helpers.BORDER)


class MatchView:

    def show_match(self, match, current_match):
        first_player_name = match[0][0]
        first_player_point = match[0][1]
        second_player_name = match[1][0]
        second_player_point = match[1][1]
        print(
            f"Match {current_match} - {first_player_name} "
            f"({first_player_point} pts) VS {second_player_name} "
            f"({second_player_point} pts)."
        )

    def get_result_of_match(self, player_1, player_2):
        print(f"{helpers.SPACE}Dans le match qui a opposé :"
              f"\n{helpers.BORDER}\n1 - {player_1}"
              f"\n2 - {player_2}\n3 - Match nul\n{helpers.BORDER}"
        )
        return input("Qui a gagné le match ? (1/3) : ")

    def show_error_message(self, user_choice):
        print(f"La commande \"{user_choice}\" n'est pas valide.")


class RoundView:
    @staticmethod
    def show_menu(
        menu_function: Callable,
        menu_name: str,
        options_menu: list,
        current_round: int
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
        full_menu = decoration(menu_name, options_menu, current_round)
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
        print(f"Erreur: La commande \"{user_choice}\" n'est pas une commande valide.")