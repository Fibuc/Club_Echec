# Imports modèle et vue du player.
from datetime import datetime
from Models.playermodel import PlayerModel
from Views.playerview import PlayerView, EDITABLE_INFORMATIONS_PLAYER
from Controllers.clubcontroller import ClubController

import string

# Import des utilitaires.
import helpers

class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()
        self.player_model = PlayerModel()
        self.club = ClubController()

    def player_menu(self):
        launch = True
        while launch:
            self.player_view.show_menu(
                helpers.create_menu,
                self.player_model.menu_name,
                self.player_model.menu_options,
            )
            user_choice = self.player_view.get_menu_user_choice()
            match user_choice:
                case "1":
                    self.new_player()
                case "2":
                    self.modify_a_player()
                case "3":
                    launch = False
                case _:
                    self.player_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def new_player(self):
        first_name, last_name = self.player_view.get_new_player_name()
        if not self._check_names(first_name, last_name):
            return
        birth_date = self.player_view.get_new_player_birth_date()
        if not self._check_birth_date(birth_date):
            return
        club = self.club.select_club(from_player_menu=True)
        if not club:
            return
        participation = self.player_view.get_new_player_participation()
        participation = participation in ["o", "O"]
        player = self.player_model.create_player(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            club_name=club.name,
            participation=participation
        )
        self.player_view.show_new_player_created(player.full_name)
        self.player_model.all_players.append(player)
        helpers.sleep_a_few_seconds()

    
    def modify_a_player(self):
        first_name_search = self.player_view.get_first_name().capitalize()
        matching_players = [
            player
            for player in self.player_model.all_players
            if first_name_search in player.first_name
        ]
        if not matching_players:
            self.player_view.show_no_match_player_found(first_name_search)
            return

        self.player_view.show_title_players()
        self.player_view.show_players(matching_players, numbering=True)
        player_user_choice = self.player_view.get_index_player_to_modify()
        if not player_user_choice:
            return
        
        index_player_to_modify = self.check_user_choice(
            player_user_choice,
            matching_players
        )
        if not isinstance(index_player_to_modify, bool):
            player = matching_players[index_player_to_modify]
            self.player_view.show_informations_type()
            information_user_choice = self.player_view.get_information_to_modify()
            index_information_to_modify = self.check_user_choice(
                information_user_choice,
                EDITABLE_INFORMATIONS_PLAYER
            )
            if not isinstance(index_information_to_modify, bool):
                match index_information_to_modify:
                    case 0:
                        new_value = self.player_view.get_new_value()
                        if not self._check_a_name(new_value):
                            return
                        
                        new_value = new_value.capitalize()
                        player.modify_player(first_name=new_value)
                        player.first_name = new_value
                    case 1:
                        new_value = self.player_view.get_new_value()
                        if not self._check_a_name(new_value):
                            return
                        
                        new_value = new_value.capitalize()
                        player.modify_player(last_name=new_value)
                        player.last_name = new_value
                    case 2:
                        new_value = self.player_view.get_new_value()
                        if not self._check_birth_date(new_value):
                            return
                        
                        player.modify_player(birth_date=new_value)
                        player.birth_date = new_value
                    case 3:
                        club = self.club.select_club(from_player_menu=True)
                        if not club:
                            return
                        player.modify_player(club_name=club.name)
                        player.club_name = club.name

                self.player_view.show_valid_modifications()
                helpers.sleep_a_few_seconds()

    def charge_all_players(self):
        self.player_model.load_players()
        self.player_model.sort_players()

    def check_user_choice(self, user_choice: str, list_to_control: list):
        list_lenght = list(range(len(list_to_control)))
        try:
            index = int(user_choice) - 1
            if index in list_lenght:
                return index
            else:
                self.player_view.show_error_message_choice(user_choice)
                helpers.sleep_a_few_seconds()
                return False

        except ValueError:
            self.player_view.show_error_message_choice(user_choice)
            helpers.sleep_a_few_seconds()
            return False
        
    def _check_names(self, first_name: str, last_name: str):
        special_characteres = string.punctuation + string.digits
        names_to_check = first_name + last_name
        if any(charactere in special_characteres for charactere in names_to_check):
            self.show_error_characteres()
            return False
        
        elif not (first_name and last_name):
            self.show_empty_names()
            return False
        
        return True

    def _check_a_name(self, name: str):
        special_characteres = string.punctuation + string.digits
        if any(charactere in special_characteres for charactere in name):
            self.show_error_characteres()
            return False
        
        elif not name:
            self.show_empty_names()
            return False
        
        return True

    def _check_birth_date(self, birth_date):
        try:
            birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
            return True
        except ValueError:
            self.player_view.show_error_date(birth_date)
            helpers.sleep_a_few_seconds()
            return False
    
    def show_empty_names(self):
        self.player_view.show_error_empty_names()
        helpers.sleep_a_few_seconds()

    def show_error_characteres(self):
        self.player_view.show_error_characteres_names()
        helpers.sleep_a_few_seconds()