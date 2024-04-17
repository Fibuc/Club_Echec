from typing import ClassVar

from tinydb import TinyDB, where

import helpers
import menus


class RoundModel:
    """Classe modèle des rounds."""
    menu_name: ClassVar[str] = menus.ROUND_MENU[menus.NAME_MENU]
    menu_options: ClassVar[list] = menus.ROUND_MENU[menus.OPTIONS_MENU]

    def __init__(
        self, round_number: int = 0, date_time_start: str = "",
        date_time_end: str = "", matches: list = []
    ):
        """Initialise l'instance de classe RoundModel.

        Args:
            round_number (int, optional): Numéro du round. Défaut 0.
            date_time_start (str, optional): Date de début du round.
            Défaut "".
            date_time_end (str, optional): Date de fin du round. Défaut "".
            matches (list, optional): Matchs du round. Défaut [].
        """
        self.round_number = round_number
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.matches = matches

    def __str__(self) -> str:
        """Retourne l'instance RoundModel sous forme de chaîne de caractères.

        Returns:
            str: Chaîne de caractères représentant l'objet.
        """
        if not self.date_time_start:
            self.date_time_start = "Non commencé"

        if not self.date_time_end:
            self.date_time_end = "Non terminé"

        return (f"Nom: Round {self.round_number}, Date de début: "
                f"{self.date_time_start}, Date de fin: {self.date_time_end}, "
                f"Nombre de match: {len(self.matches)}"
                )

    def __repr__(self) -> str:
        """Retourne la représentation sous forme de chaîne de
        caractères de l'instance RoundModel.

        Returns:
            str: Chaîne de caractères de la représentation de l'objet.
        """
        return f"RoundModel{self.round_number, self.date_time_start, self.date_time_end}"

    @staticmethod
    def create_new_round(round_number: int, matches: list) -> "RoundModel":
        """Crée une instance de classe RoundModel.

        Args:
            round_number (int): Numéro du round.
            matches (list): Matchs du round.

        Returns:
            RoundModel: Instance de RoundModel créée.
        """
        date_string = str(helpers.get_date_time())
        return RoundModel(
            round_number=round_number,
            date_time_start=date_string,
            matches=matches
            )

    @staticmethod
    def _create_db_table(tournament_db: TinyDB) -> TinyDB.table_class:
        """
        Crée une table "Rounds" dans la base de données.

        Args:
            tournament_db (TinyDB): Base de données du tournoi.

        Returns:
            TinyDB.table_class: La table dans la base de données.
        """
        return tournament_db.table("Rounds")

    def save_round(self, tournament_db: TinyDB):
        """Enregistre l'instance du round dans la base de données.

        Args:
            tournament_db (TinyDB): Base de données.
        """
        table = self._create_db_table(tournament_db)
        table.insert(self.__dict__)

    def update_round(self, tournament_db: TinyDB):
        """Met à jour les informations du round dans la base de données.

        Args:
            tournament_db (TinyDB): Base de données.
        """
        table = self._create_db_table(tournament_db)
        table.update(self.__dict__, where("round_number") == self.round_number)

    @classmethod
    def load_rounds(cls, tournament_db: TinyDB) -> list['RoundModel']:
        """
        Charge toutes les instances de classe à partir de la base
        de données.

        Args:
            tournament_db (TinyDB): Base de données.

        Returns:
            list[RoundModel]: Liste de toutes les instances de RoundModel.
        """
        table = cls._create_db_table(tournament_db)
        return [cls(**round) for round in table]
