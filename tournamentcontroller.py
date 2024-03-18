from tournamentview import TournamentView
from tournamentmodel import TournamentModel
import helpers

class TournamentController:
    def __init__(self):
        self.tournament_view = TournamentView()
        self.tournament_model = TournamentModel()

    def create_new_tournament(self):
        all_informations = self.tournament_view.get_tournament_informations()
        self.tournament_model.name = all_informations[0]
        self.tournament_model.location = all_informations[1]
        self.tournament_model.save_not_ended_tournament(
            self.tournament_model.name,
            self.tournament_model.location
        )
        self.tournament_view.show_tournament_created(
            self.tournament_model.name
        )
        helpers.sleep_a_few_seconds()
        self.tournament_menu()
        

    def tournament_menu(self):
        launch = True
        while launch:
            self.tournament_view.show_menu_tournament()
            self.user_choice = self.tournament_view.get_user_choice()
            match self.user_choice:
                case "1":
                    print("Lancer le tournois")
                case "2":
                    print("Ajouter des participants")
                case "3":
                    print("Afficher les participants")
                case "4":
                    print("Enregistrer le tournois et quitter")
                case _:
                    print("Non autorisé.")
        

    








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
