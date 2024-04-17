class MatchModel:
    """Classe modèle des matchs."""
    def create_match(
            self, player_1_name: str, player_2_name: str,
            player_1_points: int | float, player_2_points: int | float
    ) -> tuple:
        """Crée un match et le retourne sous forme de tuple.

        Args:
            player_1_name (str): Nom du premier joueur.
            player_2_name (str): Nom du deuxième joueur.
            player_1_points (int | float): Points du premier joueur.
            player_2_points (int | float): Points du deuxième joueur.

        Returns:
            tuple: Match de ces joueurs.
        """
        match = (
            [player_1_name, player_1_points],
            [player_2_name, player_2_points]
        )
        return tuple(match)
