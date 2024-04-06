from tinydb import TinyDB, where
from typing import ClassVar

import helpers
import menus

class RoundModel:
    menu_name: ClassVar[str]=menus.ROUND_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.ROUND_MENU[menus.OPTIONS_MENU]

    def __init__(
            self,
            round_number: int=0,
            date_time_start: str="",
            date_time_end: str="",
            matches: list=[]
        ):
        self.round_number=round_number
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.matches = matches

    def __str__(self) -> str:
        if not self.date_time_start:
            self.date_time_start = "Non commencé"

        if not self.date_time_end:
            self.date_time_end = "Non terminé"

        return f"Nom: Round {self.round_number}, Date de début: {self.date_time_start}, Date de fin: {self.date_time_end}, Nombre de match: {len(self.matches)}"

    def __repr__(self) -> str:
        return f"RoundModel{self.round_number, self.date_time_start, self.date_time_end}"

    @staticmethod
    def create_new_round(round_number, matches):
        date_string = str(helpers.get_date_time())
        return RoundModel(
            round_number=round_number,
            date_time_start=date_string,
            matches=matches
            )
    @staticmethod
    def _create_db_table(tournament_db):
        return tournament_db.table("Rounds")

    def save_round(self, tournament_db):
        table = self._create_db_table(tournament_db)
        table.insert(self.__dict__)

    def update_round(self, tournament_db):
        table = self._create_db_table(tournament_db)
        table.update(self.__dict__, where("round_number") == self.round_number)
    
    @classmethod
    def load_rounds(cls, tournament_db: TinyDB) -> list['RoundModel']:
        table = cls._create_db_table(tournament_db)
        return [cls(**round) for round in table]
            