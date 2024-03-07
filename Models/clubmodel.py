from dataclasses import dataclass
from pathlib import Path
import json

DIR_PATH = Path.cwd()
DATA_DIR = DIR_PATH / "data"
SAVING_PATH_CLUB = DATA_DIR / "clubs.json"

@dataclass
class ClubModel:
    """Classe Club"""
    name : str = ""
    national_chest_id : str = ""

    @staticmethod
    def save_club_datas(name: str, national_chest_id: str):
        """Sauvegarde le nouveau club ou modifie le nom du club existant.

        Args:
            name (str): Nom du club.
            national_chest_id (str): Identifiant national du club.
        """
        datas = {}
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if SAVING_PATH_CLUB.exists():
            with open(SAVING_PATH_CLUB, "r", encoding="utf-8") as file:
                datas = json.load(file)
        with open(SAVING_PATH_CLUB, "w", encoding="utf-8") as file:
            datas[national_chest_id] = name
            json.dump(datas, file, ensure_ascii=False, indent=4)

    @staticmethod
    def get_all_clubs_informations():
        if SAVING_PATH_CLUB.exists():
            with open(SAVING_PATH_CLUB, "r", encoding="utf-8") as file:
                datas = json.load(file)
            return datas
        else:
            return {}