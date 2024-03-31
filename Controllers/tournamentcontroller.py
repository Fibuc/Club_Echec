# Imports modèle et vue du tournament.
from Controllers.roundcontroller import RoundController
from Models.roundmodel import RoundModel
from Models.tournamentmodel import TournamentModel, NOT_ENDED_TOURNAMENT_PREFIX
from Views.tournamentview import TournamentView

# Imports des autres contrôleurs nécessaires.
from Controllers.playercontroller import PlayerController

# Imports des utilitaires.
import helpers
import menus


class TournamentController:
    def __init__(self):
        self.tournament_view = TournamentView()
        self.tournament_model = TournamentModel()
        self.player = PlayerController()
        self.round = RoundController()

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
                    self.new_tournament()
                    self.round.participants = (
                        self.tournament_model.participants
                    )
                    RoundModel.round_db = self.tournament_model.tournament_path
                    self.round.round_menu()
                case "2":
                    self.add_participant()
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
            players_list=self.tournament_model.participants
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
                    self.round.participants.append(tournament)

    def resume_tournament(self):
        pass

    def get_participants(self):
        all_players = self.player.player_model.all_players
        participants = [player for player in all_players if player.participation == True]
        self.tournament_model.participants = participants

    def add_participant(self):
        players_found = []
        first_name = self.player.player_view.get_first_name()
        for player in self.player.player_model.all_players:
            if first_name in player.first_name:
                players_found.append(player)
        self.player.player_view.show_players(players_found, numbering=True)
        user_choice = self.player.player_view.get_index_player_to_modify()
        index = self.player.check_user_choice(user_choice, players_found)
        if type(index) == int:
            player_to_modify = players_found[index]
            if player_to_modify.participation == True:
                player_to_modify.participation = False
            else:
                player_to_modify.participation = True

            player_to_modify.modify_player(participation=True)

    def start_tournament(self):
        """Démarre le tournois."""
        self.date_time_start = helpers.get_date()

    def end_tournament(self, description):
        """Termine le tournois."""
        self.description = description
        self.date_time_end = helpers.get_date()


