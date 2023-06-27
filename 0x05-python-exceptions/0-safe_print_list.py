#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    """
    sum = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            sum += 1
        except IndexError:
            break
    print()
    return(sum)
