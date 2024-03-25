# Imports modèle et vue des rapports.
from Models.reportmodel import ReportModel
from Views.reportview import ReportView

# Imports des autres contrôleurs nécessaires.
from Controllers.playercontroller import PlayerController
from Controllers.tournamentcontroller import TournamentController

# Import des utilitaires.
import helpers

class ReportController:
    def __init__(self):
        self.report_view = ReportView()
        self.report_model = ReportModel()
        self.player = PlayerController()
        self.tournament = TournamentController()

    def report_menu(self):
        launch = True
        while launch:
            self.report_view.show_menu(
                helpers.create_menu,
                self.report_model.menu_name,
                self.report_model.menu_options,
            )
            user_choice = self.report_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    self.player.player_view.show_players(
                        self.player.player_model.all_players
                    )
                case "2":
                    self.tournament.tournament_view.show_all_tournaments(
                        self.tournament.tournament_model.all_tournaments
                    )
                case "3":
                    print("Choix 3")
                case "4":
                    print("Choix 4")
                case "5":
                    print("Choix 5")
                case "6":
                    launch = False
                case _:
                    self.report_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()