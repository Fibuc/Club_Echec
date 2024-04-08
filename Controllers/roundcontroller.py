from pprint import pprint

from Models.roundmodel import RoundModel
from Views.roundview import RoundView
from Controllers.matchcontroller import MatchController

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
            round_db = None
        ):
        self.round_model = round_model
        self.round_view = round_view
        self.match_controller = match_controller
        self.all_matches = all_matches
        self.participants = participants
        self.current_round=current_round
        self.round_db = round_db

    def round_menu(self, all_matches_played: list, players_bye: list, resume: bool=False, round_start: bool=False):
        all_rounds_launch = False
        if not resume:
            self.start_new_round()  
        else:
            self.resume_round(all_matches_played)

        while self.current_round <= helpers.DEFAULT_NUMBER_ROUNDS:
            option = self.option_choice(round_start)
            self.round_view.show_menu(
                helpers.create_menu,
                self.round_model.menu_name,
                option,
                self.current_round,
                can_undo=not round_start
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
                        self.add_new_matchs(all_matches_played, players_bye)
                        round_start = True

                case "2":
                    if round_start:
                        self.round_view.show_error_message_choice(user_choice)
                        helpers.sleep_a_few_seconds()
                        continue

                    return all_rounds_launch
                
                case _:
                    self.round_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

        return True

    def add_new_matchs(self, all_matches_played, players_bye):
        """Créée une nouvelle liste de matchs et les enregistre.

        Returns:
            fonction: Sauvegarde la nouvelle liste de match.
        """
        all_players = self.participants[:]
        matches = self.match_controller.get_matches(
            self.current_round, all_players, all_matches_played, players_bye
        )
        self.round_model.matches = matches
        self.round_model.save_round(self.round_db)

    def end_match(self):
        for match in self.round_model.matches:
            for player in self.participants:
                if player.full_name == match[0][0]:
                    player_1 = player
                elif player.full_name == match[1][0]:
                    player_2 = player
            self.match_controller.get_winner(player_1, player_2)
        self.round_model.date_time_end = str(helpers.get_date_time())
        self.round_model.update_round(self.round_db)

    def start_new_round(self):
        self.current_round += 1
        self.round_model = self.round_model.create_new_round(
            round_number=self.current_round,
            matches=self.all_matches
        )

    def reset_participants_points(self):
        self.current_round = 0
        for participant in self.participants:
            participant.points = 0

    def option_choice(self, round_start):
        if round_start:
            return [self.round_model.menu_options[1]]
        
        return [self.round_model.menu_options[0]]
    
    def get_informations_rounds(self, all_matches_played: list[tuple]):
        all_rounds = self.round_model.load_rounds(self.round_db)
        self.add_to_match_played(all_matches_played, all_rounds)
        if all_rounds:
            self.round_model = all_rounds[-1]
            self.current_round = self.round_model.round_number
        else:
            self.current_round = 0

    def add_to_match_played(self, all_matches_played: list[tuple], all_rounds: list[RoundModel]):
        for round in all_rounds:
            for match in round.matches:
                already_played_match = match[0][0], match[1][0]
                all_matches_played.extend((already_played_match, already_played_match[::-1]))

    def resume_round(self, all_matches_played: list[tuple]):
        self.get_informations_rounds(all_matches_played)
        self.start_new_round()