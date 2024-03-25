import helpers
import menus
from tournamentmodel import INDEX_PLAYER_NAME, INDEX_PLAYER_POINT


from tinydb import TinyDB


import json
from typing import ClassVar


class RoundModel:
    menu_name: ClassVar[str]=menus.ROUND_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.ROUND_MENU[menus.OPTIONS_MENU]
    number_of_round: ClassVar[int]=helpers.DEFAULT_NUMBER_ROUNDS
    round_db: ClassVar[TinyDB]
    current_round: ClassVar[int]=0
    all_rounds: ClassVar[list]=[]
    all_match_played: ClassVar[list]=[]
    all_player_list: ClassVar[list]=[]

    def __init__(
            self,
            date_time_start: str="Non commencé",
            date_time_end: str="Non terminé",
            matchs: list=[]
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
        round = RoundModel(date_time_start=date_string)
        RoundModel.all_rounds.append(round)
        RoundModel.current_round += 1

        return round

    def save_round(self):
        db = RoundModel.round_db.table("Rounds")
        db.insert(self.__dict__)


    def add_new_matchs(self, matchs):
        self.matchs.append(matchs)

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


    def sorted_by_elo(self):
        RoundModel.all_player_list = sorted(
            RoundModel.all_player_list, key=lambda player: (
                player.number_of_points,
                player.first_name,
                player.last_name
            )
        )
