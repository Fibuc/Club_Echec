import copy
from pprint import pprint

from roundmodel import RoundModel
from roundview import RoundView
from matchcontroller import MatchController

import helpers

class RoundController:
    def __init__(
            self,
            round_model=RoundModel(),
            round_view=RoundView(),
            match_controller=MatchController(),
            all_matches: list=[],
            participants: list=[],
            current_round: int=0,
            all_matches_possible: list=[]
        ):
        self.round_model = round_model
        self.round_view = round_view
        self.match_controller = match_controller
        self.all_matches = all_matches
        self.participants = participants
        self.current_round=current_round
        self.all_matches_possible=all_matches_possible

    def round_menu(self):
        self.generate_all_possible_matches(self.participants)
        self.start_new_round()
        launch = True
        round_start = False
        while launch:
            options = []
            if round_start:
                options.append(self.round_model.menu_options[1])
            else:
                options.append(self.round_model.menu_options[0])
            self.round_view.show_menu(
                helpers.create_menu,
                self.round_model.menu_name,
                options,
                self.current_round
            )
            user_choice = self.round_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    if round_start:
                        self.end_match()
                        round_start = False
                        self.all_matches.clear()
                        self.start_new_round()
                    else:
                        self.add_new_matchs()
                        round_start = True

                case "2":
                    launch = False
                case _:
                    self.round_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def add_new_matchs(self):
        """Créée une nouvelle liste de matchs et les enregistre.

        Returns:
            fonction: Sauvegarde la nouvelle liste de match.
        """
        all_players = copy.deepcopy(self.participants)
        matches = self.match_controller.get_matches(self.current_round, all_players, self.all_matches_possible)
        self.round_model.matches = matches
        self.round_model.save_round()


    def end_match(self):
        for match in self.round_model.matches:
            for player in self.participants:
                if player.get_full_name() == match[0][0]:
                    player_1 = player
                elif player.get_full_name() == match[1][0]:
                    player_2 = player
            self.match_controller.get_winner(player_1, player_2)
        self.round_model.update_round()

    def start_new_round(self):
        self.current_round += 1
        self.round_model.create_new_round(
            round_number=self.current_round,
            matches=self.all_matches
        )

    def generate_all_possible_matches(self, players: list):
        for i_1, player_1 in enumerate(players):
            for i_2, player_2 in enumerate(players):
                if i_1 != i_2:
                    match = tuple(
                        [player_1.get_full_name(),
                         player_2.get_full_name()]
                    )
                    self.all_matches_possible.append(match)