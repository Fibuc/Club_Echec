import helpers

class MenuModel:
    """Classe modèle des menus.
    """
    def __init__(self, name:str = "", options_list:list =[], file_name:str = ""):
        self.name = name
        self.options_list = options_list
        self.file_name = file_name

    @staticmethod
    def create_menu(name_menu: str, option_list: list) -> str:
        """Formatage du menu souhaité en chaînes de caratères.

        Args:
            name_menu (str): Nom du menu.
            option_list (list): Liste des options du menu.

        Returns:
            str: Menu formaté en chaîne de caractères.
        """
        number_of_option = 1
        all_choices = []
        for option in option_list:
            all_choices.append(f"{number_of_option} - {option}")
            number_of_option += 1
        if name_menu != helpers.MAIN_MENU_NAME:
            all_choices.append(
                f"{number_of_option} <-- Revenir au menu précédent")
        
        all_choices_menu = "\n".join(all_choices)
        return all_choices_menu