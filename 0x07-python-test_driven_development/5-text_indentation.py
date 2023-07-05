#!/usr/bin/python3
"""This module contains a function that indents texts
a function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """prints a text with 2 new lines after each ".", "?", or ":"
    the Args:
        text (str): The string to be printed
    the Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    the_count = 0
    while the_count < len(text) and text[the_count] == " ":
        the_count = the_count + 1

    while the_count < len(text):
        print(text[the_count], end="")
        if text[the_count] == "\n" or text[the_count] in ".?:":
            if text[the_count] in ".?:":
                print("\n")
            the_count = the_count + 1
            while the_count < len(text) and text[the_count] == " ":
                the_count = the_count + 1
            continue
        the_count = the_count + 1
