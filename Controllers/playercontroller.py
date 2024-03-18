from Models.playermodel import PlayerModel
from Views.playerview import PlayerView
import helpers

class PlayerController():
    def __init__(self):
        self.player_view = PlayerView()
        self.player_model = PlayerModel()
        
    def create_new_player(self):
        player_informations = self.player_view.get_new_player_informations()
        self.player_model.first_name = player_informations[0]
        self.player_model.last_name = player_informations[1]
        self.player_model.birth_date = player_informations[2]
        self.player_model.club_name = player_informations[3]
        if player_informations[4] in ("O", "o"):
            self.player_model.tournament_participant = True
        else:
            self.player_model.tournament_participant = False

        result = self.check_player_exist()
        if not result:
            self.player_model.save_new_player()
            self.player_view.show_new_player_created(
                self.player_model.first_name,
                self.player_model.last_name
            )
            helpers.sleep_a_few_seconds()
        else:
            self.player_view.show_player_exist(
                self.player_model.first_name,
                self.player_model.last_name,
                self.player_model.birth_date
            )
            helpers.sleep_a_few_seconds()

    def check_player_exist(self):
        all_players_list = self.player_model.list_all_players_informations()
        self.all_player_datas = (
            self.player_model.first_name,
            self.player_model.last_name,
            self.player_model.birth_date
        )
        if all_players_list:
            if self.all_player_datas in all_players_list:
                return True
            return False
        else:
            return False

    def show_players_list_in_order(self):
        all_player_list = self.player_model.list_all_players_in_order()
        if all_player_list:
            self.show_players(all_player_list)
        else:
            self.player_view.show_no_player_datas()
    
    def get_participating_players_list(self):
        all_players_list = self.player_model.list_all_players_in_order()
        participants_list = []
        if all_players_list:
            participants_list = [player for player in all_players_list if player[4]]

        return participants_list
    
    def show_players(self, players_list):
        current_player = 1
        for player in players_list:
            player_first_name = player[0]
            player_last_name = player[1]
            player_birth_date = player[2]
            player_club = player[3]
            self.player_view.show_players_informations(
                player_first_name,
                player_last_name,
                player_birth_date,
                player_club,
                current_player
            )
            current_player += 1



    def modify_a_player(self):
        all_players = self.player_model.list_all_players_informations()
        first_name_search = self.player_view.get_first_name()
        player_match = []
        if all_players:
            for player in all_players:
                if first_name_search in player:
                    player_match.append(player)

            for player in player_match:
                first_name = player[0]
                last_name = player[1]
                birth_date = player[2]
                club_name = player[3]
                self.player_view.show_players_informations(
                    first_name,
                    last_name,
                    birth_date,
                    club_name
                )
            
            

        if not player_match:
            self.player_view.no_match_player_found(first_name_search)

        helpers.sleep_a_few_seconds()

    # def create_options_list(self):
    #     number_of_option = 1
    #     all_choices = []
    #     for option in option_list:
    #         all_choices.append(f"{number_of_option} - {option}")
    #         number_of_option += 1
    #     if name_menu != helpers.MAIN_MENU_NAME:
    #         all_choices.append(
    #             f"{number_of_option} <-- Revenir au menu précédent")
        
    #     all_choices_menu = "\n".join(all_choices)
    #     return all_choices_menu