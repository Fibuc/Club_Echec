from Models.matchmodel import MatchModel
from Views.matchview import MatchView
from Models.playermodel import PlayerModel

import helpers

PLAYER_PER_MATCH = 2
COLORS = ["Blanc", "Noir"]
MATCH_RESULT_OPTIONS = ["1", "2", "3"]


class MatchController:
    """Contrôleur des matchs"""
    def __init__(self, match_view=MatchView(), match_model=MatchModel()):
        """Initialise le contrôleur avec la vue et le modèle.

        Args:
            match_view (MatchView, optional): Vue du match. Defaults to MatchView().
            match_model (MatchModel, optional): Modèle du match. Defaults to MatchModel().
        """
        self.match_view = match_view
        self.match_model = match_model

    def get_matches(
        self, current_round: int, players: list,
        all_matches_played: list, players_bye: list
    ) -> list:
        """
        Récupère et retourne la liste des matchs.

        Args:
            current_round (int): Numéro du round actuel.
            players (list): Liste des joueurs.

        Returns:
            list: Retourne la liste des matchs
        """
        return self.evaluate_type_match(current_round, players, all_matches_played, players_bye)

    def evaluate_type_match(
        self, current_round: int, players: list,
        all_matches_played: list, players_bye: list
    ) -> list:
        """
        Lance le type de match selon le round actuel.

        Args:
            current_round (int): Numéro du round actuel.
            players (list): Liste des joueurs.

        Returns:
            list: Retourne la liste des matchs.
        """
        number_matches = len(players) // PLAYER_PER_MATCH
        if current_round == 1:
            return self.random_matches(players, number_matches, all_matches_played, players_bye)
        else:
            return self.matches_by_elo(players, number_matches, all_matches_played, players_bye)

    def random_matches(
        self, players: list[PlayerModel], number_matches: int,
        all_matches_played: list, players_bye: list
    ) -> list:
        """
        Génère et retourne des matchs aléatoires entre les joueurs.

        Args:
            players (list[PlayerModel]): Liste des joueurs.
            number_matches (int): Nombre de matchs.
            all_matches_played (list): Liste des matchs déjà joués.
            players_bye (list): Liste des joueurs bye.

        Returns:
            list: Liste des matchs.
        """
        round_player_bye = self.bye_player_if_odd(players, players_bye)
        matches = []
        for _ in range(number_matches):
            helpers.shuffle_element(players)
            player_1 = players.pop()
            player_2 = players.pop()
            match = self.create_new_match(player_1, player_2)
            matches.append(match)
            self.add_to_match_played(player_1, player_2, all_matches_played)

        self.prepare_match_to_show(matches, round_player_bye)

        return matches

    def matches_by_elo(
        self, players: list[PlayerModel], number_matches: int,
        all_matches_played: list, players_bye: list
    ) -> list:
        """
        Génère et retourne des matchs selon le elo de chaque joueur.

        Args:
            players (list[PlayerModel]): Liste des joueurs.
            number_matches (int): Nombre de matchs.
            all_matches_played (list): Liste des matchs déjà joués.
            players_bye (list): Liste des joueurs bye.

        Returns:
            list: Liste des matchs.
        """
        round_player_bye = self.bye_player_if_odd(players, players_bye)
        matches = []
        max_test_number = 50
        found = False
        test = 0
        while not found:
            restart = False
            helpers.shuffle_element(players)
            sorted_players = self.sort_by_elo(players)
            for _ in range(number_matches):
                match = self.generate_ranked_match(sorted_players, all_matches_played)
                if not match:
                    test += 1
                    if test < max_test_number:
                        restart = True
                        break
                    else:
                        match = self.generate_already_played_match(sorted_players)

                matches.append(match)

            if restart:
                matches.clear()
                continue

            found = True
            for match in matches:
                players_match = [
                    player
                    for player in players
                    if player.full_name in [match[0][0], match[1][0]]
                ]
                self.add_to_match_played(players_match[0], players_match[1], all_matches_played)

        self.prepare_match_to_show(matches, round_player_bye)

        return matches

    def get_concurrent(
        self, player_1: PlayerModel, players: list[PlayerModel],
        all_matches_played: list
    ) -> PlayerModel | None:
        """Retourne l'adversaire du joueur pour le prochain match après avoir
        vérifié qu'ils ne se sont pas déjà affronté.

        Args:
            player_1 (PlayerModel): Joueur en attente d'adversaire.
            players (list[PlayerModel]): Liste de tous les participants.
            all_matches_played (list): Liste de tous les matchs déjà joués.

        Returns:
            PlayerModel | None: Si trouvé, retourne le joueur. Si aucun
            adversaire disponible, retourne None.
        """
        already_played = {
            match[1]
            for match in all_matches_played
            if match[0] == player_1.full_name
        }
        concurrents_names = {player.full_name for player in players if player.full_name != player_1.full_name}
        available_concurrent = concurrents_names - already_played
        for player in players:
            if player.full_name in available_concurrent:
                return player

    def get_winner(self, player_1: PlayerModel, player_2: PlayerModel):
        """
        Récupère le résultat du match et associe les points.

        Args:
            player_1 (PlayerModel): Premier joueur.
            player_2 (PlayerModel): Deuxième joueur.
        """
        valid_choice = False
        while not valid_choice:
            result = self.match_view.get_result_of_match(player_1.full_name, player_2.full_name)
            if result in MATCH_RESULT_OPTIONS:
                match result:
                    case "1":
                        self.add_score_to_player(player_1)
                        valid_choice = True
                    case "2":
                        self.add_score_to_player(player_2)
                        valid_choice = True
                    case "3":
                        self.add_score_to_player(player_1, player_2)
                        valid_choice = True
            else:
                self.match_view.show_error_message_choice(result)
                helpers.sleep_a_few_seconds()

    def add_score_to_player(self, player_1: PlayerModel, player_2: PlayerModel = None):
        """
        Ajoute le résultat au points des joueurs. L'option "player_2" permet
        d'associer le résultat au deux joueurs en cas d'égalité.

        Args:
            player_1 (PlayerModel): Joueur vainqueur ou premier joueur.
            player_2 (PlayerModel, optional): Deuxième joueur. Défaut None.
        """
        if player_2:
            player_1.points += 0.5
            player_2.points += 0.5
            helpers.convert_if_integer(player_1.points)
            helpers.convert_if_integer(player_2.points)
        else:
            player_1.points += 1
            helpers.convert_if_integer(player_1.points)

    def create_new_match(
            self, player_1: PlayerModel, player_2: PlayerModel
    ) -> tuple:
        """
        Crée un nouveau match avec les deux joueurs.

        Args:
            player_1 (PlayerModel): Instance PlayerModel du premier joueur.
            player_2 (PlayerModel): Instance PlayerModel du deuxième joueur.

        Returns:
            tuple: Tuple représentant le match.
        """
        return self.match_model.create_match(
            player_1_name=player_1.full_name,
            player_2_name=player_2.full_name,
            player_1_points=player_1.points,
            player_2_points=player_2.points
        )

    def prepare_match_to_show(
        self, matches: list, player_bye_name: str | None
    ):
        """
        Prépare les matchs du round pour l'affichage à l'utilisateur.

        Args:
            matches (list): Liste des matchs du round.
            player_bye_name (str | None): Nom du joueur étant en bye ce round.
            "None" si le nombre de participants est pair.
        """
        for i, match in enumerate(matches):
            player_1_name = match[0][0]
            player_1_points = match[0][1]
            player_2_name = match[1][0]
            player_2_points = match[1][1]
            player_1_color, player_2_color = self._color_choice()
            self.match_view.show_match(
                player_1_name=player_1_name, player_1_points=player_1_points,
                player_1_color=player_1_color, player_2_name=player_2_name,
                player_2_points=player_2_points,
                player_2_color=player_2_color, current_match=i+1
            )
        if player_bye_name:
            self.match_view.show_player_bye(player_bye_name)

        self.match_view.waiting_user_continuation()

    @staticmethod
    def sort_by_elo(players: list[PlayerModel]) -> list[PlayerModel]:
        """
        Trie la liste des joueurs dans l'ordre décroissant de leur score.

        Args:
            players (list[PlayerModel]): Liste des joueurs.

        Returns:
            list[PlayerModel]: Liste des joueurs triée.
        """
        return sorted(players, key=lambda player: -player.points)

    @staticmethod
    def _color_choice() -> tuple[str, str]:
        """
        Génère aléatoirement une couleur à chaque joueur.

        Returns:
            tuple[str, str]: Tuple des couleurs.
        """
        colors = COLORS[:]
        helpers.shuffle_element(colors)
        first_color = colors.pop()
        second_color = colors.pop()
        return first_color, second_color

    def add_to_match_played(
        self, player_1: PlayerModel, player_2: PlayerModel,
        all_matches_played: list[tuple[str, str]]
    ):
        """
        Ajoute le match aux matchs déjà joués

        Args:
            player_1 (PlayerModel): Premier joueur.
            player_2 (PlayerModel): Deuxième joueur.
            all_matches_played (list[tuple[str, str]]): Liste de tous les
            matchs déjà joués.
        """
        match = player_1.full_name, player_2.full_name
        all_matches_played.extend((match, match[::-1]))

    def generate_ranked_match(
        self, players: list[PlayerModel],
        all_matches_played: list[tuple[str, str]]
    ) -> tuple | None:
        """Génère les matchs non joués selon le elo des joueurs.

        Args:
            players (list[PlayerModel]): Liste des joueurs.
            all_matches_played (list[tuple[str, str]]): Liste de tous les
            matchs déjà joués.

        Returns:
            tuple | None: Retourne le match si un adversaire a été trouvé,
            sinon None.
        """
        player_1 = players[0]
        if player_2 := self.get_concurrent(
            player_1, players, all_matches_played
        ):
            match = self.create_new_match(player_1, player_2)
            self.remove_from_players_to_pairing(players, player_1, player_2)
            return match

        return

    def generate_already_played_match(
        self, players: list[PlayerModel]
    ) -> tuple:
        """Génère un match déjà joué si le joueur ne pas peut jouer contre
        d'autres adversaires.

        Args:
            players (list[PlayerModel]): Liste de tous les joueurs.

        Returns:
            tuple: Tuple correspondant au match.
        """
        player_1 = players[0]
        player_2 = players[1]
        self.remove_from_players_to_pairing(players, player_1, player_2)
        return self.create_new_match(player_1, player_2)

    def remove_from_players_to_pairing(
        self, players: list[PlayerModel], player_1: PlayerModel,
        player_2: PlayerModel
    ):
        """Retire le la liste des joueurs ceux étant déjà appariés.

        Args:
            players (list[PlayerModel]): Liste de tous les joueurs.
            player_1 (PlayerModel): Premier joueur.
            player_2 (PlayerModel): Deuxième joueur.
        """
        players.remove(player_1)
        players.remove(player_2)

    def bye_player_if_odd(
        self, players: list[PlayerModel], players_bye: list
    ) -> str | None:
        """
        Bye un joueur en le retirant aléatoirement de la liste des joueurs si
        les participants sont impairs. Ce choix est aléatoire entre les
        joueurs les plus faibles.

        Les joueurs ayant déjà été en bye ne peuvent pas l'être une seconde
        fois.

        Args:
            players (list[PlayerModel]): Liste de tous les joueurs.
            players_bye (list): Liste des joueurs bye.

        Returns:
            str | None: Nom du joueur bye si impair, sinon None.
        """
        if len(players) % 2 != 0:
            helpers.shuffle_element(players)
            sorted_players = self.sort_by_elo(players)[::-1]
            for player in sorted_players:
                if player.full_name not in players_bye:
                    players_bye.append(player.full_name)
                    players.remove(player)
                    return player.full_name
