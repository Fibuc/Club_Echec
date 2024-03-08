from Views.clubview import ClubView
from Models.clubmodel import ClubModel
import helpers

class ClubController:
    def __init__(self):
        self.club_view = ClubView()
        self.club_model = ClubModel()

    def create_new_club(self):
        club_informations = self.club_view.get_club_informations()
        self.club_model.name = club_informations[0]
        self.club_model.national_chest_id = club_informations[1]
        result = self.check_national_chest_id()
        if result:
            club_exist = self.check_club_exist()
            if not club_exist:
                self.club_model.save_club_datas()
                self.club_view.show_created_club(self.club_model.name)
                helpers.sleep_a_few_seconds()
            else:
                self.club_view.show_club_exist(self.club_model.national_chest_id)
                helpers.sleep_a_few_seconds()
        else:
            self.club_view.show_error_national_chest_id(self.club_model.national_chest_id)
            helpers.sleep_a_few_seconds()

    def check_club_exist(self):
        all_clubs = self.club_model.get_all_clubs_informations()
        if self.club_model.national_chest_id in all_clubs:
            return True
        else:
            return False

    def check_national_chest_id(self):
        if len(self.club_model.national_chest_id) != 6:
            return False
        
        if not self.club_model.national_chest_id[:2].isalpha():
            return False
        
        if not self.club_model.national_chest_id[2:].isdigit():
            return False
        
        return True
    
    def change_club_name(self):
        self.club_view.show_border()
        all_clubs_informations = self.club_model.get_all_clubs_informations()
        if all_clubs_informations:
            for club in all_clubs_informations:
                club_name = all_clubs_informations[club]
                national_chest_id = club
                self.club_view.show_club_informations(club_name, national_chest_id)

            old_name = all_clubs_informations[national_chest_id]
            self.club_model.national_chest_id = self.club_view.get_club_id_to_modify()
            if self.club_model.national_chest_id in all_clubs_informations:
                self.club_model.name = self.club_view.get_club_name_to_modify()
                self.club_model.save_club_datas()
                self.club_view.show_modified_club(old_name, self.club_model.name)
                helpers.sleep_a_few_seconds()
            else:
                self.club_view.show_national_chest_id_not_exist(self.club_model.national_chest_id)
                helpers.sleep_a_few_seconds()
        else:
            self.club_view.show_void_club_list()
            helpers.sleep_a_few_seconds()