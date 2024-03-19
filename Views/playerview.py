import helpers

class PlayerView():
    
    INFORMATIONS_TYPE = {
        "Le prénom": helpers.KEY_FIRST_NAME_PLAYER,
        "Le nom de famille": helpers.KEY_LAST_NAME_PLAYER,
        "La date de naissance": helpers.KEY_BIRTH_DATE_PLAYER,
        "Le club": helpers.KEY_CLUB_NAME_PLAYER,
        "La participation": helpers.KEY_TOURNAMENT_PARTICIPANT_PLAYER
    }


    @staticmethod
    def get_new_player_informations():
        first_name = input("Quel est le prénom du joueur ? : ")
        last_name = input("Quel est le nom de famille du joueur ? : ")
        birth_date = input("Quelle est sa date de naissance ? (JJ/MM/AAAA): ")
        club_name = input("Quel est le club du participant ? : ")
        tournament_participant = input(
            "Participera-t-il au prochain tournois"
            " ? (O/N) : "
        )
        all_player_informations = [
            first_name,
            last_name,
            birth_date,
            club_name,
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
    def show_players_informations(
        first_name: str,
        last_name: str,
        birth_date: str,
        club_name: str,
        participation: bool,
        current_player: int=1,
    ):
        print(f"Joueur {current_player}: {first_name} {last_name} "
              f"- Date de naissance : {birth_date} "
              f"- Club : {club_name} "
              f"Participant : {participation}"
        )

    @staticmethod   
    def show_no_player_datas():
        print("Il n'y a aucun joueur dans la base de données.")

    def get_first_name(self):
        return input("Quel est le prénom du joueur ? : ")
    
    @staticmethod
    def no_match_player_found(prenom):
        print(f"Il n'y a aucun joueur ayant pour prénom \"{prenom}\" dans la base de données.")

    def get_player_to_modify(self):
        self.show_border()
        return input("Quel est le numéro du joueur à modifier ? : ")
    
    def show_informations_type(self):
        self.show_border()
        print("Liste des informations")
        self.show_border()
        current_information = 1
        for information in self.INFORMATIONS_TYPE:
            print(f"{current_information} - {information}")
            current_information += 1
    
    def show_title_players(self):
        self.show_border()
        print("Liste des joueurs")
        self.show_border()

    def get_information_to_modify(self):
        self.show_border()
        return input("Quel est l'information du joueur à modifier ? : ")
    
    def get_new_value(self):
        return input(f"Quelle est la nouvelle valeur ? : ")
    
    def show_success_message(self):
        self.show_border()
        print("Validé! Le joueur à bien été modifié.")
    
    @staticmethod
    def show_error_message(user_choice: str):
        print(f"Erreur: La commande \"{user_choice}\" n'est pas valide.")

    @staticmethod
    def show_border():
        print(helpers.BORDER)

    @staticmethod
    def show_space():
        print(helpers.SPACE)

