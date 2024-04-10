from pathlib import Path



DIR_PATH = Path.cwd()
DATA_DIR = DIR_PATH / "data"
TOURNAMENT_DIR = DATA_DIR / "tournament"
SAVING_PATH_CLUB = DATA_DIR / "clubs.json"
SAVING_PATH_PLAYERS = DATA_DIR / "players.json"

WELCOME_MESSAGE = "BIENVENUE DANS L'APPLICATION DE TOURNOIS"

NAME_MENU = "menu_name"
OPTIONS_MENU = "menu_options"

MAIN_MENU = {
    NAME_MENU: "MENU PRINCIPAL",
    OPTIONS_MENU: [
        "Créer/reprendre un tournois",
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
        "Lancer les matchs",
        "Terminer les matchs"
    ]
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

REPORT_MENU = {
    NAME_MENU : "MENU RAPPORTS",
    OPTIONS_MENU : [
        "Afficher la liste des joueurs",
        "Afficher la liste des clubs",
        "Afficher la liste des tournois"
    ]
}

TOURNAMENT_REPORT_MENU = {
    NAME_MENU : "RAPPORT TOURNOIS",
    OPTIONS_MENU : [
        "Afficher la liste des participants",
        "Afficher la liste des tours",
    ]
}

MAIN_MENU_NAME = MAIN_MENU[next(iter(MAIN_MENU))]
