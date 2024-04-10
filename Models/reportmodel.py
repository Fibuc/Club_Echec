import menus

class ReportModel:
    def __init__(
            self, menu_name: str=menus.REPORT_MENU[menus.NAME_MENU],
            menu_options: list=menus.REPORT_MENU[menus.OPTIONS_MENU],
            menu_tournament_report_name: str= 
                menus.TOURNAMENT_REPORT_MENU[menus.NAME_MENU],
            menu_tournament_report_option: list=
                menus.TOURNAMENT_REPORT_MENU[menus.OPTIONS_MENU]
        ):
        self.menu_name = menu_name
        self.menu_options = menu_options
        self.menu_tournament_report_name = menu_tournament_report_name
        self.menu_tournament_report_option = menu_tournament_report_option