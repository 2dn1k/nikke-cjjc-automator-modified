import sys
import os
import questionary
from typing import Optional

SELECT_MODE_CHOICES = [
    "1: Prediction Mode (Please enter the betting page in advance)",
    "2: Review Mode (Please enter the result page showing 5 teams in advance)",
    "3: Anti-Buy Mode (Please enter the betting page in advance)",
    "4: League Prediction Mode (Please enter the league page in advance)",
    "5: Prediction 1 vs 2 (View bracket)",
    "6: Prediction 3 vs 4 (View bracket)",
    "7: Prediction 5 vs 6 (View bracket)",
    "8: Prediction 7 vs 8 (View bracket)",
    "9: Prediction 1&2 vs 3&4 (View bracket)",
    "10: Prediction 5&6 vs 7&8 (View bracket)",
    "11: Prediction 1&2&3&4 vs 5&6&7&8 (View bracket)"
]

def select_mode() -> Optional[int]:
    try:
        label = questionary.select(
            "Please select a run mode",
            choices=SELECT_MODE_CHOICES
        ).ask()
    except KeyboardInterrupt:
        sys.exit(0)
    if label is None:
        sys.exit(0)
    return SELECT_MODE_CHOICES.index(label) + 1     