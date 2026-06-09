import sys
import os
import questionary
from typing import Optional, Tuple, Any

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
    "11: Prediction 1&2&3&4 vs 5&6&7&8 (View bracket)",
    "12: Custom Bracket Prediction (Manual Selection)"
]

BOOLEAN_CHOICES = [
    "64-16 Bracket",
    "Top 8 Bracket"
]

ALL_CHOICES = SELECT_MODE_CHOICES[:-1] + BRACKET_PREDICTION_CHOICES

def validate_match_input(text: str) -> bool:
    """Ensures input is an integer between 1 and 8."""
    return text.isdigit() and 1 <= int(text) <= 8

def select_mode() -> Optional[Tuple[int, bool, list]]:
    top_8_bool = False
    custom_args = []  
    
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
        
        if label == BRACKET_PREDICTION_CHOICES[-1]:
            arg1 = questionary.text(
                "Enter First Match Number (1-8):",
                validate=validate_match_input
            ).ask()
            if arg1 is None: sys.exit(0)
            
            arg2 = questionary.text(
                "Enter Second Match Number (1-8):",
                validate=validate_match_input
            ).ask()
            if arg2 is None: sys.exit(0)
            
            custom_args = [int(arg1), int(arg2)] 
            
    mode_index = ALL_CHOICES.index(label) + 1
                
    return mode_index, top_8_bool, custom_args