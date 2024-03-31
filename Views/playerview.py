from typing import Callable

import helpers

EDITABLE_INFORMATIONS_PLAYER = [
        "Le prénom",
        "Le nom de famille",
        "La date de naissance",
        "Le club"
]

class PlayerView:
    
    # Récupération de données utilisateur
    @staticmethod
    def get_menu_user_choice() -> str:
            """Retourne le choix de l'utilisateur fait au menu.

            Returns:
                str: Choix de l'utilisateur
            """
            return input("Quel est votre choix ? : ")
    
    @staticmethod
    def get_new_player_name():
        first_name = input("Quel est le prénom du joueur ? : ").capitalize()
        last_name = input("Quel est le nom de famille du joueur ? : ").capitalize()
        return first_name, last_name
  
    @staticmethod
    def get_new_player_birth_date():
        return input("Quelle est sa date de naissance ? (JJ/MM/AAAA): ")
   
    @staticmethod
    def get_new_player_club_name():
        return input("Quel est son club ? : ")

    @staticmethod
    def get_new_player_participation():
        return input("Participera-t-il au prochain tournois ? (O/N) : ")

    def get_first_name(self):
        self._show_border()
        return input("(Laisser vide pour afficher tous les joueurs)\nQuel est le prénom du joueur ? : ")

    def get_index_player_to_modify(self):
        return input("Quel est le numéro du joueur à modifier ? : ")

    def get_information_to_modify(self):
        self._show_border()
        return input("Quel est l'information du joueur à modifier ? : ")
    
    @staticmethod
    def get_new_value():
        return input(f"Quelle est la nouvelle valeur ? : ")
  
    # Affichage des données à l'utilisateur
    @staticmethod
    def show_menu(
        menu_function: Callable,
        menu_name: str,
        options_menu: list
    ) -> list:
        """Affiche le menu formaté.

        Args:
            menu_function (Callable): Fonction comprenant le menu.
            menu_name (str): Nom du menu.
            options_menu (list): Liste des options du menu.
            first_display (bool): Etat du premier affichage.

        Returns:
            list: Retourne la liste des options.
        """
        decoration = helpers.decorative_menu_element(function=menu_function)
        full_menu = decoration(menu_name, options_menu)
        print(full_menu)
        return options_menu
    
    @staticmethod
    def show_error_message_choice(user_choice: str):
        """Affiche un message d'erreur lorsque le choix de l'utilisateur
        n'est pas correct.

        Args:
            user_choice (str): Choix de l'utilisateur.
        """
        print(f"Erreur: La commande \"{user_choice}\" n'est pas une commande valide.")
            
    def show_players(self, players: list, numbering: bool=False):
        self._show_number_of_player_found(players)
        self._show_border()
        current_player = 0
        for player in players:
            if numbering:
                current_player += 1
                print(f"Joueur {current_player}: {player}")
            else:
                print(player)

        self._show_border()
    
    @staticmethod
    def show_new_player_created(player_name: str):
        print(f"Le nouveau joueur \"{player_name}\" a bien été créé.")

    @staticmethod
    def show_error_player_already_exist(first_name: str, last_name: str, birth_date: str):
        print(f"Erreur: Le joueur \"{first_name} {last_name} {birth_date}\" existe déjà.")

    @staticmethod   
    def show_no_player_in_database(): # Pas utilisé !!!
        print("Il n'y a aucun joueur dans la base de données.")
    
    @staticmethod
    def show_no_match_player_found(prenom):
        print(f"Il n'y a aucun joueur ayant pour prénom \"{prenom}\" dans la base de données.")
    
    @staticmethod
    def show_no_paticipants(): # Pas utilisé !!!
        print("Il n'y a aucun participant au prochain prochain tournois.")

    def show_informations_type(self):
        print("Liste des informations :")
        current_information = 1
        for information in EDITABLE_INFORMATIONS_PLAYER:
            print(f"{current_information} - {information}")
            current_information += 1
    
    def show_title_players(self): # Pas utilisé !!!
        self._show_border()
        print("Liste des joueurs")
        self._show_border()
  
    def show_valid_modifications(self):
        self._show_border()
        print("Validé! Le joueur à bien été modifié.")
 
    @staticmethod
    def show_error_date(birth_date):
        print(f"La date \"{birth_date}\" n'est pas valide.")

    @staticmethod
    def _show_number_of_player_found(result_list: list):
        result_numer = len(result_list)
        plural_choice = (
            f"{'s ont été trouvés.' if result_numer > 1 else " a été trouvé."}"
        )
        print(f"Résultat: {result_numer} joueur{plural_choice} ")

    @staticmethod
    def _show_border():
        print(helpers.BORDER)
