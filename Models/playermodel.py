from typing import ClassVar
from tinydb import TinyDB, Query

import menus

PLAYER_DB = TinyDB("players.json").table("Players")
DEFAULT_NUMBER_OF_POINT = 0


class PlayerModel:
    """Classe joueur"""
    menu_name: ClassVar[str]=menus.PLAYER_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.PLAYER_MENU[menus.OPTIONS_MENU]
    all_players: ClassVar[list]=[]
    participants: ClassVar[list]=[]
    number_of_player: ClassVar[int] = len(all_players)

    def __init__(
        self,
        first_name: str="",
        last_name: str="",
        birth_date: str="",
        club_name: str="",
        tournament_participant: bool=False,
        number_of_points: int=DEFAULT_NUMBER_OF_POINT
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
            tournament_participant (bool, optional): Indique si le joueur
            participe au prochain tournoi. Defaults to False.
            number_of_points (int, optional): Le nombre de points du joueur.
            Defaults to DEFAULT_NUMBER_OF_POINT.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.club_name = club_name
        self.tournament_participant = tournament_participant
        self.number_of_points = number_of_points


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
            f"number_of_points={self.number_of_points}, "
            f"tournament_participant={self.tournament_participant})"
        )

    def __str__(self) -> str:
        """Retourne l'objet PlayerModel sous forme de chaîne de caractères.

        Returns:
            str: Chaîne de caractères représentant l'objet.
        """
        if self.tournament_participant:
            participation = "Oui"
        else:
            participation = "Non"
        return (
            f"Nom: {self.first_name} {self.last_name} \t"
            f"Club: {self.club_name} \t"
            f"Date de naissance: {self.birth_date} \t"
            f"Participant au tournoi: {participation}"
        )

    @classmethod
    def load_all_players(cls):
        all_players = PLAYER_DB.all()
        for player in all_players:
            cls.all_players.append(cls(**player))

    def create_player(self, first_name, last_name, birth_date, club_name):
        return PlayerModel(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            club_name=club_name
        )

    def save_player(self):
        PLAYER_DB.insert(self.__dict__)

if __name__ == "__main__":
    playermodel = PlayerModel()
    player = playermodel.create_player(
        first_name="Jean",
        last_name="Michel",
        birth_date= "09/09/1998",
        club_name="Club 1"
    )
    print(player)
    player.save_player()
    player.load_all_players()
    for player in PlayerModel.all_players:
        print(repr(player))
