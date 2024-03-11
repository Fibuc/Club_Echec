from datetime import datetime
from time import sleep
from pathlib import Path

BORDER_SIZE = 40
BORDER = "=" * BORDER_SIZE
BACK_TO_LINE = "\n"
SPACE = BACK_TO_LINE * 10
SECOND_TO_WAIT = 3

DIR_PATH = Path.cwd()
DATA_DIR = DIR_PATH / "data"
TOURNAMENT_DIR = DATA_DIR / "tournament"
SAVING_PATH_CLUB = DATA_DIR / "clubs.json"
SAVING_PATH_PLAYERS = DATA_DIR / "players.json"

WELCOME_MESSAGE = "BIENVENUE DANS L'APPLICATION DE TOURNOIS"

NAME_MENU = "menu_name"
OPTIONS_MENU = "menu_options"

MAIN_MENU = {
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

MAIN_MENU_NAME = MAIN_MENU[next(iter(MAIN_MENU))]

ACTION_CHOICE_MENU = {
    " <-- Revenir au menu précédent" : "launch = False",
    "Créer un tournois" : "print(\"création d'un tournois\")",
    "Reprendre un tournois" : "print('Reprise du tournois')",
    "Ajouter un joueur" : "self.player.create_new_player()",
    "Modifier un joueur" : "self.player.modify_a_player()",
    "Ajouter un club" : "self.club.create_new_club()",
    "Modifier un club" : "self.club.change_club_name()",
    "Afficher la liste des joueurs" : (
        "self.player."
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
    )
}

def sleep_a_few_seconds():
    sleep(SECOND_TO_WAIT)

def format_date_time():
    """Récupère la date et l'heure de l'exécution.

    Returns:
        str: Retourne la date et l'heure.
    """
    now = datetime.now()
    date = now.date()
    time = f"{now.hour}:{now.minute}:{now.second}"
    return f"{date} {time}"

def get_date():
    now = datetime.now()
    return now.date()

