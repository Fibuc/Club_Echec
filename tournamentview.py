import helpers

class TournamentView:
    def get_tournament_informations(self):
        name = input("Quel est le nom du tournois ? : ")
        location = input("Quel est le lieu du tournois ? : ")
        return [name, location]
    
    def show_tournament_created(self, name):
        print(f"Le tournois \"{name}\" a bien été créé")

    def show_menu_tournament(self):
        print(f"""
{helpers.BORDER}
          Création tournois
{helpers.BORDER}
1 - Valider et lancer le tournois
2 - Ajouter des participants
3 - Afficher les participants
4 <-- Enregistrer le tournois et quitter
{helpers.BORDER}
"""
)
        
    def get_user_choice(self):
        return input("Quel est votre choix ? : ")