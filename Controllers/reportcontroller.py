from tinydb import TinyDB

from Models.reportmodel import ReportModel
from Views.reportview import ReportView

from Controllers.playercontroller import PlayerController
from Controllers.tournamentcontroller import TournamentController
from Controllers.clubcontroller import ClubController
from Controllers.roundcontroller import RoundController

import helpers


class ReportController:
    """Classe contrôleur des rapports."""
    def __init__(
        self, report_view=ReportView(), report_model=ReportModel(),
        club=ClubController(), player=PlayerController(),
        tournament=TournamentController(), round=RoundController()
    ):
        """
        Initialise le contrôleur avec la vue, le modèle et autres contrôleurs
        nécessaires.

        Args:
            report_view (ReportView, optional): Vue des rapports.
            Défaut ReportView().
            report_model (ReportModel, optional): Modèle des rapports.
            Défaut ReportModel().
            club (ClubController, optional): Contrôleur des club.
            Défaut ClubController().
            player (PlayerController, optional): Contrôleur des joueurs.
            Défaut PlayerController().
            tournament (TournamentController, optional): Contrôleur des
            tournois. Défaut TournamentController().
            round (RoundController, optional): Contrôleur des rounds.
            Défaut RoundController().
        """
        self.report_view = report_view
        self.report_model = report_model
        self.club = club
        self.player = player
        self.tournament = tournament
        self.round = round

    def report_menu(self):
        """
        Contrôle la fonctionnalité du menu des rapports, permettant à
        l'utilisateur de naviguer à travers les différentes options des
        rapports.
        """
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
        """
        Prépare et affiche tous les joueurs dans l'ordre alphabétique.
        """
        self.player.player_model.all_players = sorted(
            self.player.player_model.all_players, key=lambda player: player.first_name
        )
        self.player.player_view.show_players(
            self.player.player_model.all_players
                    )
        self.report_view.waiting_user_continuation()

    def show_all_clubs(self):
        """
        Prépare et affiche tous les clubs.
        """
        for i, club in enumerate(self.club.club_model.all_clubs, start=1):
            self.club.club_view.show_club(
                club_name=club.name,
                national_chest_id=club.national_chest_id,
                current_club=i
            )
        self.club.club_view.show_border()
        self.report_view.waiting_user_continuation()

    def show_all_tournaments(self):
        """
        Prépare et affiche tous les tournois.
        """
        self.tournament.tournament_view.show_number_of_tournaments_found(
            len(self.tournament.tournament_model.all_tournaments)
            )
        tournament_number = 1
        for tournament in self.tournament.tournament_model.all_tournaments:
            if tournament.complete_status:
                self.tournament.tournament_view.show_tournament(
                    tournament=tournament,
                    current_tournament=tournament_number
                )
                tournament_number += 1

    def get_tournament(self) -> bool:
        """
        Selectionne l'instance de TournamentModel choisie par l'utilisateur.
        Retourne True si l'utilisateur a bien choisi, False autres cas.

        Returns:
            bool: Tournoi retourné (True=oui, False=non).
        """
        user_choice = self.report_view.get_tournament_to_show()
        all_finished_tournaments = [
            tournament
            for tournament in self.tournament.tournament_model.all_tournaments
            if tournament.complete_status
        ]
        if self._check_tournament_user_choice(
            user_choice, all_finished_tournaments
        ):
            self.tournament.tournament_model = (
                all_finished_tournaments[
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
        """
        Contrôle la fonctionnalité du menu des rapports des tournois,
        permettant à l'utilisateur de naviguer à travers les différentes
        options des rapports tournois.
        """
        self.get_all_rounds()
        self._transform_if_dict_player()
        tournament_start, tournament_end = self.get_tournament_dates()
        all_informations = [
            self.tournament.tournament_model.name,
            self.tournament.tournament_model.location,
            tournament_start, tournament_end,
            self.tournament.tournament_model.winner_name
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
                case "2":
                    self.show_rounds()
                case "3":
                    self.show_classification()
                case "4":
                    launch = False
                case _:
                    self.report_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def _check_tournament_user_choice(
        self, user_choice: str, all_finished_tournaments: list
    ) -> bool:
        """
        Vérifie si le choix de l'utilisateur se trouve dans la liste des choix
        disponibles.

        Args:
            user_choice (str): Choix de l'utilisateur.
            all_finished_tournaments (list): Liste à vérifier.

        Returns:
            bool: Retourne True si dans la liste, sinon False.
        """
        options = [
            str(i) for i in range(
                1, len(all_finished_tournaments) + 1
            )
        ]
        return user_choice in options

    def show_participants(self):
        """Affiche les participants du tournoi."""
        self.player.player_view.show_players(
            self.tournament.tournament_model.participants
        )
        self.report_view.waiting_user_continuation()

    def get_all_rounds(self):
        """
        Récupère tous les rounds du tournois et les ajoute à la
        variable "all_rounds" de l'instance TournamentController.
        """
        self.tournament.all_rounds = self.round.round_model.load_rounds(
            TinyDB(self.tournament.tournament_model.tournament_path)
        )

    def get_tournament_dates(self) -> tuple[str, str]:
        """
        Récupère la date de début du premier round et la date de fin du
        dernier round.

        Returns:
            tuple[str, str]: Tuple du début et de la fin du tournois.
        """
        tournament_start = self.tournament.all_rounds[0].date_time_start
        tournament_end = self.tournament.all_rounds[-1].date_time_end
        return tournament_start, tournament_end

    def show_rounds(self):
        """Prépare et affiche tous les rounds du tournoi."""
        for round in self.tournament.all_rounds:
            if all_players_bye := (
                self.tournament.tournament_model.players_bye
            ):
                player_bye = all_players_bye[round.round_number - 1]
            else:
                player_bye = ""
            self.round.round_view.show_round(
                current_round=round.round_number,
                start_date=round.date_time_start,
                end_date=round.date_time_end,
                matches=round.matches,
                player_bye=player_bye
            )
        self.report_view.waiting_user_continuation(border=True)

    def refresh_tournaments(self):
        """Actualise tous les tournois."""
        self.tournament.tournament_model.all_tournaments.clear()
        self.tournament.tournament_model.load_all_tournaments()

    def show_classification(self):
        """Affiche le vainqueur et le classement des joueurs du tournoi."""
        players_sorted = sorted(
            self.tournament.tournament_model.participants,
            key=lambda player: -player.points
        )
        winner = [
            player
            for player in players_sorted
            if player.full_name == (
                self.tournament.tournament_model.winner_name
            )
        ][0]
        self.tournament.tournament_view.show_winner(
            winner.full_name,
            winner.points)
        for player in players_sorted:
            player.points = helpers.convert_if_integer(player.points)
            self.tournament.tournament_view.show_classification(
                player_name=player.full_name, player_points=player.points
            )
        self.report_view.waiting_user_continuation(border=True)

    def _transform_if_dict_player(self):
        """
        Vérifie la liste des participants. Si tous les joueurs sont des
        dictionnaires, alors transforme en instance de PlayerModel.
        """
        if any(
            isinstance(player, dict)
            for player in self.tournament.tournament_model.participants
        ):
            self.tournament.tournament_model.participants = [
                self.player.player_model.load_players_from_dict(player)
                for player in self.tournament.tournament_model.participants
            ]
