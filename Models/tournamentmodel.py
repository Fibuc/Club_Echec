from pathlib import Path
from tinydb import TinyDB
from typing import ClassVar


import helpers
import menus 

TOURNAMENT_DIR = menus.TOURNAMENT_DIR

class TournamentModel:
    """Classe Tournois"""
    menu_name: ClassVar[str]=menus.TOURNAMENT_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.TOURNAMENT_MENU[menus.OPTIONS_MENU]
    all_tournaments: ClassVar[list['TournamentModel']]=[]

    def __init__(
            self,
            name: str="",
            location: str="",
            participants: list=[],
            players_bye: list=[],
            description : str="Aucune description",
            complete_status: bool=False,
            tournament_path: Path=Path(TOURNAMENT_DIR),
            tournament_db: TinyDB=None
    ):
        self.name = name
        self.location = location
        self.participants = participants
        self.players_bye = players_bye
        self.description = description
        self.complete_status = complete_status
        self.tournament_path = tournament_path
        self.tournament_db = tournament_db

    def __repr__(self) -> str:
        """Retourne la représentation de l'objet sous forme de chaîne de
        caractères de l'objet TournamentModel.

        Returns:
            str: Chaîne de caractère de la représentation de l'objet.
        """
        return (
            f"TournamentModel(name='{self.name}', "
            f"location='{self.location}', players_list='{self.participants}', "
            f"description={self.description}, "
            f"complete_status='{self.complete_status}')"
        )

    def __str__(self):
        """Retourne l'objet TournamentModel sous forme de chaîne de 
        caractères.

        Returns:
            str: Représentation de l'instance en chaîne de caractères.
        """
        players = len(self.participants) if self.participants else 0
        status = "Terminé" if self.complete_status else "Non terminé"
        return (
            f"Nom: {self.name} \tLieu: {self.location} \t"
            f"Nombre de participants: {players}\t"
            f"Description: {self.description}\t Statut: {status}"
        )

    @classmethod
    def load_all_tournaments(cls):
        for tournament_file in TOURNAMENT_DIR.glob("*.json"):
            table = TinyDB(tournament_file).table("Tournament")
            tournament_info = (table.all())[0]
            tournament_instance = cls(**tournament_info)
            tournament_instance.tournament_path = tournament_file
            cls.all_tournaments.append(tournament_instance)

    def load_participants(self):
        table = self._create_db_table()
        tournament = table.all()[-1]
        return tournament["participants"]

    def create_new_tournament(
            self, name: str, location: str, players_list: list=[]
    ):
        tournament = TournamentModel(
            name=name, location=location, participants=players_list
        )
        TournamentModel.all_tournaments.append(tournament)
        tournament.save_tournament()
        return tournament
    
    def save_tournament(self):
        TOURNAMENT_DIR.mkdir(exist_ok=True, parents=True)
        date = helpers.get_date()
        file_name = f"Tournament {self.name} {self.location} - {date}.json"
        self.tournament_path = self.tournament_path / file_name
        self.create_db_tournament()
        table = self._create_db_table()
        table.insert(self._serialize_tournament())

    def update_tournament(self):
        table = self._create_db_table()
        table.update(self._serialize_tournament())

    def finish_tournament(self):
        self.complete_status = True
        table = self._create_db_table()
        table.update(self._serialize_tournament())

    def create_db_tournament(self):
        self.tournament_db = TinyDB(self.tournament_path, indent=4)

    def _serialize_tournament(self):
        participants_dict = self._serialize_participants()
        return {
                "name": self.name,
                "location": self.location,
                "participants": participants_dict,
                "players_bye": self.players_bye,
                "description": self.description, 
                "complete_status": self.complete_status
            }
    
    def _serialize_participants(self):
        return [player.__dict__ for player in self.participants]

    def _create_db_table(self):
        return self.tournament_db.table("Tournament")