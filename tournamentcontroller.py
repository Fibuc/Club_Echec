from Controllers.playercontroller import PlayerController
from tournamentview import TournamentView
from tournamentmodel import TournamentModel

import helpers

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

    def add_participants(self):
        pass

        

        

    








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
