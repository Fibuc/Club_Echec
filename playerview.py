class PlayerView():

    @staticmethod
    def get_new_player_informations():
        first_name = input("Quel est le prénom du joueur ? : ")
        last_name = input("Quel est le nom de famille du joueur ? : ")
        birth_date = input("Quelle est sa date de naissance ? (JJ/MM/AAAA): ")
        tournament_participant = input(
            "Participera-t-il au prochain tournois"
            " ? (O/N) : "
        )
        all_player_informations = [
            first_name,
            last_name,
            birth_date,
            tournament_participant
        ]
        return all_player_informations
    
    @staticmethod
    def show_new_player_created(first_name: str, last_name: str):
        print(f"Le nouveau joueur \"{first_name} {last_name}\" a été créé.")

    @staticmethod
    def show_player_exist(first_name: str, last_name: str, birth_date: str):
        print(f"Erreur: Le joueur \"{first_name} {last_name} {birth_date}\" existe déjà.")

    @staticmethod
    def show_player_informations(
        first_name: str,
        last_name: str,
        birth_date: str,
        club_name: str,
        current_player: int=1
    ):
        print(f"Joueur {current_player}: {first_name} {last_name} "
              f"- Date de naissance : {birth_date} "
              f"- Club : {club_name}")

    @staticmethod   
    def show_no_player_datas():
        print("Il n'y a aucun joueur dans la base de données.")