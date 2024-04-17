from Models.clubmodel import ClubModel
from Views.clubview import ClubView

import helpers


class ClubController:
    """Classe contrôleur des clubs."""

    def __init__(self, club_view=ClubView(), club_model=ClubModel()):
        """
        Initialise le contrôleur avec le modèle et la vue.

        Args:
            club_view (ClubView, optional): Vue du club. Defaults to ClubView().
            club_model (ClubModel, optional): Modèle du club. Defaults to ClubModel().
        """
        self.club_view = club_view
        self.club_model = club_model

    def club_menu(self):
        """
        Contrôle la fonctionnalité du menu du club, permettant à
        l'utilisateur de naviguer à travers les différentes options des clubs.
        """
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
        """
        Vérifie et crée la nouvelle instance de classe ClubModel avec les
        informations données par l'utilisateur.
        """
        club_name, national_chest_id = self.club_view.get_club_informations()
        if not self._check_club_name_not_empty(club_name):
            return

        if self._check_national_chest_id(national_chest_id):
            if self._check_club_exist(national_chest_id):
                self.club_view.show_club_exist(national_chest_id)
            else:
                self.club_model.create_club(club_name, national_chest_id)
                self.club_view.show_created_club(club_name)

        else:
            self.club_view.show_error_national_chest_id(national_chest_id)

        helpers.sleep_a_few_seconds()

    def modify_club_name(self):
        """
        Met à jour le nom du club existant avec le nouveau nom récupéré.
        """
        club = self.select_club()
        if not club:
            return

        club.name = self.club_view.get_new_club_name()
        club.update_club()
        self.club_view.show_modified_club(club.name)
        helpers.sleep_a_few_seconds()

    def select_club(self, from_player_menu: bool = False) -> ClubModel | None:
        """
        Permet à l'utilisateur de choisir le club désiré.
        L'option "from_player_menu" permet de définir si la fonction est
        appelée du menu player afin de changer l'affichage.

        Args:
            from_player_menu (bool, optional): Affichage à partir du menu
            PlayerController. Défaut False.

        Returns:
            ClubModel | None: Instance de ClubModel ou None si pas de choix
            utilisateur.
        """
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

    def _check_user_choice(self, user_choice: str, options_list: list[str]) -> bool:
        """
        Retourne la présence du choix de l'utilisateur dans la liste des
        options disponibles.

        Args:
            user_choice (str): Choix de l'utilisateur.
            options_list (list[str]): Liste des options disponibles.

        Returns:
            bool: Etat de la vérification (True=Présent, False=Absent).
        """
        if user_choice in options_list:
            return True

        self.club_view.show_error_message_choice(user_choice)
        helpers.sleep_a_few_seconds()
        return False

    def _check_club_name_not_empty(self, club_name: str) -> bool:
        """
        Vérifie si le nom du club n'est pas vide.

        Args:
            club_name (str): Nom du club.

        Returns:
            bool: Etat de la vérification (True=non vide, False=vide).
        """
        if not club_name:
            self.club_view.show_error_empty_name()
            helpers.sleep_a_few_seconds()
            return False
        return True

    def _check_club_exist(self, national_chest_id: str) -> bool:
        """
        Vérifie si le club existe déjà.

        Args:
            national_chest_id (str): Identifiant national du club.

        Returns:
            bool: Etat de la vérification (True=existe, False=n'existe pas).
        """
        return any(
            club.national_chest_id == national_chest_id
            for club in self.club_model.all_clubs
        )

    @staticmethod
    def _check_national_chest_id(national_chest_id: str) -> bool:
        """
        Vérifie si l'identifiant national du club correspond au format
        alphanumérique attendu: ZZ9999.

        Args:
            national_chest_id (str): Identifiant national du club.

        Returns:
            bool: Etat de la vérification (True=conforme, False=non conforme).
        """
        if len(national_chest_id) != 6:
            return False

        if not national_chest_id[:2].isalpha():
            return False

        if not national_chest_id[2:].isdigit():
            return False

        return True
