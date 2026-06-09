import sys
import os
import questionary
from typing import Optional, Tuple

SELECT_MODE_CHOICES = [
    "1: Prediction Mode (Please enter the betting page in advance)",
    "2: Review Mode (Please enter the result page showing 5 teams in advance)",
    "3: Anti-Buy Mode (Please enter the betting page in advance)",
    "4: League Prediction Mode (Please enter the league page in advance)",
    "5: Bracket Predictions (Please enter the bracket page in advance)"
]

BRACKET_PREDICTION_CHOICES = [
    "5: Prediction 1 vs 2 (View bracket)",
    "6: Prediction 3 vs 4 (View bracket)",
    "7: Prediction 5 vs 6 (View bracket)",
    "8: Prediction 7 vs 8 (View bracket)",
    "9: Prediction 1&2 vs 3&4 (View bracket)",
    "10: Prediction 5&6 vs 7&8 (View bracket)",
    "11: Prediction 1&2&3&4 vs 5&6&7&8 (View bracket)"
]

BOOLEAN_CHOICES = [
    "64-16 Bracket",
    "Top 8 Bracket"
]

ALL_CHOICES = SELECT_MODE_CHOICES[:-1] + BRACKET_PREDICTION_CHOICES

def select_mode() -> Optional[Tuple[int, bool]]:
    top_8_bool = False
    
    try:
        label = questionary.select(
            "Please select a run mode",
            choices=SELECT_MODE_CHOICES
        ).ask()
    except KeyboardInterrupt:
        sys.exit(0)
    if label is None:
        sys.exit(0)
        
        
    if label == SELECT_MODE_CHOICES[-1]:
        # Ask the Yes/No confirmation question
        bracket = questionary.select(
            "Which bracket are you viewing?",
            choices=BOOLEAN_CHOICES
        ).ask()
            
        if bracket is None:
            sys.exit(0)
        if bracket == BOOLEAN_CHOICES[0]:
            top_8_bool = False
        elif bracket == BOOLEAN_CHOICES[1]:
            top_8_bool = True

        bracket_selection = questionary.select(
            "Please select a bracket prediction option",
            choices=BRACKET_PREDICTION_CHOICES
        ).ask()
            
        if bracket_selection is None:
            sys.exit(0)     
                
        label = bracket_selection
                
    mode_index = ALL_CHOICES.index(bracket_selection) + 1
                
    return mode_index, top_8_bool