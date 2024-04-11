import string

# Imports modèle et vue du tournament.
from Controllers.roundcontroller import RoundController
from Models.tournamentmodel import TournamentModel
from Views.tournamentview import TournamentView

# Imports des autres contrôleurs nécessaires.
from Controllers.playercontroller import PlayerController

# Imports des utilitaires.
import helpers
import menus


class TournamentController:
    def __init__(
            self,
            tournament_view=TournamentView(),
            tournament_model=TournamentModel(),
            player=PlayerController(),
            round=RoundController(),
            all_matches_played: list=[],
            all_rounds: list=[]
    ):
        self.tournament_view = tournament_view
        self.tournament_model = tournament_model
        self.player = player
        self.round = round
        self.all_matches_played = all_matches_played
        self.all_rounds = all_rounds

    def start(self):
        unfinished_tournaments = self.check_unfinished_tounament()
        if not unfinished_tournaments:
            self.tournament_menu()
            return

        if result := self.select_tournament_to_resume(unfinished_tournaments):
            self.tournament_model = result
            self.resume_tournament()

        self.tournament_menu()

    def tournament_menu(self):
        launch = True
        while launch:
            self.get_participants()
            self.tournament_view.show_menu(
                helpers.create_menu,
                self.tournament_model.menu_name,
                self.tournament_model.menu_options,
                self.tournament_model.participants
            )
            user_choice = self.tournament_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    if not self.new_tournament():
                        continue
                    self.sync_round_with_tournament()
                    self.player.player_model.clear_participants()
                    self.start_rounds()
                case "2":
                    self.add_participant()
                case "3":
                    launch = False
                case _:
                    self.tournament_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def new_tournament(self):
        if not self._check_number_participants():
            return False
        
        self.tournament_model.name = self.tournament_view.get_tournament_name()
        self.tournament_model.location = self.tournament_view.get_tournament_location()
        if not self._check_name_location():
            return False
        
        self.tournament_model = self.tournament_model.create_new_tournament(
            name=self.tournament_model.name,
            location=self.tournament_model.location,
            players_list=self.tournament_model.participants
        )
        self.tournament_view.show_tournament_created(
            self.tournament_model.name,
            self.tournament_model.location
        )
        helpers.sleep_a_few_seconds()
        return True

    def get_participants(self):
        all_players = self.player.player_model.all_players
        participants = [player for player in all_players if player.participation == True]
        self.tournament_model.participants = participants

    def add_participant(self):
        first_name = self.player.player_view.get_first_name()
        players_found = [
            player
            for player in self.player.player_model.all_players
            if first_name in player.first_name
        ]
        self.player.player_view.show_players(players_found, numbering=True)
        if not players_found:
            self.tournament_view.show_no_player_matching(first_name)
            helpers.sleep_a_few_seconds()
            return
        
        user_choice = self.player.player_view.get_index_player_to_modify()
        index = self.player.check_user_choice(user_choice, players_found)
        if type(index) == int:
            player_to_modify = players_found[index]
            player_to_modify.participation = player_to_modify.participation != True
            player_to_modify.modify_player(modify_participation=True)

    def classification(self, rounds_result):
        all_players = self.round.match_controller.sort_by_elo(rounds_result)
        winner = all_players[0]
        winner.points = helpers.convert_if_integer(winner.points)
        self.tournament_view.show_winner(winner.full_name, winner.points)
        for player in all_players:
            player.points = helpers.convert_if_integer(player.points)
            self.tournament_view.show_classification(
                player_name=player.full_name, player_points=player.points
            )

    def check_unfinished_tounament(self):
        return [
            tournament
            for tournament in self.tournament_model.all_tournaments
            if not tournament.complete_status
        ]
                
    def resume_tournament(self):
        self.tournament_model.create_db_tournament()
        self.load_participants()
        self.sync_round_with_tournament()
        self.start_rounds(resume=True)


    def load_participants(self):
        result = all(isinstance(player, dict) for player in self.tournament_model.participants)
        if result:
            self.tournament_model.participants = [
                self.player.player_model.load_players_from_dict(player)
                for player in self.tournament_model.participants
            ]
        else:
            all_participants_dict = self.tournament_model.load_participants()
            for participant in all_participants_dict:
                for player in self.tournament_model.participants:
                    if player.full_name == f"{participant["first_name"]} {participant["last_name"]}":
                        player.points = participant["points"]

    def sync_round_with_tournament(self):
        """
        Synchronise les participants et la base de données du tournoi avec 
        les participants et la base de données du tour.
        """
        self.round.participants = self.tournament_model.participants
        self.round.round_db = self.tournament_model.tournament_db

    def start_rounds(self, resume: bool=False):
        result = self.round.round_menu(
            all_matches_played=self.all_matches_played,
            resume=resume, players_bye=self.tournament_model.players_bye
        )
        self.evaluate_show_classification(result)
        self.round.reset_participants_points()

    def evaluate_show_classification(self, result):
        if result:
            self.classification(self.tournament_model.participants)
            self.get_description()

            self.tournament_model.finish_tournament()
            self.all_matches_played.clear()
            self.tournament_model.players_bye.clear()
        else:
            self.tournament_model.update_tournament()

    def select_tournament_to_resume(self, unfinished_tournaments: list[TournamentModel]):
        for tournament in unfinished_tournaments:
            resume = self.tournament_view.prompt_resume_tournament(
                tournament.name, tournament.location
            )
            if resume in ["o", "O"]:
                return tournament

        return False
    
    def get_description(self):
        while True:
            if description := self.tournament_view.get_description():
                self.tournament_model.description = description
                return
            else:
                confirm_choice = self.tournament_view.get_confirm_choice()
                if confirm_choice in ["o", "O"]:
                    return
    
    def _check_name_location(self):
        name_to_check = self.tournament_model.name + self.tournament_model.location
        if any(charactere in string.punctuation for charactere in name_to_check):
            self.tournament_view.show_error_characteres_name()
            helpers.sleep_a_few_seconds()
            return False
        elif not (self.tournament_model.name and self.tournament_model.location):
            self.tournament_view.show_error_empty_name()
            helpers.sleep_a_few_seconds()
            return False
        
        return True

    def _check_number_participants(self):
        number_of_participants = len(self.tournament_model.participants)
        if number_of_participants < helpers.MINIMUM_PLAYER_FOR_TOURNAMENT:
            self.tournament_view.show_not_enough_participants(
                number_of_participants
            )
            helpers.sleep_a_few_seconds()
            return False
        
        return True
