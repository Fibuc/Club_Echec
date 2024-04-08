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

    def show_tournament(self, numbering: bool=False):
        self._show_number_of_tournaments_found(result_list)
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

    def show_winner(self, winner_name, winner_points):
        print(helpers.SPACE)
        self._show_border()
        print(f"Fin du tournoi - Vainqueur: {winner_name} avec {winner_points} points")
        self._show_border()
    
    def show_classification(self, player_name, player_points):
        print(f"{player_name} - {player_points} points")

    def waiting_enter(self):
        self._show_border()
        input("Appuyez sur une touche pour quitter : ")

    def get_description(self):
        self._show_border()
        return input("Ajouter des remarques générales pour ce tournois ? : ")
    
    @staticmethod
    def prompt_resume_tournament(name, location):
        return input(
            f"Voulez-vous reprendre le tournoi "
            f"\"{name}\" de {location} ? (o/n) : "
        )
    
    @staticmethod
    def show_no_player_matching(player_name):
        print(f"Il n'y a aucun joueur existant ayant pour nom \"{player_name}\" "
              f"dans la base de données"
        )