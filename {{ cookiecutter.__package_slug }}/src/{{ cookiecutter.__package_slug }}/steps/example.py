"""This module contains an example function."""

from typing import Union


def nchar(x: str) -> Union[None, int]:
    """This is an example function that counts the number of characters in a string. The docstring is written using the Google convention.
    Args:
        x (str): input string. May be empty.
    Returns:
        Union[None, str]: for an empty string ("") the function will return None. For a non-empty string the function will return an integer indicating the number of characters in the string.
    """
    y: Union[None, int] = None
    if x != "":
        y = len(x)
    return y
