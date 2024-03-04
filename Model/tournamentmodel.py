from dataclasses import dataclass, field
import json

from Model.timesetmodel import Timer
import Model.playermodel as playermodel

PATH_PLAYER_LIST = playermodel.SAVING_PATH_PLAYERS
PATH_TOURNAMENT = PATH_PLAYER_LIST.parent / "tournament"

@dataclass
class Tournament:
    """Classe Tournois"""
    name : str
    location : str
    player_list : list = field(default_factory=list)
    description : str = "Aucune description"
    date_time_start : str = "Non commencé"
    date_time_end : str = "Non terminé"

    def __str__(self):
        """Retourne la représentation de la valeur 
        sous forme de chaîne de caractères.

        Returns:
            str: Représentation de l'instance en chaîne de caractères.
        """
        name = f"Nom du tournois: {self.name}"
        location = f"Lieu: {self.location}"
        date_time_start = f"Début: {self.date_time_start}"
        date_time_end = f"Fin: {self.date_time_end}"
        description = f"""Description: "{self.description}" """
        if self.player_list:
            players_list = self.player_list
        else:
            players_list = "Pas encore de joueurs"
        players_list = f"Nombre de joueurs: {len(players_list)}"
        all_informations = (
            f"{name}, "
            f"{location}, "
            f"{date_time_start}, "
            f"{date_time_end}, "
            f"{description}, "
            f"{players_list}"
            )
        return all_informations

    @staticmethod
    def create_new_tournament(name: str, location: str):
        new_tournament = Tournament(
            name = name,
            location = location
            )
        return Tournament._save_tournament(new_tournament, new_tournament.__dict__)

    @staticmethod
    def get_list_of_tournament_player():
        """Permet de récupérer la liste des joueurs du tournois.

        Returns:
            list: Liste des joueurs du tournois.
        """
        players_list = []
        with open(PATH_PLAYER_LIST, "r", encoding="utf-8") as file:
            players = json.load(file)
        for player in players:
            if player["tournament_participant"] == True:
                players_list.append(player)
        return players_list

    def start_tournament(self):
        """Démarre le tournois."""
        self.player_list = Tournament.get_list_of_tournament_player()
        self.date_time_start = Timer.format_date_time()

    def end_tournament(self, description):
        """Termine le tournois."""
        self.description = description
        self.date_time_end = Timer.format_date_time()

    def _save_tournament(self, datas):
        date = Timer.get_date()
        file_name = f"Tournois {self.location} - {date}.json"
        complete_path = PATH_TOURNAMENT / file_name
        with open(complete_path, "w", encoding="utf-8") as file:
            json.dump(datas, file,ensure_ascii=False, indent=4)
        return datas
