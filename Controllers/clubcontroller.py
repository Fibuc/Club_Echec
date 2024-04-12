from Models.clubmodel import ClubModel
from Views.clubview import ClubView

import helpers


class ClubController:
    def __init__(self):
        self.club_view = ClubView()
        self.club_model = ClubModel()

    def club_menu(self):
        launch = True
        while launch:
            self.club_view.show_menu(
                helpers.create_menu,
                self.club_model.menu_name,
                self.club_model.menu_options
            )
            user_choice = self.club_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    self.new_club()
                case "2":
                    self.modify_club_name()
                case "3":
                    launch = False
                case _:
                    self.club_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def new_club(self):
        club_name, national_chest_id = self.club_view.get_club_informations()
        if not self._check_club_name(club_name):
            return
        if self.check_national_chest_id(national_chest_id):
            if self.check_club_exist(national_chest_id):
                self.club_view.show_club_exist(national_chest_id)
            else:
                self.club_model.create_club(club_name, national_chest_id)
                self.club_view.show_created_club(club_name)

        else:
            self.club_view.show_error_national_chest_id(national_chest_id)

        helpers.sleep_a_few_seconds()

    def check_club_exist(self, national_chest_id):
        return any(
            club.national_chest_id == national_chest_id
            for club in self.club_model.all_clubs
        )

    @staticmethod
    def check_national_chest_id(national_chest_id):
        if len(national_chest_id) != 6:
            return False

        if not national_chest_id[:2].isalpha():
            return False

        if not national_chest_id[2:].isdigit():
            return False

        return True

    def modify_club_name(self):
        club = self.select_club()
        if not club:
            return
        club.name = self.club_view.get_new_club_name()
        club.modify_club()
        self.club_view.show_modified_club(club.name)

        helpers.sleep_a_few_seconds()

    def select_club(self, from_player_menu: bool=False) -> ClubModel | None:
        if not self.club_model.all_clubs:
            self.club_view.show_empty_club_list()
            helpers.sleep_a_few_seconds()
            return
        
        options_list = []
        self.club_view.show_border()
        for i, club in enumerate(self.club_model.all_clubs, start=1):
            options_list.append(str(i))
            self.club_view.show_club(
                club_name=club.name, national_chest_id=club.national_chest_id,
                current_club=i
            )
        if from_player_menu:
            user_choice = self.club_view.get_club_player()
        else:
            user_choice = self.club_view.get_club_to_modify()
        if not user_choice:
            return
        if self._check_user_choice(user_choice, options_list):
            return self.club_model.all_clubs[int(user_choice)-1]
        
        return

    def _check_user_choice(self, user_choice, options_list):
        if user_choice in options_list:
            return True
        
        self.club_view.show_error_message_choice(user_choice)
        helpers.sleep_a_few_seconds()
        return False
    
    def _check_club_name(self, club_name):
        if not club_name:
            self.club_view.show_error_empty_name()
            helpers.sleep_a_few_seconds()
            return False
        
        return True