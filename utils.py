"""
This module contains the utils functions to validate user inputs.

It contains the is_num_or_dot, is_valid_number, and is_empty functions.
"""

import re

NUM_OR_DOT_REGEX = re.compile(r"^[0-9.]$")


def is_num_or_dot(string: str) -> bool:
    """
    This function checks if the string is a number or a dot.
    """
    return bool(NUM_OR_DOT_REGEX.search(string))


def is_valid_number(string: str) -> bool:
    """
    This function checks if the string is a valid number.
    """
    try:
        float(string)

        return True

    except ValueError:
        return False


def convert_to_number(string: str) -> int | float:
    """
    This function converts the string to a number.
    """

    number = float(string)

    if number.is_integer():
        number = int(number)

    return number


def is_empty(string: str) -> bool:
    """
    This function checks if the string is empty.
    """
    return not bool(string)
