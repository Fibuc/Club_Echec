import json

import menus

class ClubModel:
    """Classe Club"""
    def __init__(
            self,
            name: str="",
            national_chest_id: str="",
            menu_name: str=menus.CLUB_MENU[menus.NAME_MENU],
            menu_options: list=menus.CLUB_MENU[menus.OPTIONS_MENU]
        ):
        self.name = name
        self.national_chest_id = national_chest_id
        self.menu_name = menu_name
        self.menu_options = menu_options

    def save_club_datas(self):
        """Sauvegarde le nouveau club ou modifie le nom du club existant.

        Args:
            name (str): Nom du club.
            national_chest_id (str): Identifiant national du club.
        """
        datas = {}
        menus.DATA_DIR.mkdir(parents=True, exist_ok=True)
        if menus.SAVING_PATH_CLUB.exists():
            with open(menus.SAVING_PATH_CLUB, "r", encoding="utf-8") as file:
                datas = json.load(file)
        with open(menus.SAVING_PATH_CLUB, "w", encoding="utf-8") as file:
            datas[self.national_chest_id] = self.name
            json.dump(datas, file, ensure_ascii=False, indent=4)

    @staticmethod
    def get_all_clubs_informations():
        if menus.SAVING_PATH_CLUB.exists():
            with open(menus.SAVING_PATH_CLUB, "r", encoding="utf-8") as file:
                datas = json.load(file)
            return datas
        else:
            return {}