from Controllers.playercontroller import PlayerController
from tournamentview import TournamentView
from tournamentmodel import TournamentModel

import helpers

START_TOURNAMENT_MENU = {
    helpers.NAME_MENU : "DEBUT TOURNOIS",
    helpers.OPTIONS_MENU : [
        "Lancer le tour et générer des matchs",
        "Enregistrer et quitter",
        ]
}

class TournamentController:
    def __init__(self):
        self.tournament_view = TournamentView()
        self.tournament_model = TournamentModel()
        self.player = PlayerController()

    def create_new_tournament(self):
        all_informations = self.tournament_view.get_tournament_informations()
        self.tournament_model.name = all_informations[0]
        self.tournament_model.location = all_informations[1]
        self.tournament_model.player_list = self.player.get_participating_players_list()
        self.tournament_model.save_tournament()
        self.tournament_view.show_tournament_created(
            self.tournament_model.name
        )
        helpers.sleep_a_few_seconds()

    def show_participants(self):
        current_player = 1
        for player in self.tournament_model.player_list:
            self.player.player_view.show_players_informations(
                player[helpers.KEY_FIRST_NAME_PLAYER],
                player[helpers.KEY_LAST_NAME_PLAYER],
                player[helpers.KEY_BIRTH_DATE_PLAYER],
                player[helpers.KEY_CLUB_NAME_PLAYER],
                player[helpers.KEY_TOURNAMENT_PARTICIPANT_PLAYER],
                current_player=current_player
            )
            current_player += 1

    def add_participants(self):
        first_name_search = self.player.player_view.get_first_name()

    def resume_tournament(self):
        pass

    def start_tournament(self):
        
        





"""


Nom du tournois ?
Lieu du tournois?
///Enregistrement du tournois : startwith "NS_"
///Afficher le nombre de joueurs
1 - Démarrer le tournois
2 - Ajouter des participants
3 - Enregistrer et revenir au menu

Démarrage du tournois.
"""
