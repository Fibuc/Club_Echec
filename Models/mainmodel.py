import menus


class MainModel:
    """Classe modèle principal."""
    def __init__(
        self,
        menu_name: str = menus.MAIN_MENU[menus.NAME_MENU],
        menu_options: list = menus.MAIN_MENU[menus.OPTIONS_MENU],
    ):
        """Intialise une instance de classe MainModel.

        Args:
            menu_name (str, optional): Nom du menu.
            Défaut menus.MAIN_MENU[menus.NAME_MENU].
            menu_options (list, optional): Liste des options du menu.
            Défaut menus.MAIN_MENU[menus.OPTIONS_MENU].
        """
        self.menu_name = menu_name
        self.menu_options = menu_options
