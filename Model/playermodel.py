from dataclasses import dataclass
from pprint import pprint
from typing import ClassVar
from pathlib import Path
from faker import Faker
import json

DEFAULT_NUMBER_OF_POINT = 0
DIR_PATH = Path(__file__).parent.parent
SAVING_PATH_PLAYERS = DIR_PATH / "data" / "players.json"

@dataclass
class Player:
    """Classe joueur"""
    number_of_player : ClassVar[int] = 0
    first_name : str
    last_name : str
    club_name : str
    birth_date : str
    number_of_points : int = DEFAULT_NUMBER_OF_POINT
    tournament_participant : bool = False

    def __post_init__(self):
        """Incrémente le nombre de joueur total créé
        """
        Player.number_of_player += 1

    def __str__(self):
        """Retourne la représentation de la valeur 
        sous forme de chaîne de caractères.

        Returns:
            str: Représentation de l'instance en chaîne de caractères.
        """
        name = f"Nom : {self.first_name} {self.last_name}"
        birth_date = f"Date de naissance: {self.birth_date}"
        club = f"Club: {self.club_name}"
        return f"{name}, {birth_date}, {club}"

    @staticmethod
    def create_new_player(
        first_name: str,
        last_name: str,
        birth_date: str,
        tournament_participant: bool,
        club_name: str
    ):
        """Créé un nouveau joueur l'enregistre.

        Args:
            first_name (str): Prénom du joueur
            last_name (str): Nom de famille du joueur
            birth_date (str): Date de naissance du joueur
            tournament_participant (bool): Participation au tournois
            club_name (str): Nom du club du joueur

        Returns:
            fonction: Enregistrement du joueur dans fichier json.
        """
        new_player_datas = Player(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            tournament_participant=tournament_participant,
            club_name=club_name
        )
        return Player._save_new_player(new_player_datas.__dict__)
    
    @staticmethod
    def list_all_player_in_order():
        """Affiche la liste de tous les joueurs triés dans l'ordre alphabétique.

        Returns:
            list: Liste triée de tous les joueurs.
        """
        all_players_list = []
        with open(SAVING_PATH_PLAYERS, "r", encoding="utf-8") as file:  # Faire fonction récupérer données et associer les deux ====
            all_players = json.load(file)
        for player in all_players:
            first_name = player["first_name"]
            last_name = player["last_name"]
            birth_date = player["birth_date"]
            club = player["club_name"]
            all_informations = first_name, last_name, birth_date, club
            all_players_list.append(all_informations)
        sorted_list = sorted(all_players_list)
        return sorted_list


    @staticmethod
    def _save_new_player(new_player_datas):
        """Sauvegardes les données du joueur dans le fichier json

        Args:
            new_player_datas (dict): Dictionnaire comportant les informations
            du joueur

        Returns:
            list: Retourne la liste comprenant tous les joueurs.
        """
        with open(SAVING_PATH_PLAYERS, "r", encoding="utf-8") as file:     # Faire fonction récupérer données et associer les deux ====
            datas = json.load(file)
        with open(SAVING_PATH_PLAYERS, "w", encoding="utf-8") as file:
            datas.append(new_player_datas)
            json.dump(datas, file, ensure_ascii=False, indent=4)
        return datas
    
    def add_to_tournament(self):
        self.tournament_participant = True