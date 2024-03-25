# Imports modèle et vue du main.
from Views.mainview import MainView
from Models.mainmodel import MainModel

# Imports des autres contrôleurs nécessaires.
from Controllers.tournamentcontroller import TournamentController
from Controllers.playercontroller import PlayerController
from Controllers.clubcontroller import ClubController
from Controllers.reportcontroller import ReportController

# Import des utilitaires.
import helpers


class MainController:
    """Classe contrôleur principal"""
    def __init__(self):
        self.main_view = MainView()
        self.main_model = MainModel()
        self.tournament = TournamentController()
        self.player = PlayerController()
        self.club = ClubController()
        self.report = ReportController()

    def run(self):
        """Lance l'éxecution de l'application"""
        self.player.player_model.load_all_players()
        self.player.get_participants()
        # self.tournament.tournament_model.load_all_tournaments()
        self.main_view.show_welcome_message()
        self.main_menu()
        self.main_view.say_goodbye()

    def main_menu(self):
        launch = True
        first_display = True
        while launch:
            self.main_view.show_menu(
                helpers.create_menu,
                self.main_model.menu_name,
                self.main_model.menu_options,
                first_display
            )
            user_choice = self.main_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    self.tournament.tournament_menu()
                case "2":
                    self.player.player_menu()
                case "3":
                    self.club.club_menu()
                case "4":
                    self.report.report_menu()
                case "5":
                    launch = False
                case _:
                    self.main_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()
            first_display = False