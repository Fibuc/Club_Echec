from pathlib import Path
from random import randint

import helpers
import menus

INDEX_PLAYER_NAME = 0
INDEX_PLAYER_POINT = 1
PLAYER_PATH = "C:/Users/Fibuc/Documents/depot_github/Club d'échec/players.json"
MATCH_PATH = "C:/Users/Fibuc/Documents/depot_github/Club d'échec/match.json"

NOT_ENDED_TOURNAMENT_PREFIX = "Incomplete_"

import json
from typing import ClassVar


class TournamentModel:
    """Classe Tournois"""
    menu_name: ClassVar[str]=menus.TOURNAMENT_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.TOURNAMENT_MENU[menus.OPTIONS_MENU]
    all_tournaments: ClassVar[list]=[]
    unfinished_tournament: ClassVar[list]=[]

    def __init__(
            self,
            name: str="",
            location: str="",
            players_list: list=[],
            rounds_list: list=[],
            date_time_start: str="Non commencé",
            date_time_end : str="Non terminé",
            description : str="Aucune description",
    ):
        self.name = name
        self.location = location
        self.players_list = players_list
        self.rounds_list = rounds_list
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.description = description

    def __repr__(self) -> str:
        """Retourne la représentation de l'objet sous forme de chaîne de
        caractères de l'objet TournamentModel.

        Returns:
            str: Chaîne de caractère de la représentation de l'objet.
        """
        return (
            f"TournamentModel(name='{self.name}', "
            f"location='{self.location}', players_list='{self.players_list}', "
            f"rounds_list='{self.rounds_list}', "
            f"date_time_start={self.date_time_start}, "
            f"date_time_end={self.date_time_end}, "
            f"description={self.description})"
        )

    def __str__(self):
        """Retourne l'objet TournamentModel sous forme de chaîne de 
        caractères.

        Returns:
            str: Représentation de l'instance en chaîne de caractères.
        """
        if self.players_list:
            players = len(self.players_list)
            plural_player = f"{"s" if players > 1 else ""}"
        else:
            players = 0
            plural_player = "s"
        if self.rounds_list:
            rounds = len(self.rounds_list)
            plural_round = f"{"s" if rounds > 1 else ""}"
        else:
            rounds = 0
            plural_round = "s"

        return (
            f"Nom: {self.name} \tLieu: {self.location} \t"
            f"Nombre de participant{plural_player}: {players}\t"
            f"Nombre de round{plural_round}: {rounds}\t"
            f"Date début: {self.date_time_start} \tDate fin: "
            f"{self.date_time_end} \t Description: {self.description}"
        )

    def create_new_tournament(
            self,
            name: str,
            location: str,
            players_list: list,
            rounds_list: list=[],
            date_time_start: str="Non commencé",
            date_time_end : str="Non terminé",
            description : str="Aucune description"
        ):
        """Créée une instance de la classe TournamentModel, l'ajoute à la liste
        des instances de la classe TournamentModel et sauvegarde cette nouvelle
        liste.

        Args:
            name (str): Nom du tournoi.
            location (str): Lieu du tournoi.
            players_list (list): Liste des joueurs participants.
            rounds_list (list): Liste des rounds du tournois.
            date_time_start (str): Date du début du tournois.
            date_time_end (str): Date de la fin du tournois.
            description (str): Description du tournois.
        """
        tournament = TournamentModel(
            name=name,
            location=location,
            players_list=players_list,
            rounds_list=rounds_list,
            date_time_start=date_time_start,
            date_time_end=date_time_end,
            description=description
        )
        TournamentModel.all_tournaments.append(tournament)
        tournament.save_tournament()

    def save_tournament(self, ended_tournament: bool=False):
        """Enregistre dans le fichier de sauvegarde toutes les instances de
        PlayerTournament présents dans la variable 
        PlayerTournament.all_tournaments.

        Args:
            ended_tournament (bool, optional): Indique si le tournois est
            terminé. Defaults to False.
        """
        menus.TOURNAMENT_DIR.mkdir(exist_ok=True, parents=True)
        date = helpers.get_date()
        prefix = NOT_ENDED_TOURNAMENT_PREFIX
        if ended_tournament:
            prefix = ""

        file_name = f"{prefix}Tournament {self.location} - {date}.json"
        complete_path = menus.TOURNAMENT_DIR / file_name
        with open(complete_path, "w", encoding="utf-8") as file:
            json.dump(self.__dict__, file,ensure_ascii=False, indent=4)


    @staticmethod
    def load_all_tournaments():
        for tournament_file in menus.TOURNAMENT_DIR.glob("*"):
            with open(tournament_file, "r",encoding="UTF-8") as file:
                tournament = TournamentModel(**json.load(file))
                TournamentModel.all_tournaments.append(tournament)

    def load_unfinished_tournament(self):
        unfinished_tournaments = []
        for tournament in menus.TOURNAMENT_DIR.glob("*"):
            if tournament.name.startswith(NOT_ENDED_TOURNAMENT_PREFIX):
                with open(tournament, "r",encoding="UTF-8") as file:
                    unfinished_tournaments.append(json.load(file))
        return unfinished_tournaments


class MatchModel:
    def __init__(
            self,
            number_of_player=0,
            number_of_match=0,
            winner_point=1,
            loser_point=0,
            draw_point=0.5,
            players_per_match=2,
            all_players_dict={},
            all_player_list=[],
            all_match_played=[],
            player_path=Path(PLAYER_PATH),
            match_path=Path(MATCH_PATH)
        ):
        self.winner_point  = winner_point
        self.loser_point = loser_point
        self.draw_point = draw_point
        self.players_per_match = players_per_match
        self.all_players_dict = all_players_dict
        self.all_player_list = all_player_list
        self.number_of_player = number_of_player
        self.number_of_match = number_of_match
        self.all_match_played = all_match_played
        self.player_path = player_path
        self.match_path = match_path

    def create_first_matchs(self):
        self.load_players()
        for _ in range(self.number_of_match):
            first_player = self.all_player_list.pop(
                randint(0, len(self.all_player_list)-1)
            )
            second_player = self.all_player_list.pop(
                randint(0, len(self.all_player_list)-1)
            )
            match_pair = (
                [
                    first_player[INDEX_PLAYER_NAME],
                    first_player[INDEX_PLAYER_POINT]
                ],
                [
                    second_player[INDEX_PLAYER_NAME],
                    second_player[INDEX_PLAYER_POINT]
                ]
            )
            self.all_match_played.append(match_pair)
        self.save_matchs()

    def end_match(self):
        for match in range(self.number_of_match):
            pass


    def create_others_matchs(self):
        self.load_players()
        self.sorted_player_by_elo()
        for match in range(self.number_of_match):
            player_1 = self.all_player_list[0]
            player_2 = self.all_player_list[1]




    def check_already_played_together(self):
        self.load_matchs()
        matchs_list_to_check = []
        for match in self.all_match_played:
            name_first_player = match[0][INDEX_PLAYER_NAME]
            name_second_player = match[1][INDEX_PLAYER_NAME]
            matchs_list_to_check.append(
                tuple((name_first_player, name_second_player))
            )
            matchs_list_to_check.append(
                tuple((name_second_player, name_first_player))
            )


    def sorted_player_by_elo(self):
        self.all_player_list = sorted(
            self.all_player_list, key=lambda
            point: point[INDEX_PLAYER_POINT], reverse=True
        )

    def load_players(self):
        with open(self.player_path, "r", encoding='UTF-8') as file:
            self.all_players_dict = json.load(file)
            for player in self.all_players_dict:
                self.all_player_list.append(
                    self._extract_player_name_and_points(player)
                )
        self.number_of_player = len(self.all_player_list)
        self.number_of_match = self.number_of_player // self.players_per_match

    def _extract_player_name_and_points(self, player):
        player_first_name = player[menus.KEY_PLAYER_FIRST_NAME]
        player_last_name = player[menus.KEY_PLAYER_LAST_NAME]
        player_full_name = f"{player_first_name} {player_last_name}"
        player_points = player[menus.KEY_PLAYER_NUMBER_POINT]
        return [player_full_name, player_points]

    def load_matchs(self):
        if self.match_path.exists():
            with open(self.match_path, "r", encoding='UTF-8') as file:
                datas = json.load(file)
            for data in datas:
                self.all_match_played.append(tuple(data))

    def save_matchs(self):
        with open(self.match_path, "w", encoding='UTF-8') as file:
            json.dump(self.all_match_played, file, ensure_ascii=False, indent=4)


class RoundModel:
    menu_name: ClassVar[str]=menus.ROUND_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.ROUND_MENU[menus.OPTIONS_MENU]
    number_of_round: ClassVar[int]=helpers.DEFAULT_NUMBER_ROUNDS
    current_round: ClassVar[int]=1
    all_rounds: ClassVar[list]=[]
    def __init__(
            self,
            date_time_start="Non commencé",
            date_time_end="Non terminé",
            matchs=[]
        ):
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.matchs = matchs

    def __str__(self) -> str:
        return f"Nom: Round {self.current_round}, Date de début: {self.date_time_start}, Date de fin: {self.date_time_end}"

    def __repr__(self) -> str:
        return f"RoundModel({self.number_of_round, self.date_time_start, self.date_time_end, self.current_round})"


    def create_new_round(self):
        date_string = str(helpers.get_date_time())
        return RoundModel(date_time_start=date_string)

    def add_new_matchs(self, matchs):
        self.matchs.append(matchs)

    @staticmethod
    def extract_rounds_dict_datas():
        all_informations = []
        for round in RoundModel.all_rounds:
            all_informations.append(round.__dict__)
        return all_informations