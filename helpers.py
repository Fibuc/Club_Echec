from datetime import datetime, date
from time import sleep
from typing import Callable
from random import shuffle

from config import SECOND_TO_WAIT, BORDER_SIZE, BORDER, SPACE
import menus

INDEX_MENU_NAME = 0


def sleep_a_few_seconds():
    """
    Met le programme en pause pendant la durée définie dans la variable
    "SECOND_TO_WAIT" dans le fichier de configuration "config.py".
    """
    sleep(SECOND_TO_WAIT)


def format_date_time(now: datetime) -> str:
    """Formate la date et l'heure en chaîne de caractères.

    Args:
        now (datetime): Objet de la date et de l'heure actuelles.

    Returns:
        str: La chaîne de date et d'heure formatée.
    """
    date = now.date()
    time = f"{now.hour}:{now.minute}:{now.second}"
    return f"{date.strftime('%d/%m/%Y')} {time}"


def get_date_time() -> str:
    """
    Renvoie la date et l'heure actuelles au format "dd/mm/yyyy HH:MM:SS".

    Returns:
        str: La date et l'heure actuelles formatées.
    """
    now = datetime.now()
    return format_date_time(now)


def get_date() -> date:
    """Renvoie la date actuelle.

    Returns:
        date: La date actuelle.
    """
    return date.today()


def convert_if_integer(number: int | float) -> int | float:
    """
    Convertit un nombre flottant en entier s'il est un nombre entier, sinon
    renvoie le nombre flottant d'origine.

    Args:
        number (float): Le nombre flottant à convertir en entier.

    Returns:
        int | float: Le nombre converti ou le flottant.
    """
    if isinstance(number, float) and number.is_integer():
        return int(number)
    return number


def shuffle_element(list_to_shuffle: list):
    """Mélange les éléments d'une liste donnée.

    Args:
        list_to_shuffle (list): Liste à mélanger.
    """
    shuffle(list_to_shuffle)


def create_menu(name_menu: str, option_list: list, can_undo: bool = True) -> str:
    """Formatage du menu souhaité en chaînes de caratères.

    Args:
        name_menu (str): Nom du menu.
        option_list (list): Liste des options du menu.
        can_undo(bool): Possibilité de l'utilisateur à revenir au menu
        précédent.

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


def decorative_menu_element(
        function: Callable, first_display: bool = True,
        description: int | list = None
) -> Callable:
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
        result = ""
        if description != "":
            result = _search_description(menu_name, description)

        centered_menu = f"{border_menu_size * ' '}{menu_name}"
        if menu_name != menus.MAIN_MENU_NAME:
            space = SPACE
        else:
            space = _show_first_display(first_display)

        top_menu = (f"{space}{BORDER}\n{centered_menu}\n{BORDER}\n{result}")

        menu_option = function(*args, **kwargs)
        bottom_menu = f"\n{BORDER}"
        all_menu = f"{top_menu}{menu_option}{bottom_menu}"

        return all_menu

    return wrapper


def _show_first_display(first_display: bool) -> str:
    """Ajoute un espace s'il ne s'agit pas du premier affichage
    du menu principal.

    Args:
        first_display (bool): Indique l'état de l'affichage

    Returns:
        str: Espace selon l'état.
    """
    return "" if first_display else SPACE


def _search_description(menu_name: str, element_to_description: list | int) -> str:
    """Renvoie la description du menu en fonction de son nom.

    Args:
        menu_name (str): Nom du menu.
        element_to_description (list | int): Elément à insérer en description.
        Celui-ci peut être un nombre entier ou une liste.

    Returns:
        str: La chaîne de caractère de la description.
    """
    if (menu_name == menus.TOURNAMENT_MENU[menus.NAME_MENU] and
            isinstance(element_to_description, list)):
        return _description_tournament(element_to_description)
    elif (menu_name == menus.ROUND_MENU[menus.NAME_MENU] and
            isinstance(element_to_description, int)):
        return _description_round(element_to_description)
    elif (menu_name == menus.TOURNAMENT_REPORT_MENU[menus.NAME_MENU] and
            isinstance(element_to_description, list)):
        return _description_tournament_report(element_to_description)

    return ""


def _description_tournament(participants: list) -> str:
    """Génère la description du tournois à partir de la liste des
    participants.

    Args:
        participants (list): Liste des participants.

    Returns:
        str: Description du menu avec le nombre de participants.
    """
    result = ""
    result += (
        f"Liste des {len(participants)} joueurs participants: \n{BORDER}\n")
    for participant in participants:
        result += f"{participant}\n"

    result += f"{BORDER}\n"
    return result


def _description_round(current_round: int) -> str:
    """Génère une description du round à partir du round actuel.

    Args:
        current_round (int): Round actuel.

    Returns:
        str: Description du menu avec le numéro du round.
    """
    result = ""
    result += f"Round actuel : Round {current_round}\n{BORDER}\n"
    return result


def _description_tournament_report(informations: list) -> str:
    """Génère une description du rapport du tournoi à partir de ses
    informations.

    Args:
        informations (list): Liste des informations du tournois.

    Returns:
        str: Description du menu avec les informations du tournois.
    """
    result = ""
    result += (
        f"Nom: {informations[0]}\nLieu: {informations[1]}\nVainqueur: {informations[4]}\n"
        f"Date début: {informations[2]}\nDate de fin: {informations[3]}\n{BORDER}\n"
    )
    return result
