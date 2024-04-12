# Imports modèle et vue des rapports.
from tinydb import TinyDB

from Controllers.clubcontroller import ClubController
from Controllers.roundcontroller import RoundController
from Models.reportmodel import ReportModel
from Views.reportview import ReportView

# Imports des autres contrôleurs nécessaires.
from Controllers.playercontroller import PlayerController
from Controllers.tournamentcontroller import TournamentController

# Import des utilitaires.
import menus
import helpers

class ReportController:
    def __init__(self):
        self.report_view = ReportView()
        self.report_model = ReportModel()
        self.club = ClubController()
        self.player = PlayerController()
        self.tournament = TournamentController()
        self.round = RoundController()

    def report_menu(self):
        launch = True
        while launch:
            self.report_view.show_menu(
                helpers.create_menu, self.report_model.menu_name,
                self.report_model.menu_options
            )
            user_choice = self.report_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    self.show_all_players()
                case "2":
                    self.show_all_clubs()
                case "3":
                    self.refresh_tournaments()
                    self.show_all_tournaments()
                    if self.get_tournament():
                        self.tournament_report_menu()
                case "4":
                    launch = False
                case _:
                    self.report_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()
    
    def show_all_players(self):
        self.player.player_model.all_players = sorted(
            self.player.player_model.all_players, key=lambda player:player.first_name
        )
        self.player.player_view.show_players(
            self.player.player_model.all_players
                    )
        self.report_view.waiting_user_continuation()

    def show_all_clubs(self):
        for i, club in enumerate(self.club.club_model.all_clubs, start=1):
            self.club.club_view.show_club(
                club_name=club.name,
                national_chest_id=club.national_chest_id,
                current_club=i
            )
        self.club.club_view.show_border()
        self.report_view.waiting_user_continuation()
    
    def show_all_tournaments(self):
        self.tournament.tournament_view.show_number_of_tournaments_found(
            len(self.tournament.tournament_model.all_tournaments)
            )
        for i, tournament in enumerate(
            self.tournament.tournament_model.all_tournaments, start=1
        ):
            self.tournament.tournament_view.show_tournament(
                tournament=tournament, current_tournament=i
            )
    
    def get_tournament(self):
        user_choice = self.report_view.get_tournament_to_show()
        if self._check_user_choice(user_choice):
            self.tournament.tournament_model = (
                self.tournament.tournament_model.all_tournaments[
                    int(user_choice) - 1
                ]
            )
            return True
        elif user_choice == "":
            return False
        else:
            self.report_view.show_error_message_choice(user_choice)
            helpers.sleep_a_few_seconds()
            return False


    def tournament_report_menu(self):
        self.get_all_rounds()
        tournament_start, tournament_end = self.get_tournament_dates()
        all_informations = [
            self.tournament.tournament_model.name,
            self.tournament.tournament_model.location,
            tournament_start, tournament_end
            
        ]
        launch = True
        while launch:
            self.report_view.menu_tournament_report(
                helpers.create_menu,
                self.report_model.menu_tournament_report_name,
                self.report_model.menu_tournament_report_option,
                all_informations
            )
            user_choice = self.report_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    self.show_participants()
                    self.report_view.waiting_user_continuation()
                case "2":
                    self.show_rounds()
                    self.report_view.waiting_user_continuation()
                case "3":
                    launch = False
                case _:
                    self.report_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def _check_user_choice(self, user_choice):
        options = [
            str(i) for i in range(
                1, len(self.tournament.tournament_model.all_tournaments) + 1
            )
        ]
        return user_choice in options

    def show_participants(self):
        if not any(
            isinstance(player, dict)
            for player in self.tournament.tournament_model.participants):
            self.player.player_view.show_players(
                self.tournament.tournament_model.participants
            )

        players = [
            self.player.player_model.load_players_from_dict(player)
            for player in self.tournament.tournament_model.participants
        ]
        self.player.player_view.show_players(players)

    def get_all_rounds(self):
        self.tournament.all_rounds = self.round.round_model.load_rounds(
            TinyDB(self.tournament.tournament_model.tournament_path)
        )

    def get_tournament_dates(self):
        tournament_start = self.tournament.all_rounds[0].date_time_start
        tournament_end = self.tournament.all_rounds[-1].date_time_end
        return tournament_start, tournament_end
    
    def show_rounds(self):
        for round in self.tournament.all_rounds:
            self.round.round_view.show_rounds(
                current_round=round.round_number,
                start_date=round.date_time_start,
                end_date=round.date_time_end,
                matches=round.matches
            )

    def refresh_tournaments(self):
        self.tournament.tournament_model.all_tournaments.clear()
        self.tournament.tournament_model.load_all_tournaments()