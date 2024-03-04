from dataclasses import dataclass
from datetime import datetime
from pprint import pprint
from typing import ClassVar
from pathlib import Path
from faker import Faker
from Model.tournamentmodel import Tournament, PATH_TOURNAMENT
from Model.timesetmodel import Timer
from random import randint
import json

DIR_PATH = Path(__file__).parent.parent
SAVING_PATH_PLAYERS = DIR_PATH / "data" / "players.json"

POINT_PER_WIN = 1
POINT_PER_LOSE = 0
POINT_PER_DRAW = 0.5
DEFAULT_MATCH_NUMBER = 4
NUMBER_MATCH_PLAYER = 2

@dataclass
class Match:
    """Classe Match"""
    match_list : list
    date_time_start : datetime
    date_time_end : datetime
    current_match_number : int
    number_of_match : int = DEFAULT_MATCH_NUMBER

    @staticmethod
    def create_new_matchs(): # Tuple (["Nom_joueur_1", "score"], ["Nom_joueur_2", "score"],)
        """Créée une nouvelle liste de matchs et les enregistre.

        Returns:
            fonction: Sauvegarde la nouvelle liste de match.
        """
        all_match_list = []
        player_list = Tournament.get_list_of_tournament_player()
        for _ in player_list:
            first_player = player_list.pop(randint(1, len(player_list)-1))
            second_player = player_list.pop(randint(1, len(player_list)-2))
            match_pair = (
                tuple(first_player.values()),
                tuple(second_player.values())
                )
            all_match_list.append(tuple(match_pair))
        pprint(all_match_list)
        return Match._save_match(all_match_list)
    
    @staticmethod
    def _save_match(datas):
        """Sauvegarde la liste de match en json.

        Args:
            datas (list): Liste des matchs

        Returns:
            list: Retourne la liste des matchs sauvegardés.
        """
        date = Timer.get_date()
        file_name = f"Round 1 - {date}.json"
        complete_path = PATH_TOURNAMENT / file_name
        with open(complete_path, "w", encoding="utf-8") as file:
            json.dump(datas, file,ensure_ascii=False, indent=4)
        return datas

    def start_match(self):
        pass

    def end_match(self):
        pass

Match.create_new_matchs()