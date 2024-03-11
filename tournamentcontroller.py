from tournamentview import TournamentView
from tournamentmodel import TournamentModel

class TournamentController:
    def __init__(self):
        self.tournament_view = TournamentView()
        self.tournament_model = TournamentModel()

    def create_new_tournament(self):
        all_informations = self.tournament_view.get_tournament_informations()
        








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
