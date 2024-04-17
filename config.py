from pathlib import Path

# Configurations des menus.
BORDER_SIZE = 125
BORDER = "=" * BORDER_SIZE
SPACING_SIZE = 10
SPACE = "\n" * SPACING_SIZE

# Configuration d'affichage des messages.
SECOND_TO_WAIT = 3

# Configurations des tournois.
DEFAULT_NUMBER_ROUNDS = 4
MINIMUM_PLAYER_FOR_TOURNAMENT = 8

# Configuration des joueurs.
DEFAULT_NUMBER_OF_POINT = 0

# Configurations des répertoires.
DIR_PATH = Path(__file__).resolve().parent
DATA_DIR = DIR_PATH / "data"
TOURNAMENT_DIR = DATA_DIR / "tournament"
SAVING_PATH_CLUB = DATA_DIR / "clubs.json"
SAVING_PATH_PLAYERS = DATA_DIR / "players.json"
