from typing import ClassVar
from tinydb import TinyDB, Query

import config
import menus

CLUB_DB = TinyDB(config.SAVING_PATH_CLUB, indent=4).table("Clubs")

class ClubModel:
    """Classe Club"""
    menu_name: ClassVar[str]=menus.CLUB_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.CLUB_MENU[menus.OPTIONS_MENU]
    all_clubs: ClassVar[list['ClubModel']]=[]

    def __init__(
            self,
            name: str="",
            national_chest_id: str="",

        ):
        self.name = name
        self.national_chest_id = national_chest_id

    def save_club(self):
        CLUB_DB.insert(self.__dict__)

    @staticmethod
    def create_club(name, national_chest_id):
        club = ClubModel(name=name, national_chest_id=national_chest_id)
        club.save_club()
        ClubModel.all_clubs.append(club)

        return club

    @classmethod
    def load_clubs(cls):
        all_clubs = CLUB_DB.all()
        for club in all_clubs:
            cls.all_clubs.append(cls(**club))

    def modify_club(self):
        Club = Query()
        CLUB_DB.update(
            self.__dict__,
            Club.national_chest_id == self.national_chest_id
        )