# Imports modèle et vue du player.
from Models.playermodel import PlayerModel
from Views.playerview import PlayerView

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
                    print(2)
                case "3":
                    launch = False
                case _:
                    self.player_view.show_error_message_choice(user_choice)
                    helpers.sleep_a_few_seconds()

    def new_player(self):
        full_name = self.player_view.get_new_player_name()
        birth_date = self.player_view.get_new_player_birth_date()
        club_name = self.player_view.get_new_player_club_name()
        first_name = full_name[0]
        last_name = full_name[1]
        player = self.player_model.create_player(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            club_name=club_name
        )
        self.player_view.show_new_player_created(first_name, last_name)
        self.player_model.all_players.append(player)
        helpers.sleep_a_few_seconds()

    def add_participant(self):
        players_found = []
        first_name = self.player_view.get_first_name()
        for player in self.player_model.all_players:
            if first_name in player.first_name:
                players_found.append(player)
        self.player_view.show_players(players_found, numbering=True)
        self.player_view.get_player_to_modify()
        index = self.check_user_choice(
            self.player_view.user_choice_player,
            players_found
        )
        if type(index) == int:
            player_to_modify = players_found[index]
            player_to_modify.tournament_participant = True
            player_to_modify.modify_player()
            PlayerModel.participants.append(player_to_modify)
            
    def get_participants(self):
        participants = [player for player in self.player_model.all_players if player.tournament_participant == True]
        PlayerModel.participants = participants

    def check_user_choice(self, user_choice: str, list_to_control: list):
        list_lenght = [i for i in range(len(list_to_control))]
        print(list_lenght)
        try:
            index = int(user_choice) - 1
            if index in list_lenght:
                print(index)
                return index
            else:
                self.player_view.show_error_message_choice(user_choice)
                helpers.sleep_a_few_seconds()

        except ValueError:
            self.player_view.show_error_message_choice(user_choice)
            helpers.sleep_a_few_seconds()



