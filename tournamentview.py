class TournamentView:
    def get_tournament_informations(self):
        name = input("Quel est le nom du tournois ? : ")
        location = input("Quel est le lieu du tournois ? : ")
        return [name, location]