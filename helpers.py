BORDER_SIZE = 40
BORDER = "=" * BORDER_SIZE
BACK_TO_LINE = "\n"
SPACE = BACK_TO_LINE * 10

WELCOME_MESSAGE = "BIENVENUE DANS L'APPLICATION DE TOURNOIS"

MAIN_MENU = {
    "menu_name": "MENU PRINCIPAL",
    "menu_options": {
        "Créer/reprendre un tournois": {
            "menu_name": "MENU TOURNOIS",
            "menu_options": ["Créer un tournois", "Reprendre un tournois"]
        },
        "Créer un nouveau joueur": {
            "menu_name": "MENU JOUEUR",
            "menu_options": ["Ajouter un joueur", "Modifier un joueur"]
        },
        "Ajouter/modifier un club": {
            "menu_name": "MENU CLUB",
            "menu_options": ["Ajouter un club", "Modifier un club"]
        },
        "Afficher le menu des rapports": {
            "menu_name": "MENU RAPPORTS",
            "menu_options": [
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
    "Ajouter un joueur" : "print('Ajout du joueur')",
    "Modifier un joueur" : "print('Modification du joueur')",
    "Ajouter un club" : "print('Ajout du club')",
    "Modifier un club" : "print('Modification du club')",
    "Afficher la liste des joueurs" : (
        "print('Affiche de la liste des joueurs')"
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