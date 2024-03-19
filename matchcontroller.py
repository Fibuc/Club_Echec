from pprint import pprint
from random import randint

from matchmodel import MatchModel
from matchview import MatchView

class MatchController():
    def __init__(self):
        self.match_model = MatchModel()
        self.match_view = MatchView()


    def create_match(self):
        self.all_players = self.match_model.get_all_player()
        pass


    def create_new_matchs(self): # Tuple (["Nom_joueur_1", "score"], ["Nom_joueur_2", "score"],)
        # Liste des matchs = [([Joueur_1], [Joueur_2])]
        """Créée une nouvelle liste de matchs et les enregistre.

        Returns:
            fonction: Sauvegarde la nouvelle liste de match.
        """
        all_match_list = []
        player_list = self.match_model.get_all_player()
        for _ in player_list:
            first_player = player_list.pop(randint(1, len(player_list)-1))
            second_player = player_list.pop(randint(1, len(player_list)-2))
            match_pair = (
                tuple(first_player.values()),
                tuple(second_player.values())
                )
            all_match_list.append(tuple(match_pair))
        pprint(all_match_list)


if __name__ == "__main__":
    match = MatchController()
    match.create_new_matchs()