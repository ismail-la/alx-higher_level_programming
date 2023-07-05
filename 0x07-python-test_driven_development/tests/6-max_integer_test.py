#!/usr/bin/python3
"""to  find the max integer in a list"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
    """

    if len(list) == 0:
        return None
    the_result = list[0]
    x = 1
    while x < len(list):
        if list[x] > the_result:
            the_result = list[x]
        x += 1
    return the_result
