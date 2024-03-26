import copy
from pprint import pprint

from roundmodel import RoundModel
from roundview import RoundView

import helpers

PLAYER_PER_MATCH = 2
COLORS = ["Blanc", "Noir"]

class RoundController:
    def __init__(
            self,
            round_model=RoundModel(),
            round_view=RoundView()
        ):
        self.round_model = round_model
        self.round_view = round_view

    def round_menu(self):
        self.round_model.create_new_round()
        launch = True
        round_start = False
        while launch:
            options = []
            # self.round_model.sorted_by_elo()
            if round_start:
                options.append(self.round_model.menu_options[1])
            else:
                options.append(self.round_model.menu_options[0])
            self.round_view.show_menu(
                helpers.create_menu,
                self.round_model.menu_name,
                options,
                RoundModel.current_round
            )
            user_choice = self.round_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    if round_start:
                        self.end_match()
                        round_start = False
                        self.round_model.matchs.clear()
                        self.round_model.create_new_round()
                    else:
                        result = self.start_matchs()
                        if not result:
                            return self.round_view.show_all_match_played()
                        round_start = True
                case "2":
                    launch = False
                case _:
                    self.round_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def start_matchs(self): # Tuple (["Nom_joueur_1", "score"], ["Nom_joueur_2", "score"],)
        # Liste des matchs = [([Joueur_1], [Joueur_2])]
        """Créée une nouvelle liste de matchs et les enregistre.

        Returns:
            fonction: Sauvegarde la nouvelle liste de match.
        """
        all_players = copy.deepcopy(RoundModel.participants)
        if self.round_model.current_round != 1:
            all_players = self.sort_players(all_players)
        number_of_match = len(all_players) // PLAYER_PER_MATCH
        current_match = 1
        for _ in range(number_of_match):
            if self.round_model.current_round == 1:
                self.first_matchs(all_players)
                
            else:
                result = self.other_matchs(all_players)
                if not result:
                    return False

        self.round_model.save_round()
        current_match = 1
        for match in self.round_model.matchs:
            self.round_view.show_match(match, current_match)
            current_match += 1
        
        return True

    def first_matchs(self, players):
            player_1 = helpers.shuffle_element(players)
            player_2 = helpers.shuffle_element(players)
            match = self.create_match(player_1, player_2)
            self.round_model.all_matchs_played.append(match)
            self.round_model.matchs.append(match)

    
    def other_matchs(self, players: list):
        player_1 = players.pop(0)
        number_of_concurrent = len(players)
        index_concurrent = 0
        while index_concurrent != number_of_concurrent:
            player_2 = players.pop(index_concurrent)
            match = self.create_match(player_1, player_2)
            result = self.check_match_played(match)
            if result:
                players.insert(index_concurrent, player_2)
                index_concurrent += 1
                continue
            else:
                self.round_model.all_matchs_played.append(match)
                self.round_model.matchs.append(match)
                return True
            
        return False


        

    def end_match(self):
        all_players = RoundModel.participants
        for match in self.round_model.matchs:
            player_1_name = match[0][0]
            player_2_name = match[1][0]
            result = self.get_winner(player_1_name, player_2_name)
            match result:
                case 1:
                    for player in all_players:
                        full_name_search = f"{player.first_name} {player.last_name}"
                        if full_name_search == player_1_name:
                            player.number_of_points += 1
                case 2:
                    for player in all_players:
                        full_name_search = f"{player.first_name} {player.last_name}"
                        if full_name_search == player_2_name:
                            player.number_of_points += 1
                case 3:
                    for player in all_players:
                        full_name_search = f"{player.first_name} {player.last_name}"
                        if full_name_search in [player_1_name, player_2_name]:
                            player.number_of_points += 0.5

    def get_winner(self, player_1, player_2):
        lauch = True
        player_1_choice = 1
        player_2_choice = 2
        draw_choice = 3
        accept_choices = [player_1_choice, player_2_choice, draw_choice]
        while lauch:
            user_choice = self.round_view.get_result_of_match(
                    player_1,
                    player_2
            )
            try:
                user_choice = int(user_choice)
                if user_choice in accept_choices:
                    return user_choice
                else:
                    self.round_view.show_error_message(user_choice)
                    helpers.sleep_a_few_seconds()
                    continue

            except ValueError:
                self.round_view.show_error_message(user_choice)
                helpers.sleep_a_few_seconds()
                continue

    def create_match(self, player_1, player_2):
        player_1_name = self.get_full_name(player_1)
        player_2_name = self.get_full_name(player_2)
        match = sorted(
                (
                    [player_1_name, player_1.number_of_points],
                    [player_2_name, player_2.number_of_points]
                )
            )
        return tuple(match)

    def check_match_played(self, match):
        player_name_current_match = [player[0] for player in match]
        player_name_all_match = []
        for match in self.round_model.all_matchs_played:
            player_match = [player[0] for player in match]
            player_name_all_match.append(player_match)

        if player_name_current_match in player_name_all_match:
            return True
        
        return False


    @staticmethod
    def color_choice():
        colors = copy.deepcopy(COLORS)
        first_color = helpers.shuffle_element(colors)
        second_color = colors.pop()
        return first_color, second_color
    
    @staticmethod
    def sort_players(players):
        return sorted(players, key=lambda player:(
                -player.number_of_points,
                player.first_name,
                player.last_name
            )
        )
    
    @staticmethod
    def add_to_all_matchs_played(matchs):
        for match in matchs:
            RoundModel.all_matchs_played.append(match)


    @staticmethod
    def get_full_name(player):
        return f"{player.first_name} {player.last_name}"

