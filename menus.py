from pathlib import Path



DIR_PATH = Path.cwd()
DATA_DIR = DIR_PATH / "data"
TOURNAMENT_DIR = DATA_DIR / "tournament"
SAVING_PATH_CLUB = DATA_DIR / "clubs.json"
SAVING_PATH_PLAYERS = DATA_DIR / "players.json"

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

RAPPORT_MENU = {
    NAME_MENU : "MENU RAPPORTS",
    OPTIONS_MENU : [
        "Afficher la liste des joueurs",
        "///Afficher la liste des tournois",
        "///Afficher le nom et date d'un tournois donné",
        "///Afficher liste des joueurs du tournois",
        "///Afficher liste tours d'un tournois + tous les matchs du tour"
    ]
}

MAIN_MENU_NAME = ALL_MENU[next(iter(ALL_MENU))]
