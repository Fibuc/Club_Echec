from typing import ClassVar

from tinydb import TinyDB, Query

import config
import menus

PLAYER_DB = TinyDB(config.SAVING_PATH_PLAYERS, indent=4).table("Players")


class PlayerModel:
    """Classe modèle joueur"""
    menu_name: ClassVar[str] = menus.PLAYER_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list] = menus.PLAYER_MENU[menus.OPTIONS_MENU]
    all_players: ClassVar[list['PlayerModel']] = []

    def __init__(
        self, first_name: str = "", last_name: str = "", birth_date: str = "",
        club_name: str = "", participation: bool = False,
        points: float = config.DEFAULT_NUMBER_OF_POINT
    ):
        """Initialise l'instance de classe joueur.

        Args:
            first_name (str, optional): Prénom du joueur. Défaut "".
            last_name (str, optional): Nom de famille du joueur. Défaut "".
            birth_date (str, optional): Date de naissance du joueur.
            Défaut "".
            club_name (str, optional): Nom du club du joueur. Défaut "".
            participation (bool, optional): Participation au prochain tournoi.
            Défaut False.
            points (float, optional): Nombre de points du joueur.
            Défaut config.DEFAULT_NUMBER_OF_POINT.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.club_name = club_name
        self.participation = participation
        self.points = points

    def __repr__(self) -> str:
        """Retourne la représentation sous forme de chaîne de
        caractères de l'instance PlayerModel.

        Returns:
            str: Chaîne de caractères de la représentation de l'objet.
        """
        return (
            f"PlayerModel(first_name='{self.first_name}', "
            f"last_name='{self.last_name}', club_name='{self.club_name}', "
            f"birth_date='{self.birth_date}', "
            f"participation='{self.participation}', "
            f"points='{self.points}')"
        )

    def __str__(self) -> str:
        """Retourne l'instance PlayerModel sous forme de chaîne de caractères.

        Returns:
            str: Chaîne de caractères représentant l'objet.
        """
        participation = "Oui" if self.participation else "Non"
        return (
            f"Nom: {self.first_name} {self.last_name}\t"
            f"Date de naissance: {self.birth_date}\t"
            f"Club: {self.club_name}\t"
            f"Participant au tournoi: {participation}"
        )

    def sort_players(self):
        """Trie la liste de tous les joueurs par ordre alphabétique"""
        PlayerModel.all_players = sorted(
            self.all_players,
            key=lambda x: (x.first_name, x.last_name)
        )

    @classmethod
    def load_players(cls):
        """
        Charge tous les joueurs présents dans la base de données en instances de
        classe et les ajoute à la liste de classe "all_players" contenant tous
        les joueurs.
        """
        all_players = PLAYER_DB.all()
        for player in all_players:
            cls.all_players.append(cls(**player))

    @classmethod
    def load_players_from_dict(cls, player: dict) -> "PlayerModel":
        """Crée une instance de classe à partir d'un dictionnaire.

        Args:
            player (dict): Informations du joueur.

        Returns:
            PlayerModel: Instance de PlayerModel créée.
        """
        return cls(**player)

    @staticmethod
    def create_player(
        first_name: str, last_name: str, birth_date: str,
        club_name: str, participation=False
    ) -> "PlayerModel":
        """Crée une instance de classe PlayerModel.

        Args:
            first_name (str): Prénom du joueur.
            last_name (str): Nom de famille du joueur.
            birth_date (str): Date de naissance du joueur.
            club_name (str): Nom du club du joueur.
            participation (bool, optional): Participation au prochain tournoi.
            Défaut False.

        Returns:
            PlayerModel: Instance de PlayerModel créée.
        """
        player = PlayerModel(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            club_name=club_name,
            participation=participation
        )
        player.save_player()

        return player

    def save_player(self):
        """
        Sauvegarde l'instance de classe dans la base de données des joueurs.
        """
        PLAYER_DB.insert(self.__dict__)

    def update_player(
        self, first_name: str = "", last_name: str = "", birth_date: str = "",
        club_name: str = "", modify_participation: bool = False
    ):
        """
        Met à jour les informations de l'instance du joueur dans la base de
        données. L'option "modify_participation=True" permet de mettre à jour
        uniquement la participation du joueur.

        Args:
            first_name (str, optional): Prénom du joueur. Défaut "".
            last_name (str, optional): Nom de famille du joueur. Défaut "".
            birth_date (str, optional): Date de naissance du joueur.
            Défaut "".
            club_name (str, optional): Nom du club du joueur. Défaut "".
            modify_participation (bool, optional): Participation au prochain
            tournoi. Défaut False.
        """
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
        if modify_participation:
            PLAYER_DB.update(self.__dict__, condition)
        else:
            for key, value in element_to_modify.items():
                if value != "":
                    PLAYER_DB.update({key: value}, condition)

    @classmethod
    def clear_participants(cls):
        """Attribut False au statut de participation de tous les joueurs."""
        for player in cls.all_players:
            player.participation = False
            player.update_player(modify_participation=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
