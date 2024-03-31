from typing import ClassVar
from tinydb import TinyDB, Query

import menus
from helpers import DEFAULT_NUMBER_OF_POINT

PLAYER_DB = TinyDB(menus.SAVING_PATH_PLAYERS).table("Players")

class PlayerModel:
    """Classe joueur"""
    menu_name: ClassVar[str]=menus.PLAYER_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.PLAYER_MENU[menus.OPTIONS_MENU]
    all_players: ClassVar[list]=[]

    def __init__(
        self,
        first_name: str="",
        last_name: str="",
        birth_date: str="",
        club_name: str="",
        participation: bool=False,
        points: float=DEFAULT_NUMBER_OF_POINT
    ):
        """Initialise un joueur avec les attributs spécifiés.

        Args:
            first_name (str, optional): Le prénom du joueur. Defaults to "".
            last_name (str, optional): Le nom de famille du joueur.
            Defaults to "".
            birth_date (str, optional): La date de naissance du joueur au
            format 'DD/MM/AAAA'. Defaults to "".
            club_name (str, optional): Le nom du club auquel le joueur est
            assigné. Defaults to "".
            participation (bool, optional): Indique si le joueur
            participe au prochain tournoi. Defaults to False.
            points (int, optional): Le nombre de points du joueur.
            Defaults to DEFAULT_NUMBER_OF_POINT.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.club_name = club_name
        self.participation = participation
        self.points = points


    def __repr__(self) -> str:
        """Retourne la représentation de l'objet sous forme de chaîne de
        caractères de l'objet PlayerModel.

        Returns:
            str: Chaîne de caractère de la représentation de l'objet.
        """
        return (
            f"PlayerModel(first_name='{self.first_name}', "
            f"last_name='{self.last_name}', club_name='{self.club_name}', "
            f"birth_date='{self.birth_date}', "
            f"number_of_points={self.points}, "
            f"tournament_participant={self.participation})"
        )

    def __str__(self) -> str:
        """Retourne l'objet PlayerModel sous forme de chaîne de caractères.

        Returns:
            str: Chaîne de caractères représentant l'objet.
        """
        if self.participation:
            participation = "Oui"
        else:
            participation = "Non"
        return (
            f"Nom: {self.first_name} {self.last_name}\t"
            f"Date de naissance: {self.birth_date}\t"
            f"Club: {self.club_name}\t"
            f"Participant au tournoi: {participation}"
        )

    def sort_players(self):
        PlayerModel.all_players = sorted(
            self.all_players,
            key=lambda x: (x.first_name, x.last_name)
        )

    @classmethod
    def load_players(cls):
        all_players = PLAYER_DB.all()
        for player in all_players:
            cls.all_players.append(cls(**player))

    @staticmethod
    def create_player(first_name, last_name, birth_date, club_name):
        player = PlayerModel(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            club_name=club_name
        )
        player.save_player()

        return player

    def save_player(self):
        PLAYER_DB.insert(self.__dict__)

    def modify_player(
        self,
        first_name: str="",
        last_name: str="",
        birth_date: str="",
        club_name: str="",
        participation: str=""

    ):
        Player = Query()
        element_to_modify = {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "club_name": club_name
        }
        condition = (
            (Player.first_name == self.first_name) &
            (Player.last_name == self.last_name) &
            (Player.birth_date == self.birth_date) &
            (Player.club_name == self.club_name)
        )
        if participation:
            PLAYER_DB.update(self.__dict__, condition)
        else:
            for key, value in element_to_modify.items():
                if value != "":
                    PLAYER_DB.update({key: value}, condition)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
