#!/usr/bin/python3
""" a function that prints a text with 2 new lines after 
each of these characters: ., ? and :
"""


def print_square(size):

    """Print square with the # character.
    the Args:
        size (int): The height/width of the square.
    the Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
