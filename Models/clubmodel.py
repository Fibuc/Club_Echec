import json

import helpers

class ClubModel:
    """Classe Club"""
    def __init__(self, name: str="", national_chest_id: str=""):
        self.name = name
        self.national_chest_id = national_chest_id

    @staticmethod
    def save_club_datas(name: str, national_chest_id: str):
        """Sauvegarde le nouveau club ou modifie le nom du club existant.

        Args:
            name (str): Nom du club.
            national_chest_id (str): Identifiant national du club.
        """
        datas = {}
        helpers.DATA_DIR.mkdir(parents=True, exist_ok=True)
        if helpers.SAVING_PATH_CLUB.exists():
            with open(helpers.SAVING_PATH_CLUB, "r", encoding="utf-8") as file:
                datas = json.load(file)
        with open(helpers.SAVING_PATH_CLUB, "w", encoding="utf-8") as file:
            datas[national_chest_id] = name
            json.dump(datas, file, ensure_ascii=False, indent=4)

    @staticmethod
    def get_all_clubs_informations():
        if helpers.SAVING_PATH_CLUB.exists():
            with open(helpers.SAVING_PATH_CLUB, "r", encoding="utf-8") as file:
                datas = json.load(file)
            return datas
        else:
            return {}