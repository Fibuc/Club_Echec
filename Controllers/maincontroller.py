from pathlib import Path

# Import des utilitaires.
import helpers
import config

# Imports modèle et vue du main.
from Views.mainview import MainView
from Models.mainmodel import MainModel

# Imports des autres contrôleurs nécessaires.
from Controllers.tournamentcontroller import TournamentController
from Controllers.playercontroller import PlayerController
from Controllers.clubcontroller import ClubController
from Controllers.reportcontroller import ReportController

# Création du dossier data si n'existe pas
Path(config.DATA_DIR).mkdir(exist_ok=True, parents=True)


class MainController:
    """Classe contrôleur principal"""
    def __init__(
        self, main_view=MainView(), main_model=MainModel(),
        tournament=TournamentController(), player=PlayerController(),
        club=ClubController(), report=ReportController()
    ):
        """Initialise le contrôleur avec le modèle et la vue ainsi que les
        autres contrôleurs nécessaires.

        Args:
            main_view (MainView, optional): Vue principale. Défaut MainView().
            main_model (MainModel, optional): Modèle principal.
            Défaut MainModel().
            tournament (TournamentController, optional): Contrôleur des
            tournois. Défaut TournamentController().
            player (PlayerController, optional): Contrôleur des joueurs.
            Défaut PlayerController().
            club (ClubController, optional): Contrôleur des clubs.
            Défaut ClubController().
            report (ReportController, optional): Contrôleur des rapports.
            Défaut ReportController().
        """
        self.main_view = main_view
        self.main_model = main_model
        self.tournament = tournament
        self.player = player
        self.club = club
        self.report = report

    def run(self):
        """Lance l'éxecution de l'application"""
        self.load_datas()
        self.main_view.show_welcome_message()
        self.main_menu()
        self.main_view.say_goodbye()

    def main_menu(self):
        """
        Contrôle la fonctionnalité du menu principal, permettant aux
        utilisateurs de naviguer à travers les différentes options du menu.
        """
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
                    self.tournament.check_unfinished_tournaments()
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

    def load_datas(self):
        """
        Charges toutes les données des joueurs, des tournois et des clubs.
        """
        self.player.charge_all_players()
        self.tournament.tournament_model.load_all_tournaments()
        self.club.club_model.load_clubs()
