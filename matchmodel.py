import helpers
import json

class MatchModel():
    def __init__(self):
        self.winner_point = 1
        self.loser_point = 0
        self.nul = 0,5

    
    def get_all_player(self):
        with open(helpers.SAVING_PATH_PLAYERS, encoding='UTF-8') as file:
            return json.load(file)
        
    def create_a_match(self):
        pass