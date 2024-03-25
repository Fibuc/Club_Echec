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
        """
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
        """

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
        player.save_player()
        self.player_view.show_new_player_created(first_name, last_name)
        helpers.sleep_a_few_seconds()

    def add_participant(self):
        self.player_view.show_players()

if __name__ == "__main__":
    controller = PlayerController()
    controller.new_player()
