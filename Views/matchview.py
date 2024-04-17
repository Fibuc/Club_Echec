import config


class MatchView:
    """Classe vue des matchs"""
    def get_result_of_match(self, player_1: str, player_2: str) -> str:
        """Affiche les opposants du match et retourne le résultat.

        Args:
            player_1 (str): Nom du premier opposant.
            player_2 (str): Nom du deuxième opposant.

        Returns:
            str: Choix de l'utilisateur.
        """
        print(f"{config.SPACE}Dans le match qui a opposé, le vainqueur est :"
              f"\n{config.BORDER}\n1 - {player_1}"
              f"\n2 - {player_2}\n3 - Match nul\n{config.BORDER}"
              )
        return input("Quel est votre choix ? : ")

    @staticmethod
    def show_error_message_choice(user_choice: str):
        """Affiche un message d'erreur indiquant que le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(f"Erreur: La commande \"{user_choice}\" "
              f"n'est pas une commande valide."
              )

    def show_match(
            self, player_1_name: str, player_1_points: float,
            player_1_color: str, player_2_name: str, player_2_points: float,
            player_2_color: str, current_match: int
    ):
        """
        Affiche les détails d'un match entre deux joueurs.

        Args:
            player_1_name (str): Nom du premier joueur.
            player_1_points (float): Points du premier joueur.
            player_1_color (str): Couleur du premier joueur.
            player_2_name (str): Nom du deuxième joueur.
            player_2_points (float): Points du deuxième joueur.
            player_2_color (str): Couleur du deuxième joueur.
            current_match (int): Numéro du match en cours.
        """
        print(
            f"\nMatch {current_match}: \n\tJoueur 1: {player_1_name} "
            f"({player_1_points} pts) Couleur: {player_1_color} \n\t"
            f"Joueur 2: {player_2_name} ({player_2_points} pts) Couleur: "
            f"{player_2_color}."
        )

    @staticmethod
    def waiting_user_continuation():
        """
        Attend que l'utilisateur appuie sur une touche pour continuer.
        """
        input("Appuyez sur une touche pour continuer : ")

    @staticmethod
    def show_player_bye(player_name: str):
        """
        Affiche le joueur qui est bye pour le round.

        Args:
            player_name (str): Nom du joueur bye.
        """
        print(f"\nJoueur bye ce round: {player_name}.\n")
