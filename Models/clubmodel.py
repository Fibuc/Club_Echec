from typing import ClassVar

from tinydb import TinyDB, Query

import config
import menus

CLUB_DB = TinyDB(config.SAVING_PATH_CLUB, indent=4).table("Clubs")


class ClubModel:
    """Classe modèle des clubs"""
    menu_name: ClassVar[str] = menus.CLUB_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list] = menus.CLUB_MENU[menus.OPTIONS_MENU]
    all_clubs: ClassVar[list['ClubModel']] = []

    def __init__(
        self, name: str = "", national_chest_id: str = ""
    ):
        """Initialise l'instance de classe ClubModel.

        Args:
            name (str, optional): Nom de l'instance. Défaut "".
            national_chest_id (str, optional): Identifiant national de
            l'instance. Défaut "".
        """
        self.name = name
        self.national_chest_id = national_chest_id

    def save_club(self):
        """
        Sauvegarde l'instance de classe dans la base de données des clubs.
        """
        CLUB_DB.insert(self.__dict__)

    def update_club(self):
        """
        Met à jour les informations de l'instance dans la base de données.
        """
        Club = Query()
        CLUB_DB.update(
            self.__dict__,
            Club.national_chest_id == self.national_chest_id
        )

    @staticmethod
    def create_club(name: str, national_chest_id: str) -> "ClubModel":
        """
        Crée une instance de classe ClubModel.

        Args:
            name (str): Nom du club.
            national_chest_id (str): Identifiant du club.

        Returns:
            ClubModel: Instance ClubModel créée.
        """
        club = ClubModel(name=name, national_chest_id=national_chest_id)
        club.save_club()
        ClubModel.all_clubs.append(club)
        return club

    @classmethod
    def load_clubs(cls):
        """
        Charge tous les clubs présents dans la base de données en instances de
        classe et les ajoute à la liste de classe "all_clubs" contenant tous
        les clubs.
        """
        all_clubs = CLUB_DB.all()
        for club in all_clubs:
            cls.all_clubs.append(cls(**club))
