import helpers

class MatchView:

    def get_result_of_match(self, player_1, player_2):
        print(f"{helpers.SPACE}Dans le match qui a opposé, le vainqueur est :"
              f"\n{helpers.BORDER}\n1 - {player_1}"
              f"\n2 - {player_2}\n3 - Match nul\n{helpers.BORDER}"
        )
        return input("Quel est votre choix ? (1/3) : ")

    @staticmethod
    def show_all_match_played():
        print("Tous les matchs ont été joués.")
    
    @staticmethod
    def show_error_message_choice(user_choice: str):
        """Affiche un message d'erreur lorsque le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(f"Erreur: La commande \"{user_choice}\" n'est pas une commande valide.")

    def show_match(
            self, player_1_name: str, player_1_points: float,
            player_1_color: str, player_2_name: str, player_2_points: float,
            player_2_color: str, current_match: int
    ):
        print(
            f"\nMatch {current_match}: \n\tJoueur 1: {player_1_name} "
            f"({player_1_points} pts) Couleur: {player_1_color} \n\t"
            f"Joueur 2: {player_2_name} ({player_2_points} pts) Couleur: "
            f"{player_2_color}."
        )

    @staticmethod
    def waiting_user_continuation():
        input("Appuyez sur une touche pour continuer : ")