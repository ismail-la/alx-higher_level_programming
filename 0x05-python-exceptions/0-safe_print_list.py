#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print the x elememts of a list.
    """
    try:
        sum = 0
        for i in range(x):
            print(my_list[i], end="")
            sum += 1
        print()
        return sum
    except IndexError:
        print()
        return sum
