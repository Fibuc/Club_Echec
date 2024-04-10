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
    
    def get_matches(
        self, current_round: int, players: list,
        all_matches_played: list, players_bye: list
    ) -> list:
        """Récupère et retourne les matchs.

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
        """Lance le type de match selon le round actuel.

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
        matches = []
        for _ in range(number_matches):
            helpers.shuffle_element(players)
            player_1 = players.pop()
            player_2 = players.pop()
            match = self.serialize_player_to_create_match(player_1, player_2)
            matches.append(match)
            self.add_to_match_played(player_1, player_2, all_matches_played)
        
        self.prepare_match_to_show(matches)
        if len(players) == 1:
            players_bye.append(players[0].full_name)

        return matches
        
    def matches_by_elo(
        self, players: list[PlayerModel], number_matches: int,
        all_matches_played: list, players_bye: list
    ) -> list:
        self.bye_player_if_odd(players, players_bye)
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

        self.prepare_match_to_show(matches)

        return matches
    
    def get_concurrent(self, player_1: PlayerModel, players: list, all_matches_played: list) -> list:
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
        valid_choice = False
        while not valid_choice:
            result = self.match_view.get_result_of_match(player_1.full_name, player_2.full_name)
            if result in OPTIONS_WINNER:
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

    def add_score_to_player(self, player_1: PlayerModel, player_2: PlayerModel=None):
        if player_2:
            player_1.points += 0.5
            player_2.points += 0.5
            helpers.convert_if_integer(player_1.points)
            helpers.convert_if_integer(player_2.points)
        else:
            player_1.points += 1
            helpers.convert_if_integer(player_1.points)

    def serialize_player_to_create_match(
            self, player_1: PlayerModel, player_2: PlayerModel
    ) -> tuple:
        return self.match_model.create_match(
            player_1_name=player_1.full_name,
            player_2_name=player_2.full_name,
            player_1_points=player_1.points, 
            player_2_points=player_2.points
        )

    def prepare_match_to_show(self, matches):
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
                player_2_color=player_2_color, current_match= i+1
            )
        self.match_view.waiting_user_continuation()

    @staticmethod
    def sort_by_elo(players: list[PlayerModel]) -> list[PlayerModel]:
        return sorted(
            players, key=lambda player:(-player.points)
        )

    @staticmethod
    def _color_choice():
        colors = COLORS[:]
        helpers.shuffle_element(colors)
        first_color = colors.pop()
        second_color = colors.pop()
        return first_color, second_color

    def add_to_match_played(self, player_1: PlayerModel, player_2: PlayerModel, all_matches_played: list):
        match = player_1.full_name, player_2.full_name
        all_matches_played.extend((match, match[::-1]))
    
    def generate_ranked_match(self, players, all_matches_played):
        player_1 = players[0]
        if player_2 := self.get_concurrent(player_1, players, all_matches_played):
            match = self.serialize_player_to_create_match(player_1, player_2)
            self.remove_from_players_to_pairing(players, player_1, player_2)
            return match

        return False
    
    def generate_already_played_match(self, players):
        player_1 = players[0]
        player_2 = players[1]
        self.remove_from_players_to_pairing(players, player_1, player_2)
        return self.serialize_player_to_create_match(player_1, player_2)
    
    def remove_from_players_to_pairing(self, players: list, player_1, player_2):
        players.remove(player_1)
        players.remove(player_2)
    
    def bye_player_if_odd(self, players: list[PlayerModel], players_bye: list):
        if len(players) % 2 != 0:
            helpers.shuffle_element(players)
            sorted_players = self.sort_by_elo(players)[::-1]
            for player in sorted_players:
                if player.full_name not in players_bye:
                    players_bye.append(player.full_name)
                    players.remove(player)
                    break