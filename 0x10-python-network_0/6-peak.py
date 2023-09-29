#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """Finds the peak in a list of integers
    Args:
    list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """

    Length = len(list_of_integers)
    mid = Length
    m = Length // 2
    if Length == 0:
        return None

    while True:
        mid = mid // 2
        if (m < Length - 1 and
                list_of_integers[m] < list_of_integers[m + 1]):
            if mid // 2 == 0:
                mid = 2
            m = m + mid // 2
        elif mid > 0 and list_of_integers[m] < list_of_integers[m - 1]:
            if mid // 2 == 0:
                mid = 2
            m = m - mid // 2
        else:
            return list_of_integers[m]
