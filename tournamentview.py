import helpers

class TournamentView:
    def get_tournament_informations(self):
        name = input("Quel est le nom du tournois ? : ")
        location = input("Quel est le lieu du tournois ? : ")
        return [name, location]
    
    def show_tournament_created(self, name):
        print(f"Le tournois \"{name}\" a bien été créé")
        
    def get_user_choice(self):
        return input("Quel est votre choix ? : ")
    