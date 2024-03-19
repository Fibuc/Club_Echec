from playermodel import PlayerModel
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
            self.player_model.add_new_player()
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

    def show_players_in_order(self):
        all_player_list = self.player_model.all_players_in_order()
        if all_player_list:
            self.show_players(all_player_list)
        else:
            self.player_view.show_no_player_datas()
    
    def get_participating_players_list(self):
        all_players_list = self.player_model.all_players_in_order()
        participants_list = []
        if all_players_list:
            participants_list = [
                player
                for player in all_players_list
                if player[helpers.KEY_TOURNAMENT_PARTICIPANT_PLAYER]
            ]

        return participants_list
    
    def show_players(self, players: dict, show_participation: bool=False):
        current_player = 1
        for player in players:
            player_first_name = player[helpers.KEY_FIRST_NAME_PLAYER]
            player_last_name = player[helpers.KEY_LAST_NAME_PLAYER]
            player_birth_date = player[helpers.KEY_BIRTH_DATE_PLAYER]
            player_club = player[helpers.KEY_CLUB_NAME_PLAYER]
            player_participation = player[helpers.KEY_TOURNAMENT_PARTICIPANT_PLAYER]             
            self.player_view.show_players_informations(
                player_first_name,
                player_last_name,
                player_birth_date,
                player_club,
                player_participation,
                current_player
            )
            current_player += 1


    def check_user_choice(self, information_to_control, options):
        try:
            index_to_modify = int(information_to_control) - 1
            if index_to_modify in [i for i in range(len(options))]:
                return index_to_modify
            else:
                self.player_view.show_error_message(information_to_control)
                helpers.sleep_a_few_seconds()
                return False

        except ValueError:
            self.player_view.show_error_message(information_to_control)
            helpers.sleep_a_few_seconds()
            return False


    def modify_a_player(self):
        all_players = self.player_model.charge_players()
        first_name_search = self.player_view.get_first_name().capitalize()
        player_match = [
            player
            for player in all_players
            if first_name_search in player[helpers.KEY_FIRST_NAME_PLAYER]
        ]
        if not player_match:
            self.player_view.no_match_player_found(first_name_search)
            return
        
        self.player_view.show_title_players()
        self.show_players(player_match)
        player_user_choice = self.player_view.get_player_to_modify()
        index_player_to_modify = self.check_user_choice(player_user_choice, player_match)
        if index_player_to_modify != bool:
            player_to_modify = player_match[index_player_to_modify]
            all_informations_type = list(self.player_view.INFORMATIONS_TYPE.keys())
            information_user_choice = self.player_view.get_information_to_modify()
            index_information_to_modify = self.check_user_choice(
                information_user_choice,
                all_informations_type
            )
            if index_information_to_modify:
                informations_to_modify = 0
                new_value = self.player_view.get_new_value()
                player_to_modify[key_to_modify] = new_value
                self.player_model.save_players(all_players)
                self.player_view.show_success_message()