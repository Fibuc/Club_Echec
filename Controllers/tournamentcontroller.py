# Imports modèle et vue du tournament.
from roundcontroller import RoundController
from roundmodel import RoundModel
from tournamentmodel import TournamentModel, NOT_ENDED_TOURNAMENT_PREFIX
from Views.tournamentview import TournamentView

# Imports des autres contrôleurs nécessaires.
from Controllers.playercontroller import PlayerController

# Imports des utilitaires.
import helpers
import menus


START_TOURNAMENT_MENU = {
    menus.NAME_MENU : "DEBUT TOURNOIS",
    menus.OPTIONS_MENU : [
        "Lancer le tour et générer des matchs",
        "Enregistrer et quitter",
        ]
}


class TournamentController:
    def __init__(self):
        self.tournament_view = TournamentView()
        self.tournament_model = TournamentModel()
        self.player = PlayerController()
        self.round = RoundController()

    def tournament_menu(self):
        launch = True
        while launch:
            self.tournament_view.show_menu(
                helpers.create_menu,
                self.tournament_model.menu_name,
                self.tournament_model.menu_options,
                self.player.player_model.participants
            )

            user_choice = self.tournament_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    self.new_tournament()
                    RoundModel.participants = (
                        self.player.player_model.participants
                    )
                    RoundModel.round_db = self.tournament_model.tournament_path
                    self.round.round_menu()
                case "2":
                    self.player.add_participant()
                case "3":
                    launch = False
                case _:
                    self.tournament_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def new_tournament(self):
        self.tournament_model.name = self.tournament_view.get_tournament_name()
        self.tournament_model.location = self.tournament_view.get_tournament_location()
        self.tournament_model.create_new_tournament(
            name=self.tournament_model.name,
            location=self.tournament_model.location,
            players_list=self.player.player_model.participants
        )
        self.tournament_view.show_tournament_created(
            self.tournament_model.name,
            self.tournament_model.location
        )
        helpers.sleep_a_few_seconds()

    def get_unfinished_tournament(self):
        TournamentModel.unfinished_tournament = []
        if TournamentModel.all_tournaments:
            for tournament in TournamentModel.all_tournaments:
                if tournament.name.startwith(NOT_ENDED_TOURNAMENT_PREFIX):
                    PlayerModel.participants.append(tournament)

    def resume_tournament(self):
        pass

    def start_tournament(self):
        """Démarre le tournois."""
        self.date_time_start = helpers.get_date()

    def end_tournament(self, description):
        """Termine le tournois."""
        self.description = description
        self.date_time_end = helpers.get_date()


