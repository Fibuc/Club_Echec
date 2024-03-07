import helpers

class ClubView():

    @staticmethod
    def show_border():
        print(helpers.BORDER)
    
    @staticmethod
    def back_to_line():
        print(helpers.BACK_TO_LINE)

    def get_club_informations(self) -> list:
        self.show_border()
        club_name = input("Quel est le nom du club ? : ")
        national_chest_id = input("Quel est sont identifiant national ? : ")
        informations_club_list = [club_name, national_chest_id]
        return informations_club_list
    
    @staticmethod
    def show_created_club(club_name: str):
        print(f"Le club \"{club_name}\" a bien été créé.")


    @staticmethod
    def show_error_national_chest_id(national_chest_id: str):
        print(f"Le numéro d'identifiant national \"{national_chest_id}\" n'est pas correct.")

    @staticmethod
    def show_national_chest_id_not_exist(national_chest_id: str):
        print(f"Le numéro d'identifiant national \"{national_chest_id}\" n'existe pas dans la base.")

    @staticmethod
    def show_club_informations(club_name: str, national_chest_id: str):
        print(f"ID : {national_chest_id} - Nom du club : {club_name}")

    @staticmethod
    def show_void_club_list():
        print("La liste des clubs est vide.")


    def get_club_id_to_modify(self):
        self.show_border()
        return input("Quel est l'ID du club à modifier ? : ")

    def get_club_name_to_modify(self):
        self.show_border()
        return input("Quel est son nouveau nom ? : ")
    
    @staticmethod
    def show_modified_club(old_name: str, new_name: str):
        print(f"Le club \"{old_name}\" a bien été changé en \"{new_name}\".")

    @staticmethod
    def show_club_exist(national_chest_id):
        print(f"Création impossible: Un club ayant pour identifiant \"{national_chest_id}\" existe déjà dans la base de données.")

