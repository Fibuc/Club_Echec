from pathlib import Path



DIR_PATH = Path.cwd()
DATA_DIR = DIR_PATH / "data"
TOURNAMENT_DIR = DATA_DIR / "tournament"
SAVING_PATH_CLUB = DATA_DIR / "clubs.json"
SAVING_PATH_PLAYERS = DATA_DIR / "players.json"

# Keys player dictionnary
KEY_PLAYER_FIRST_NAME = "first_name"
KEY_PLAYER_LAST_NAME = "last_name"
KEY_PLAYER_BIRTH_DATE = "birth_date"
KEY_PLAYER_CLUB_NAME = "club_name"
KEY_PLAYER_NUMBER_POINT = "number_of_points"
KEY_PLAYER_TOURNAMENT_PARTICIPANT = "tournament_participant"

# Keys tournament dictionnary
KEY_TOURNAMENT_NAME = "name"
KEY_TOURNAMENT_LOCATION = "location"
KEY_TOURNAMENT_PLAYERS_LIST = "players_list"
KEY_TOURNAMENT_ROUNDS_LIST = "rounds_list"
KEY_TOURNAMENT_DATE_TIME_START = "date_time_start"
KEY_TOURNAMENT_DATE_TIME_END = "date_time_end"
KEY_TOURNAMENT_DESCRIPTION = "description"

WELCOME_MESSAGE = "BIENVENUE DANS L'APPLICATION DE TOURNOIS"

NAME_MENU = "menu_name"
OPTIONS_MENU = "menu_options"

ALL_MENU = {
    NAME_MENU : "MENU PRINCIPAL",
    OPTIONS_MENU : {
        "Créer/reprendre un tournois": {
            NAME_MENU : "MENU TOURNOIS",
            OPTIONS_MENU : [
                "Créer un tournois",
                "Reprendre un tournois"
            ]
        },
        "Ajouter/modifier un joueur": {
            NAME_MENU : "MENU JOUEUR",
            OPTIONS_MENU : [
                "Ajouter un joueur",
                "Modifier un joueur"
            ]
        },
        "Ajouter/modifier un club": {
            NAME_MENU : "MENU CLUB",
            OPTIONS_MENU : [
                "Ajouter un club",
                "Modifier un club"
            ]
        },
        "Afficher des rapports": {
            NAME_MENU : "MENU RAPPORTS",
            OPTIONS_MENU : [
                "Afficher la liste des joueurs",
                "Afficher la liste des tournois",
                "Afficher le nom et date d'un tournois donné",
                "Afficher liste des joueurs du tournois",
                "Afficher liste tours d'un tournois + tous les matchs du tour"
            ]
        },
        "Quitter l'application": None
    }
}

MAIN_MENU = {
    NAME_MENU: "MENU PRINCIPAL",
    OPTIONS_MENU: [
        "Créer un nouveau tournois",
        "Ajouter/modifier un joueur",
        "Ajouter/modifier un club",
        "Afficher des rapports",
        "Quitter l'application"
    ]
}

TOURNAMENT_MENU = {
    NAME_MENU : "CREATION TOURNOIS",
    OPTIONS_MENU : [
        "Valider et lancer le tournois",
        "Ajouter/retirer des participants"
    ]
}

ROUND_MENU = {
    NAME_MENU: "TOURNOIS LANCE",
    OPTIONS_MENU: [
        "Lancer les matchs"
    ]
}

MATCH_MENU = {
    NAME_MENU: "MENU MATCH"
}

PLAYER_MENU = {
    NAME_MENU : "MENU JOUEUR",
    OPTIONS_MENU : [
        "Ajouter un joueur",
        "Modifier un joueur"
    ]
}

CLUB_MENU = {
    NAME_MENU : "MENU CLUB",
    OPTIONS_MENU : [
        "Ajouter un club",
        "Modifier un club"
    ]
}

RAPPORT_MENU = {
    NAME_MENU : "MENU RAPPORTS",
    OPTIONS_MENU : [
        "Afficher la liste des joueurs",
        "Afficher la liste des tournois",
        "Afficher le nom et date d'un tournois donné",
        "Afficher liste des joueurs du tournois",
        "Afficher liste tours d'un tournois + tous les matchs du tour"
    ]
}

MAIN_MENU_NAME = ALL_MENU[next(iter(ALL_MENU))]

ACTION_CHOICE_MENU = {
    " <-- Revenir au menu précédent" : "launch = False",
    "Créer un tournois" : "self.create_tournament_menu()",
    "Reprendre un tournois" : "self.resume_tournament_menu()",
    "Ajouter un joueur" : "self.player.create_new_player()",
    "Modifier un joueur" : "self.player.modify_a_player()",
    "Ajouter un club" : "self.club.create_new_club()",
    "Modifier un club" : "self.club.change_club_name()",
    "Afficher la liste des joueurs" : (
        "self.player.show_players_in_order()"
    ),
    "Afficher la liste des tournois" : (
        "print('Affiche de la liste des tournois')"
    ),
    "Afficher le nom et date d'un tournois donné" : (
        "print(\"Affiche le nom et la date d'un tournois\")"
    ),
    "Afficher liste des joueurs du tournois" : (
        "print('Affiche la liste des joueurs du tournois')"
    ),
    "Afficher liste tours d'un tournois + tous les matchs du tour" : (
        "print(\"Affiche la liste des tours d'un tournois et tous"
        " les matchs\")"
    ),
    "Valider et lancer le tournois" : "self.tournament.start_tournament()",
    "Ajouter des participants" : "print('Ajout des participants')",
    "Afficher les participants" : "self.tournament.show_participants()"
}

