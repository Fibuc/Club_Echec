from dataclasses import dataclass
from pathlib import Path
import json

DIR_PATH = Path(__file__).parent.parent
SAVING_PATH_CLUB = DIR_PATH / "data" / "clubs.json"

@dataclass
class Club:
    """Classe Club"""
    name : str
    national_chest_id : str

    @staticmethod
    def create_new_club(name: str, national_chest_id: str):     # Controleur doit vérifier si l'ID existe déjà et s'il souhaite modifier le nom associé sinon annuler.
        """Création d'une nouvelle instance de Club.

        Args:
            name (str): Nom du club.
            national_chest_id (str): Identifiant national du club.

        Returns:
            fonction: Sauvegarde la nouvelle instance dans le fichier
        """
        return Club._save_new_club(name, national_chest_id)
    
    @staticmethod
    def _save_new_club(name, national_chest_id):
        """Sauvegarde la nouvelle instance de Club.

        Args:
            name (str): Nom du club.
            national_chest_id (str): Identifiant national du club.

        Returns:
            dict: Dictionnaire des datas sauvegardées.
        """
        with open(SAVING_PATH_CLUB, "r", encoding="utf-8") as file:
            datas = json.load(file)
        with open(SAVING_PATH_CLUB, "w", encoding="utf-8") as file:
            datas[national_chest_id] = name
            json.dump(datas, file, ensure_ascii=False, indent=4)
        return datas