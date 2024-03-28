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