from typing import ClassVar
import json

import helpers

DEFAULT_NUMBER_OF_POINT = 0

class PlayerModel:
    """Classe joueur"""
    number_of_player: ClassVar[int] = 0

    def __init__(
        self,
        first_name: str="",
        last_name: str="",
        club_name: str="",
        birth_date: str="",
        number_of_points: int=DEFAULT_NUMBER_OF_POINT,
        tournament_participant: bool=False
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.club_name = club_name
        self.birth_date = birth_date
        self.number_of_points = number_of_points
        self.tournament_participant = tournament_participant

    def __post_init__(self):
        """Incrémente le nombre de joueur total créé"""
        PlayerModel.number_of_player += 1

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
    
    def list_all_players_in_order(self):
        """Affiche la liste de tous les joueurs triés dans l'ordre alphabétique.

        Returns:
            list: Liste triée de tous les joueurs.
        """
        all_players_list = self.list_all_players_informations()
        if all_players_list:
            sorted_list = sorted(all_players_list)
            return sorted_list
        else:
            return None

    def save_new_player(self):
        """Sauvegardes les données du joueur dans le fichier json

        Args:
            new_player_datas (dict): Dictionnaire comportant les informations
            du joueur

        Returns:
            list: Retourne la liste comprenant tous les joueurs.
        """
        datas = []
        dict_informations_new_player = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "club_name": self.club_name,
            "birth_date": self.birth_date,
            "number_of_points": self.number_of_points,
            "tournament_participant": self.tournament_participant
        }
        helpers.DATA_DIR.mkdir(parents=True, exist_ok=True)
        if helpers.SAVING_PATH_PLAYERS.exists():
            with open(helpers.SAVING_PATH_PLAYERS, "r", encoding="utf-8") as file:     # Faire fonction récupérer données et associer les deux ====
                datas = json.load(file)
        with open(helpers.SAVING_PATH_PLAYERS, "w", encoding="utf-8") as file:
            datas.append(dict_informations_new_player)
            json.dump(datas, file, ensure_ascii=False, indent=4)


    def add_to_tournament(self):
        self.tournament_participant = True

    def list_all_players_informations(self):
        """Affiche la liste de tous les joueurs triés dans l'ordre alphabétique.

        Returns:
            list: Liste triée de tous les joueurs.
        """
        all_players_list = []
        try:
            with open(helpers.SAVING_PATH_PLAYERS, "r", encoding="utf-8") as file:
                all_players = json.load(file)
            for player in all_players:
                self.first_name = player["first_name"]
                self.last_name = player["last_name"]
                self.birth_date = player["birth_date"]
                self.club_name = player["club_name"]
                self.tournament_participant = player["tournament_participant"]
                all_informations = [
                    self.first_name,
                    self.last_name,
                    self.birth_date,
                    self.club_name,
                    self.tournament_participant
                ]
                all_players_list.append(all_informations)
                
            return all_players_list
        
        except FileNotFoundError:
            return None