from Models.matchmodel import MatchModel
from Views.matchview import MatchView
from Models.playermodel import PlayerModel

import helpers

PLAYER_PER_MATCH = 2
COLORS = ["Blanc", "Noir"]
OPTIONS_WINNER = ["1", "2", "3"]

class MatchController:
    """Contrôleur des matchs"""
    def __init__(self, match_view=MatchView(), match_model=MatchModel()):
        self.match_view=match_view
        self.match_model=match_model
    
    def get_matches(self, current_round: int, players: list, all_matches_possible) -> list:
        """Récupère retourne les matchs.

        Args:
            current_round (int): Numéro du round actuel.
            players (list): Liste des joueurs.

        Returns:
            list: Retourne la liste des matchs
        """
        return self.evaluate_type_match(current_round, players, all_matches_possible)
        
    def evaluate_type_match(self, current_round: int, players: list, all_matches_possible) -> list:
        """Lance le type de match selon le round actuel.

        Args:
            current_round (int): Numéro du round actuel.
            players (list): Liste des joueurs.

        Returns:
            list: Retourne la liste des matchs.
        """
        number_matches = len(players) // PLAYER_PER_MATCH
        if current_round == 1:
            return self.random_matches(players, number_matches, all_matches_possible)
        else:
            sorted_players = self.sort_by_elo(players)
            return self.matches_by_elo(sorted_players, number_matches, all_matches_possible)

    def random_matches(self, players: list, number_matches: int, all_matches_possible: list) -> list:
        players = players
        matches = []
        for _ in range(number_matches):
            helpers.shuffle_element(players)
            player_1 = players.pop()
            player_2 = players.pop()
            match = self.create_match(player_1, player_2)
            matches.append(match)
            self._remove_match_from_matches_possible(player_1, player_2, all_matches_possible)
        
        self.prepare_match_to_show(matches)

        return matches
        
    def matches_by_elo(self, players: list, number_matches: int, all_matches_possible: list) -> list:
        matches = []
        for _ in range(number_matches):
            player_1 = players.pop(0)
            player_2 = self.get_concurrent(
                all_matches_possible,
                player_1,
                players
            )
            players.remove(player_2)
            match = self.create_match(player_1, player_2)
            matches.append(match)
            self._remove_match_from_matches_possible(player_1, player_2, all_matches_possible)

        self.prepare_match_to_show(matches)

        return matches
    
    def get_concurrent(self, matches_possible: list, player: PlayerModel, players: list) -> PlayerModel:
        concurrents = self.get_sort_concurrents(matches_possible, player, players)
        if len(concurrents) > 1:
            return self.get_random_concurrent(concurrents)
        return concurrents[0]

    def get_random_concurrent(self, concurrents: list) -> PlayerModel:
        best_concurrent_points = concurrents[0].points
        concurrents_to_shuffle = [
            concurrent
            for concurrent in concurrents
            if concurrent.points == best_concurrent_points
        ]
        helpers.shuffle_element(concurrents_to_shuffle)
        return concurrents_to_shuffle.pop()

    def get_sort_concurrents(self, matches_possible: list, player: PlayerModel, players: list) -> list:
        concurrents = self.get_all_concurrents(
            matches_possible,
            player,
            players
        )
        return self.sort_by_elo(concurrents)

    def get_all_concurrents(self, matches_possibles: list, player, players: list) -> list:
        concurrent_name = [
            match[1]
            for match in matches_possibles
            if player.get_full_name() in match[0]
        ]
        all_concurrents = [
            player
            for player in players
            if player.get_full_name() in concurrent_name
        ]
        return all_concurrents

    def get_winner(self, player_1: PlayerModel, player_2: PlayerModel):
        result = self.match_view.get_result_of_match(player_1.get_full_name(), player_2.get_full_name())
        if result in OPTIONS_WINNER:
            match result:
                case "1":
                    self.add_score_to_player(player_1)
                case "2":
                    self.add_score_to_player(player_2)
                case "3":
                    self.add_score_to_player(player_1, player_2)
        else:
            self.match_view.show_error_message_choice(result)

    def add_score_to_player(self, player_1: PlayerModel, player_2=None):
        if player_2:
            player_1.points += 0.5
            player_2.points += 0.5
        else:
            player_1.points += 1    

    def create_match(self, player_1: PlayerModel, player_2: PlayerModel) -> tuple:
        return self.match_model.create_match(
            player_1_name=player_1.get_full_name(),
            player_2_name=player_2.get_full_name(),
            player_1_points=player_1.points, 
            player_2_points=player_2.points
        )

    def prepare_match_to_show(self, matches):
        for i, match in enumerate(matches):
            self.match_view.show_match(match, i+1)

    @staticmethod
    def sort_by_elo(players: list):
        return sorted(
            players, key=lambda player:(
                -player.points,
                player.first_name,
                player.last_name
            )
        )

    @staticmethod
    def _remove_match_from_matches_possible(player_1: PlayerModel, player_2: PlayerModel, all_matches_possible: list):
        match = tuple([player_1.get_full_name(), player_2.get_full_name()])
        all_matches_possible.remove(match)
        all_matches_possible.remove(match[::-1])

    @staticmethod
    def color_choice():
        colors = copy.deepcopy(COLORS)
        first_color = helpers.shuffle_element(colors)
        second_color = colors.pop()
        return first_color, second_color

    
    