import copy
from random import shuffle

from roundmodel import RoundModel
from roundview import RoundView

import helpers

PLAYER_PER_MATCH = 2

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
                        self.start_matchs()
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
        all_players = copy.deepcopy(RoundModel.all_player_list)
        number_of_match = len(all_players) // PLAYER_PER_MATCH

        for _ in range(number_of_match):
            player_1 = self.shuffle_players(all_players)
            player_1_name = f"{player_1.first_name} {player_1.last_name}"
            player_2 = self.shuffle_players(all_players)
            player_2_name = f"{player_2.first_name} {player_2.last_name}"
            match_pair = sorted(
                (
                    [player_1_name, player_1.number_of_points],
                    [player_2_name, player_2.number_of_points]
                )
            )
            self.round_model.all_match_played.append(match_pair)
            self.round_model.matchs.append(match_pair)
        self.round_model.save_round()

        current_match = 1
        for match in self.round_model.matchs:
            self.round_view.show_match(match, current_match)
            current_match += 1

    
    def end_match(self):
        all_players = RoundModel.all_player_list
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

    @staticmethod
    def shuffle_players(players):
        shuffle(players)
        return players.pop()
