class MatchModel:
    
    def create_match(self, player_1_name, player_2_name, player_1_points, player_2_points):
        match = (
            [player_1_name, player_1_points],
            [player_2_name, player_2_points]
        )
        return tuple(match)
    
