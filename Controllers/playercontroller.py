# Imports modèle et vue du player.
from Models.playermodel import PlayerModel
from Views.playerview import PlayerView, EDITABLE_INFORMATIONS_PLAYER

# Import des utilitaires.
import helpers



class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()
        self.player_model = PlayerModel()

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
        full_name = self.player_view.get_new_player_name()
        birth_date = self.player_view.get_new_player_birth_date()
        club_name = self.player_view.get_new_player_club_name()
        player = self.player_model.create_player(
            first_name=full_name[0],
            last_name=full_name[1],
            birth_date=birth_date,
            club_name=club_name
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
        index_player_to_modify = self.check_user_choice(
            player_user_choice,
            matching_players
        )
        if index_player_to_modify != bool:
            player = matching_players[index_player_to_modify]
            self.player_view.show_informations_type()
            information_user_choice = self.player_view.get_information_to_modify()
            index_information_to_modify = self.check_user_choice(
                information_user_choice,
                EDITABLE_INFORMATIONS_PLAYER
            )
            if index_information_to_modify != bool:
                new_value = self.player_view.get_new_value()
                match index_information_to_modify:
                    case 0:
                        player.modify_player(first_name=new_value)
                        player.first_name = new_value
                    case 1:
                        player.modify_player(last_name=new_value)
                        player.last_name = new_value
                    case 2:
                        player.modify_player(birth_date=new_value)
                        player.birth_date = new_value
                    case 3:
                        player.modify_player(club_name=new_value)
                        player.club_name = new_value

                self.player_view.show_valid_modifications()
                helpers.sleep_a_few_seconds()

    def charge_all_players(self):
        self.player_model.load_players()
        self.player_model.sort_players()

    def check_user_choice(self, user_choice: str, list_to_control: list):
        list_lenght = [i for i in range(len(list_to_control))]
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
    


