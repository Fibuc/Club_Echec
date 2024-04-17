import string

# Imports modèle et vue du tournament.
from Models.tournamentmodel import TournamentModel
from Views.tournamentview import TournamentView

# Imports des autres contrôleurs nécessaires.
from Controllers.playercontroller import PlayerController
from Controllers.roundcontroller import RoundController
from Models.roundmodel import RoundModel

# Imports des utilitaires.
import config
import helpers


class TournamentController:
    def __init__(
        self, tournament_view=TournamentView(),
        tournament_model=TournamentModel(), player=PlayerController(),
        round=RoundController(), all_matches_played: list[tuple] = [],
        all_rounds: list[RoundModel] = []
    ):
        """Initialise le contrôleur avec la vue le modèle et autres
        contrôleurs nécéssaires.

        Args:
            tournament_view (TournamentView, optional): Vue du tournoi.
            Défaut TournamentView().
            tournament_model (TournamentModel, optional): Modèle du tournoi.
            Défaut TournamentModel().
            player (PlayerController, optional): Contrôleur du joueur.
            Défaut PlayerController().
            round (RoundController, optional): Contrôleur du round.
            Défaut RoundController().
            all_matches_played (list, optional): Liste de tous les matchs
            joués. Défaut [].
            all_rounds (list[RoundModel], optional): Liste de tous les rounds.
            Défaut [].
        """
        self.tournament_view = tournament_view
        self.tournament_model = tournament_model
        self.player = player
        self.round = round
        self.all_matches_played = all_matches_played
        self.all_rounds = all_rounds

    def check_unfinished_tournaments(self):
        """
        Vérifie si des tournois non terminés. S'il y en a, propose à
        l'utilisateur de le(s) reprendre, sinon affiche le menu tournoi.
        """
        unfinished_tournaments = self.get_unfinished_tournaments()
        if not unfinished_tournaments:
            self.tournament_menu()
            return

        if result := self.select_tournament_to_resume(unfinished_tournaments):
            self.tournament_model = result
            self.resume_tournament()

        self.tournament_menu()

    def tournament_menu(self):
        """
        Contrôle la fonctionnalité du menu des tournois, permettant à
        l'utilisateur de naviguer à travers les différentes options des
        tournois.
        """
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
                    self.change_participation_player()
                case "3":
                    launch = False
                case _:
                    self.tournament_view.show_error_message_choice(
                        user_choice
                    )
                    helpers.sleep_a_few_seconds()

    def new_tournament(self) -> bool:
        """Vérifie les informations de l'utilisateur et crée le tournoi.
        Retourne un booléen indiquant la validation de sa création.

        Returns:
            bool: Etat de la création du tournoi (True=créé, False=non créé).
        """
        if not self._check_number_participants():
            return False

        self.tournament_model.name = (
            self.tournament_view.get_tournament_name()
        )
        self.tournament_model.location = (
            self.tournament_view.get_tournament_location()
        )
        if not self._check_name_location():
            return False

        self.tournament_model = self.tournament_model.create_new_tournament(
            name=self.tournament_model.name,
            location=self.tournament_model.location,
            participants=self.tournament_model.participants
        )
        self.tournament_view.show_tournament_created(
            self.tournament_model.name,
            self.tournament_model.location
        )
        helpers.sleep_a_few_seconds()
        return True

    def get_participants(self):
        """Récupère tous les joueurs participant."""
        all_players = self.player.player_model.all_players
        participants = [
            player
            for player in all_players
            if player.participation
        ]
        self.tournament_model.participants = participants

    def change_participation_player(self):
        """
        Ajoute ou retire la participation d'un joueur lors du prochain
        tournoi.
        """
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
        if not user_choice:
            return

        index = self.player.check_user_choice(user_choice, players_found)
        if isinstance(index, int):
            player_to_modify = players_found[index]
            player_to_modify.participation = not player_to_modify.participation
            player_to_modify.update_player(modify_participation=True)

    def classification(self, rounds_result: list):
        """Affiche la classification des participants dans le tournoi.

        Args:
            rounds_result (list[PlayerModel]): Liste des participants.
        """
        all_players = self.round.match_controller.sort_by_elo(rounds_result)
        winner = all_players[0]
        self.tournament_model.winner_name = winner.full_name
        winner.points = helpers.convert_if_integer(winner.points)
        self.tournament_view.show_winner(winner.full_name, winner.points)
        for player in all_players:
            player.points = helpers.convert_if_integer(player.points)
            self.tournament_view.show_classification(
                player_name=player.full_name, player_points=player.points
            )

    def get_unfinished_tournaments(self) -> list[TournamentModel]:
        """Retourne la liste des tournois non terminés.

        Returns:
            list[TournamentModel]: Liste des tournois non terminés.
        """
        return [
            tournament
            for tournament in self.tournament_model.all_tournaments
            if not tournament.complete_status
        ]

    def resume_tournament(self):
        """Charge les données et reprend le tournoi."""
        self.tournament_model.create_db_tournament()
        self.load_participants()
        self.sync_round_with_tournament()
        self.start_rounds(resume=True)

    def load_participants(self):
        """
        Charge les participants lors de la reprise d'un tournoi en vérifiant
        le type des participants.
        """
        result = all(
            isinstance(player, dict)
            for player in self.tournament_model.participants
        )
        if result:
            self.tournament_model.participants = [
                self.player.player_model.load_players_from_dict(player)
                for player in self.tournament_model.participants
            ]
        else:
            all_participants_dict = (
                self.tournament_model.get_participants_dict()
            )
            for participant in all_participants_dict:
                for player in self.tournament_model.participants:
                    if player.full_name == (
                        f"{participant['first_name']} "
                        f"{participant['last_name']}"
                    ):
                        player.points = participant['points']

    def sync_round_with_tournament(self):
        """
        Synchronise les participants et la base de données du tournoi avec
        les participants et la base de données du tour.
        """
        self.round.participants = self.tournament_model.participants
        self.round.round_db = self.tournament_model.tournament_db

    def start_rounds(self, resume: bool = False):
        """
        Démarre les rounds selon s'il s'agit d'une reprise ou d'un nouveau
        tournoi.

        Args:
            resume (bool, optional): Etat de la reprise
            (True=reprise, False=nouveau). Défaut False.
        """
        result = self.round.round_menu(
            all_matches_played=self.all_matches_played,
            resume=resume, players_bye=self.tournament_model.players_bye
        )
        self.evaluate_show_classification(result)
        self.round.reset_rounds()

    def evaluate_show_classification(self, result: bool):
        """
        Evalue s'il faut afficher la classification selon le statut du
        tournoi.

        Args:
            result (bool): Statut du tournoi (True=terminé, False=non terminé)
        """
        if result:
            self.classification(self.tournament_model.participants)
            self.get_description()
            self.tournament_model.finish_tournament()
            self.all_matches_played.clear()
            self.tournament_model.players_bye.clear()
        else:
            self.tournament_model.update_tournament()

    def select_tournament_to_resume(
        self, unfinished_tournaments: list[TournamentModel]
    ) -> TournamentModel | None:
        """
        Demande à l'utilisateur et retourne le tournoi si l'utilisateur
        valide la volonté de reprendre le tournoi. Sinon retourne None.

        Args:
            unfinished_tournaments (list[TournamentModel]): Liste des tournois
            non terminés.

        Returns:
            TournamentModel | None: Tournoi à reprendre si valide, sinon None.
        """
        for tournament in unfinished_tournaments:
            resume = self.tournament_view.prompt_resume_tournament(
                tournament.name, tournament.location
            )
            if resume in ["o", "O"]:
                return tournament

        return

    def get_description(self):
        """Demande à l'utilisateur une description à ajouter au tournoi."""
        while True:
            if description := self.tournament_view.get_description():
                self.tournament_model.description = description
                return
            else:
                confirm_choice = self.tournament_view.get_confirm_choice()
                if confirm_choice in ["o", "O"]:
                    return

    def _check_name_location(self) -> bool:
        """
        Vérifie si le nom et le lieu du tournoi ne sont pas vides et ne
        possèdent pas de caractères spéciaux.

        Returns:
            bool: Etat de la vérification du nom (True=valide, False=invalide)
        """
        name_to_check = (
            self.tournament_model.name + self.tournament_model.location
        )
        if any(
            charactere in string.punctuation
            for charactere in name_to_check
        ):
            self.tournament_view.show_error_characteres_name()
            helpers.sleep_a_few_seconds()
            return False
        elif not (
            self.tournament_model.name and self.tournament_model.location
        ):
            self.tournament_view.show_error_empty_name()
            helpers.sleep_a_few_seconds()
            return False

        return True

    def _check_number_participants(self) -> bool:
        """
        Vérifie s'il y a le nombre minimum de participants pour commencer le
        tournoi. Cette valeur est définie par la variable
        "MINIMUM_PLAYER_FOR_TOURNAMENT" dans le module config.

        Returns:
            bool: Etat de la vérification
            (True=assez de joueurs, False=pas assez de joueurs)
        """
        number_of_participants = len(self.tournament_model.participants)
        if number_of_participants < config.MINIMUM_PLAYER_FOR_TOURNAMENT:
            self.tournament_view.show_not_enough_participants(
                number_of_participants
            )
            helpers.sleep_a_few_seconds()
            return False

        return True
