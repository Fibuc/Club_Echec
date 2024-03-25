# Imports modèle et vue du tournament.
from Models.tournamentmodel import TournamentModel, MatchModel, RoundModel, NOT_ENDED_TOURNAMENT_PREFIX
from Views.tournamentview import TournamentView, MatchView, RoundView

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


class MatchController:
    def __init__(self):
        self.match_model = MatchModel()
        self.match_view = MatchView()

    def start_first_matchs(self): # Tuple (["Nom_joueur_1", "score"], ["Nom_joueur_2", "score"],)
        # Liste des matchs = [([Joueur_1], [Joueur_2])]
        """Créée une nouvelle liste de matchs et les enregistre.

        Returns:
            fonction: Sauvegarde la nouvelle liste de match.
        """
        self.match_model.create_first_matchs()
        current_match = 1
        for match in self.match_model.all_match_played:
            self.match_view.show_match(match, current_match)
            current_match += 1
        return self.match_model.all_match_played

    def finish_match(self):
        current_match = 1
        for match in self.match_model.all_match_played:
            player_1 = match[0][0]
            player_2 = match[1][0]
            self.get_winner(player_1, player_2)
            current_match += 1

    def get_winner(self, player_1, player_2):
        lauch = True
        player_1_choice = 1
        player_2_choice = 2
        draw_choice = 3
        accept_choices = [player_1_choice, player_2_choice, draw_choice]
        while lauch:
            user_choice = self.match_view.get_result_of_match(
                    player_1,
                    player_2
            )
            try:
                user_choice = int(user_choice)
                if user_choice in accept_choices:
                    return user_choice
                else:
                    self.match_view.show_error_message(user_choice)
                    helpers.sleep_a_few_seconds()
                    continue

            except ValueError:
                self.match_view.show_error_message(user_choice)
                helpers.sleep_a_few_seconds()
                continue


class RoundController:
    def __init__(
            self,
            round_model=RoundModel(),
            round_view=RoundView(),
            match_controller=MatchController(),
            rounds=[]
        ):
        self.round_model = round_model
        self.round_view = round_view
        self.match = match_controller
        self.rounds = rounds

    def round_menu(self):
        launch = True
        while launch:
            self.round_view.show_menu(
                helpers.create_menu,
                self.round_model.menu_name,
                self.round_model.menu_options,
                RoundModel.current_round
            )

            user_choice = self.round_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    RoundModel.all_rounds.append(RoundModel())
                case "2":
                    launch = False
                case _:
                    self.round_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def add_matchs_to_round(self):
        self.round = self.round_model.create_new_round()
        self.round_model.add_new_matchs(
            self.match.start_first_matchs()
        )


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
                PlayerModel.participants
            )

            user_choice = self.tournament_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    self.new_tournament()
                    # self.player.set_all_player_participation_false()
                    self.round.round_menu()
                case "2":
                    self.player.add_player_at_tournament()
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
            players_list=participants_list
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


