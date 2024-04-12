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
        decoration = helpers.decorative_menu_element(
            function=menu_function, description=participants
            )
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

    def get_tournament_name(self):
        return input("Quel est le nom du tournois ? : ")

    def get_tournament_location(self):
        return input("Quel est le lieu du tournois ? : ")

    def show_tournament_created(self, name, location):
        print(f"Le tournois \"{name}\" de {location} a bien été créé")

    def get_user_choice(self):
        return input("Quel est votre choix ? : ")

    def show_tournament(self, tournament, current_tournament: int=-1):
        message = ""
        if current_tournament != -1:
            message += f"Tournois {current_tournament}:\n"
        tournament = "\n".join("\t" + "- " + line for line in str(tournament).split("\n"))
        message += f"{tournament}\n"
        print(message)

    @staticmethod
    def show_number_of_tournaments_found(number_of_tournament: int):
        plural_choice = (
            f"{'s trouvés.' if number_of_tournament > 1 else ' trouvé.'}"
        )
        print(f"Résultat: {number_of_tournament} tournoi{plural_choice} ")

    @staticmethod
    def _show_border():
        print(config.BORDER)

    def show_winner(self, winner_name, winner_points):
        print(config.SPACE)
        self._show_border()
        print(f"Fin du tournoi - Vainqueur: {winner_name} avec {winner_points} points")
        self._show_border()
    
    def show_classification(self, player_name, player_points):
        print(f"{player_name} - {player_points} points")

    def get_description(self):
        self._show_border()
        return input("Ecrivez des remarques générales de ce tournois : ")
    
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
    
    @staticmethod
    def get_confirm_choice():
        return input("Êtes-vous sûr de ne pas laisser de remarques ? (o/n) : ")
    
    @staticmethod
    def show_error_characteres_name():
        print(
            "Erreur: Le nom d'un tournois ou le lieu ne peuvent pas "
            "contenir de caractères spéciaux."
        )
    
    @staticmethod
    def show_error_empty_name():
        print("Erreur: Le nom du tournois ou le lieu ne peuvent pas être vides.")

    @staticmethod
    def show_not_enough_participants(number_of_participants):
        print(
            f"Erreur: Il faut minimum {config.MINIMUM_PLAYER_FOR_TOURNAMENT} "
            f"participants pour lancer un tournoi. Actuellement "
            f"{number_of_participants} participants.")