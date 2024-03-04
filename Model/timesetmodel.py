from dataclasses import dataclass
from datetime import datetime

@dataclass
class Timer:

    @staticmethod
    def format_date_time():
        """Récupère la date et l'heure de l'exécution.

        Returns:
            str: Retourne la date et l'heure.
        """
        now = datetime.now()
        date = now.date()
        time = f"{now.hour}:{now.minute}:{now.second}"
        return f"{date} {time}"
    
    @staticmethod
    def get_date():
        now = datetime.now()
        return now.date()



