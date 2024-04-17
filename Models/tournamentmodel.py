from pathlib import Path
from typing import ClassVar

from tinydb import TinyDB

from Models.playermodel import PlayerModel

import config
import helpers
import menus

TOURNAMENT_DIR = config.TOURNAMENT_DIR


class TournamentModel:
    """Classe modèle des tournois"""
    menu_name: ClassVar[str] = menus.TOURNAMENT_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list] = menus.TOURNAMENT_MENU[menus.OPTIONS_MENU]
    all_tournaments: ClassVar[list['TournamentModel']] = []

    def __init__(
        self, name: str = "", location: str = "",
        participants: list[PlayerModel] = [], players_bye: list[str] = [],
        winner_name: str = "", description: str = "Aucune description",
        complete_status: bool = False,
        tournament_path: Path = Path(TOURNAMENT_DIR), tournament_db: TinyDB = None
    ):
        """Initialise l'instance de classe TournamentModel.

        Args:
            name (str, optional): Nom du tournoi. Défaut "".
            location (str, optional): Lieu du tournoi. Défaut "".
            participants (list[PlayerModel], optional): Participants du
            tournoi. Défaut [].
            players_bye (list, optional): Joueurs en bye. Défaut [].
            winner_name (str, optional): Nom du vainqueur. Défaut "".
            description (str, optional): Description du tournoi.
            Défaut "Aucune description".
            complete_status (bool, optional): Statut du tournoi. Défaut False.
            tournament_path (Path, optional): Chemin d'enregistrement du tournoi.
            Défaut Path(TOURNAMENT_DIR).
            tournament_db (TinyDB, optional): Base de données du tournoi.
            Défaut None.
        """
        self.name = name
        self.location = location
        self.participants = participants
        self.players_bye = players_bye
        self.winner_name = winner_name
        self.description = description
        self.complete_status = complete_status
        self.tournament_path = tournament_path
        self.tournament_db = tournament_db

    def __repr__(self) -> str:
        """Retourne la représentation sous forme de chaîne de
        caractères de l'instance TournamentModel.

        Returns:
            str: Chaîne de caractères de la représentation de l'objet.
        """
        return (
            f"TournamentModel(name='{self.name}', "
            f"location='{self.location}', participants='{self.participants}', "
            f"players_bye='{self.players_bye}', winner='{self.winner_name}'"
            f"description='{self.description}', "
            f"complete_status='{self.complete_status}', "
            f"tournament_path='{self.tournament_path}', "
            f"tournament_db='{self.tournament_db}')"
        )

    def __str__(self):
        """
        Retourne l'objet TournamentModel sous forme de chaîne de
        caractères.

        Returns:
            str: Représentation de l'instance en chaîne de caractères.
        """
        if self.complete_status:
            status = "Terminé"
            winner = f"\nVainqueur: {self.winner_name}"
        else:
            status = "Non terminé"
            winner = ""
        return (
            f"Nom: {self.name}\nLieu: {self.location}\n"
            f"Statut: {status}{winner}\nDescription: {self.description}"
        )

    @classmethod
    def load_all_tournaments(cls):
        """
        Charge toutes les instances de classe à partir des bases de données
        et les ajoute à la liste de classe "all_tournaments".
        """
        for tournament_file in TOURNAMENT_DIR.glob("*.json"):
            table = TinyDB(tournament_file).table("Tournament")
            tournament_info = (table.all())[0]
            tournament_instance = cls(**tournament_info)
            tournament_instance.tournament_path = tournament_file
            cls.all_tournaments.append(tournament_instance)

    def get_participants_dict(self) -> list[dict]:
        """Récupère et retourne la liste contenant tous les dictionnaires
        correspondants aux informations des participants à partir de la base
        de données.

        Returns:
            list[dict]: Retourne la liste des dictionnaires des participants.
        """
        table = self._create_db_table()
        tournament = table.all()[-1]
        return tournament["participants"]

    def create_new_tournament(
            self, name: str, location: str, participants: list = []
    ) -> "TournamentModel":
        """
        Crée une instance de classe TournamentModel.

        Args:
            name (str): Nom du tournoi.
            location (str): Lieu du tournoi.
            participants (list, optional): Liste des participants. Défaut [].

        Returns:
            TournamentModel: Instance de TournamentModel créée.
        """
        tournament = TournamentModel(
            name=name, location=location, participants=participants
        )
        TournamentModel.all_tournaments.append(tournament)
        tournament._save_tournament()
        return tournament

    def _save_tournament(self):
        """
        Enregistre l'instance de classe dans une nouvelle base de données.
        """
        TOURNAMENT_DIR.mkdir(exist_ok=True, parents=True)
        date = helpers.get_date()
        file_name = f"Tournament {self.name} {self.location} - {date}.json"
        self.tournament_path = self.tournament_path / file_name
        self.create_db_tournament()
        table = self._create_db_table()
        table.insert(self._serialize_tournament())

    def update_tournament(self):
        """
        Met à jour les informations de l'instance dans la base de données.
        """
        table = self._create_db_table()
        table.update(self._serialize_tournament())

    def finish_tournament(self):
        """
        Indique le statut du tournoi comme terminé et le met à jour dans la
        base de données.
        """
        self.complete_status = True
        table = self._create_db_table()
        table.update(self._serialize_tournament())

    def create_db_tournament(self):
        """Crée base de données correspondant à l'instance."""
        self.tournament_db = TinyDB(self.tournament_path, indent=4)

    def _serialize_tournament(self) -> dict:
        """
        Retourne toutes les informations de l'instance sous forme de
        dictionnaire.

        Returns:
            dict: Dictionnaire des informations de l'instance.
        """
        participants_dict = self._serialize_participants()
        return {
                "name": self.name,
                "location": self.location,
                "participants": participants_dict,
                "players_bye": self.players_bye,
                "winner_name": self.winner_name,
                "description": self.description,
                "complete_status": self.complete_status
                }

    def _serialize_participants(self) -> list[dict]:
        """
        Retourne une liste comprenant toutes les informations des
        participants sous forme de dictionnaires.

        Returns:
            list[dict]: Liste des dictionnaires des informations des
            participants.
        """
        return [player.__dict__ for player in self.participants]

    def _create_db_table(self) -> TinyDB.table_class:
        """
        Crée une table "Tournament" dans la base de données.

        Returns:
            TinyDB.table_class: La table dans la base de données.
        """
        return self.tournament_db.table("Tournament")
