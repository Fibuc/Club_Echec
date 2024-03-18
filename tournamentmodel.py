import json

import helpers

PATH_PLAYER_LIST = helpers.SAVING_PATH_PLAYERS

class TournamentModel:
    """Classe Tournois"""
    def __init__(
            self,
            name: str="",
            location: str="",
            player_list: list=[],
            date_time_start: str="Non commencé",
            date_time_end : str="Non terminé",
            description : str="Aucune description"
    ):
        self.name = name
        self.location = location
        self.player_list = player_list
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.description = description


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
    def get_list_of_tournament_player():
        """Permet de récupérer la liste des joueurs du tournois.

        Returns:
            list: Liste des joueurs du tournois.
        """
        players_list = []
        with open(PATH_PLAYER_LIST, "r", encoding="utf-8") as file:
            players = json.load(file)
        for player in players:
            if player["tournament_participant"]:
                players_list.append(player)
        return players_list

    def start_tournament(self):
        """Démarre le tournois."""
        self.player_list = self.get_list_of_tournament_player()
        self.date_time_start = helpers.format_date_time()

    def end_tournament(self, description):
        """Termine le tournois."""
        self.description = description
        self.date_time_end = helpers.format_date_time()

    def save_not_ended_tournament(self, name:str, location:str):
        datas = {"name" : name, "location" : location}
        helpers.TOURNAMENT_DIR.mkdir(exist_ok=True, parents=True)
        date = helpers.get_date()
        file_name = f"NT_Tournois {self.location} - {date}.json"
        complete_path = helpers.TOURNAMENT_DIR / file_name
        with open(complete_path, "w", encoding="utf-8") as file:
            json.dump(datas, file,ensure_ascii=False, indent=4)
