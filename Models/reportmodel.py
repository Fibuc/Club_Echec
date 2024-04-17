import menus


class ReportModel:
    """Classe modèle des rapports."""
    def __init__(
            self, menu_name: str = menus.REPORT_MENU[menus.NAME_MENU],
            menu_options: list[str] = menus.REPORT_MENU[menus.OPTIONS_MENU],
            menu_tournament_report_name: str =
            menus.TOURNAMENT_REPORT_MENU[menus.NAME_MENU],
            menu_tournament_report_option: list[str] =
            menus.TOURNAMENT_REPORT_MENU[menus.OPTIONS_MENU]
    ):
        """Initialise l'instance de classe des rapports.

        Args:
            menu_name (str, optional): Nom du menu.
            Défaut menus.REPORT_MENU[menus.NAME_MENU].
            menu_options (list, optional): Options du menu.
            Défaut menus.REPORT_MENU[menus.OPTIONS_MENU].
            menu_tournament_report_name (str, optional):
            Nom du menu rapport tournois. Défaut menus.TOURNAMENT_REPORT_MENU[menus.NAME_MENU].
            menu_tournament_report_option (list, optional):
            Option du menu rapport tournois. Défaut menus.TOURNAMENT_REPORT_MENU[menus.OPTIONS_MENU].
        """
        self.menu_name = menu_name
        self.menu_options = menu_options
        self.menu_tournament_report_name = menu_tournament_report_name
        self.menu_tournament_report_option = menu_tournament_report_option
