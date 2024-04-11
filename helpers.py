from datetime import datetime
from time import sleep
from typing import Callable
from random import shuffle

import menus

BORDER_SIZE = 125
BORDER = "=" * BORDER_SIZE
BACK_TO_LINE = "\n"
SPACE = BACK_TO_LINE * 10
SECOND_TO_WAIT = 3

INDEX_MENU_NAME = 0
INDEX_MENU_OPTIONS = 1
INDEX_MENU_DESCRIPTION = 2

DEFAULT_NUMBER_ROUNDS = 4

MINIMUM_PLAYER_FOR_TOURNAMENT = 8

DEFAULT_NUMBER_OF_POINT = 0

def sleep_a_few_seconds():
    sleep(SECOND_TO_WAIT)

def format_date_time(now):
    """Récupère la date et l'heure de l'exécution.

    Returns:
        str: Retourne la date et l'heure.
    """
    date = now.date()
    time = f"{now.hour}:{now.minute}:{now.second}"
    return f"{date.strftime("%d/%m/%Y")} {time}"

def format_date(date):
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return date.strftime("%d/%m/%Y %H:%M:%S")

def get_date_time():
    now = datetime.now()
    return format_date_time(now)

def get_date():
    now = datetime.now()
    return now.date()

def create_menu(name_menu: str, option_list: list, description: str="", can_undo: bool=True) -> str:
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
    if name_menu != menus.MAIN_MENU_NAME and can_undo:
        all_choices.append(
            f"{number_of_option} <-- Revenir au menu précédent")

    return "\n".join(all_choices)


def decorative_menu_element(function: Callable, first_display: bool=True) -> Callable:
    """Enveloppe pour formater le menu désiré pour affichage.

    Args:
        function (Callable): Fonction comportant le menu.
        first_display (bool): Etat du premier affichage.

    Returns:
        Callable: Retourne l'enveloppe du menu décoré.
    """
    def wrapper(*args, **kwargs):
        menu_name = args[INDEX_MENU_NAME]
        border_menu_size = (BORDER_SIZE - len(menu_name)) // 2
        try:
            sub_name = args[INDEX_MENU_DESCRIPTION]
        except IndexError:
            sub_name = ""
        result = ""
        if sub_name != "":
            result = search_description(menu_name, sub_name)

        centered_menu = f"{border_menu_size * " "}{menu_name}"
        if menu_name != menus.MAIN_MENU_NAME:
            space = SPACE
        else:
            space = show_first_display(first_display)
        
        top_menu = (
            f"{space}{BORDER}{BACK_TO_LINE}{centered_menu}"
            f"{BACK_TO_LINE}{BORDER}{BACK_TO_LINE}{result}"
        )
 
        menu_option = function(*args, **kwargs)
        bottom_menu = f"{BACK_TO_LINE}{BORDER}"
        all_menu = f"{top_menu}{menu_option}{bottom_menu}"

        return all_menu
    
    return wrapper



def show_first_display(first_display: bool) -> str:
    """Ajoute un espace s'il ne s'agit pas du premier affichage
    du menu principal.

    Args:
        first_display (bool): Indique l'état de l'affichage

    Returns:
        str: Espace selon l'état.
    """
    return "" if first_display else SPACE

def search_description(menu_name, sub_name):
    if menu_name == menus.TOURNAMENT_MENU[menus.NAME_MENU]:
        return description_tournament(sub_name)
    elif menu_name == menus.ROUND_MENU[menus.NAME_MENU]:
        return description_round(sub_name)
    elif menu_name == menus.TOURNAMENT_REPORT_MENU[menus.NAME_MENU]:
        return description_tournament_report(sub_name)
    
def description_tournament(sub_name):
    result = ""
    result += (
        f"Liste des {len(sub_name)} joueurs participants: {BACK_TO_LINE}"
        f"{BORDER}{BACK_TO_LINE}"
    )
    for participant in sub_name:            
        result += (f"{participant}{BACK_TO_LINE}")

    result += f"{BORDER}{BACK_TO_LINE}"
    return result

def description_round(sub_name):
    result = ""
    result += f"Round actuel : Round {sub_name}{BACK_TO_LINE}{BORDER}{BACK_TO_LINE}"
    return result

def shuffle_element(element_to_shuffle: list):
    return shuffle(element_to_shuffle)

def convert_if_integer(number):
    if isinstance(number, float) and number.is_integer():
        return int(number)
    return number

def description_tournament_report(sub_name):
    result = ""
    result += (
        f"Nom: {sub_name[0]}\nLieu: {sub_name[1]}\nDate début: {sub_name[2]}"
        f"\nDate de fin: {sub_name[3]}{BACK_TO_LINE}{BORDER}{BACK_TO_LINE}"
    )
    return result
