import menus

class ReportModel:
    def __init__(
            self,
            menu_name: str=menus.RAPPORT_MENU[menus.NAME_MENU],
            menu_options:
                list=menus.RAPPORT_MENU[menus.OPTIONS_MENU]
        ):
        self.menu_name = menu_name
        self.menu_options = menu_options