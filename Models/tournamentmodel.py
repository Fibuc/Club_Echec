from pathlib import Path
from random import randint
from tinydb import TinyDB, Query

from Models.playermodel import PlayerModel

import helpers
import menus 

TOURNAMENT_DIR = menus.TOURNAMENT_DIR

INDEX_PLAYER_NAME = 0
INDEX_PLAYER_POINT = 1

NOT_ENDED_TOURNAMENT_PREFIX = "Incomplete_"

import json
from typing import ClassVar


class TournamentModel:
    """Classe Tournois"""
    menu_name: ClassVar[str]=menus.TOURNAMENT_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list]=menus.TOURNAMENT_MENU[menus.OPTIONS_MENU]
    all_tournaments: ClassVar[list]=[]
    unfinished_tournament: ClassVar[list]=[]
    tournament_path: ClassVar[TinyDB]

    def __init__(
            self,
            name: str="",
            location: str="",
            participants: list=[],
            rounds_list: list=[],
            date_time_start: str="Non commencé",
            date_time_end : str="Non terminé",
            description : str="Aucune description",
    ):
        self.name = name
        self.location = location
        self.participants = participants
        self.rounds_list = rounds_list
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.description = description

    def __repr__(self) -> str:
        """Retourne la représentation de l'objet sous forme de chaîne de
        caractères de l'objet TournamentModel.

        Returns:
            str: Chaîne de caractère de la représentation de l'objet.
        """
        return (
            f"TournamentModel(name='{self.name}', "
            f"location='{self.location}', players_list='{self.participants}', "
            f"rounds_list='{self.rounds_list}', "
            f"date_time_start={self.date_time_start}, "
            f"date_time_end={self.date_time_end}, "
            f"description={self.description})"
        )

    def __str__(self):
        """Retourne l'objet TournamentModel sous forme de chaîne de 
        caractères.

        Returns:
            str: Représentation de l'instance en chaîne de caractères.
        """
        if self.participants:
            players = len(self.participants)
            plural_player = f"{"s" if players > 1 else ""}"
        else:
            players = 0
            plural_player = "s"
        if self.rounds_list:
            rounds = len(self.rounds_list)
            plural_round = f"{"s" if rounds > 1 else ""}"
        else:
            rounds = 0
            plural_round = "s"

        return (
            f"Nom: {self.name} \tLieu: {self.location} \t"
            f"Nombre de participant{plural_player}: {players}\t"
            f"Nombre de round{plural_round}: {rounds}\t"
            f"Date début: {self.date_time_start} \tDate fin: "
            f"{self.date_time_end} \t Description: {self.description}"
        )

    def create_new_tournament(
            self,
            name: str,
            location: str,
            players_list: list=[],
            rounds_list: list=[],
            date_time_start: str="Non commencé",
            date_time_end : str="Non terminé",
            description : str="Aucune description"
        ):
        """Créée une instance de la classe TournamentModel, l'ajoute à la liste
        des instances de la classe TournamentModel et sauvegarde cette nouvelle
        liste.

        Args:
            name (str): Nom du tournoi.
            location (str): Lieu du tournoi.
            players_list (list): Liste des joueurs participants.
            rounds_list (list): Liste des rounds du tournois.
            date_time_start (str): Date du début du tournois.
            date_time_end (str): Date de la fin du tournois.
            description (str): Description du tournois.
        """
        tournament = TournamentModel(
            name=name,
            location=location,
            participants=players_list,
            rounds_list=rounds_list,
            date_time_start=date_time_start,
            date_time_end=date_time_end,
            description=description
        )
        TournamentModel.all_tournaments.append(tournament)
        tournament.save_tournament()

    def save_tournament(self, ended_tournament: bool=False):
        """Enregistre dans le fichier de sauvegarde toutes les instances de
        PlayerTournament présents dans la variable 
        PlayerTournament.all_tournaments.

        Args:
            ended_tournament (bool, optional): Indique si le tournois est
            terminé. Defaults to False.
        """
        date = helpers.get_date()
        prefix = NOT_ENDED_TOURNAMENT_PREFIX
        if ended_tournament:
            prefix = ""

        file_name = f"{prefix}Tournament {self.location} - {date}.json"
        full_path = TOURNAMENT_DIR / file_name
        TournamentModel.tournament_path = TinyDB(full_path)
        db = TournamentModel.tournament_path
        tournament_db = db.table("Tournament")
        self.participants = [player.__dict__ for player in self.participants]
        tournament_db.insert(self.__dict__)



    @staticmethod
    def load_all_tournaments():
        for tournament_file in menus.TOURNAMENT_DIR.glob("*"):
            with open(tournament_file, "r",encoding="UTF-8") as file:
                tournament = TournamentModel(**json.load(file))
                TournamentModel.all_tournaments.append(tournament)

    def load_unfinished_tournament(self):
        unfinished_tournaments = []
        for tournament in menus.TOURNAMENT_DIR.glob("*"):
            if tournament.name.startswith(NOT_ENDED_TOURNAMENT_PREFIX):
                with open(tournament, "r",encoding="UTF-8") as file:
                    unfinished_tournaments.append(json.load(file))
        return unfinished_tournaments


if __name__ == '__main__':
    tournament_model = TournamentModel()


    player_model = PlayerModel()
    player_1 = player_model.create_player("Jean", "Lucas", "03/04/1997", "Mélodie")
    player_2 = player_model.create_player("Jérémy", "Louis", "08/08/1998", "Mélodie")
    player_3 = player_model.create_player("Christophe", "Morrain", "02/12/1968", "Mélodie")
    all_players = [player_1.__dict__, player_2.__dict__, player_3.__dict__]

    tournament = tournament_model.create_new_tournament("Médium", "Nantes", all_players)




