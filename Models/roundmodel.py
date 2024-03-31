from tinydb import TinyDB
from typing import ClassVar

import helpers
import menus

class RoundModel:
    menu_name: ClassVar[str]=menus.ROUND_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.ROUND_MENU[menus.OPTIONS_MENU]
    round_db: ClassVar[TinyDB]

    def __init__(
            self,
            round_number: int=0,
            date_time_start: str="Non commencé",
            date_time_end: str="Non terminé",
            matches: list=[]
        ):
        self.round_number=round_number
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.matches = matches

    def __str__(self) -> str:
        return f"Nom: Round {self.round_number}, Date de début: {self.date_time_start}, Date de fin: {self.date_time_end}, Nombre de match: {len(self.matches)}"

    def __repr__(self) -> str:
        return f"RoundModel{self.round_number, self.date_time_start, self.date_time_end}"

    def create_new_round(self, round_number, matches):
        date_string = str(helpers.get_date_time())
        return RoundModel(
            round_number=round_number,
            date_time_start=date_string,
            matches=matches
            )

    def save_round(self):
        db = RoundModel.round_db.table("Rounds")
        db.insert(self.__dict__)

    def update_round(self):
        db = RoundModel.round_db.table("Rounds")
        db.update(self.__dict__)