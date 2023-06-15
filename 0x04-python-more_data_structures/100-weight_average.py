#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    Denom = 0
    nbr = 0

    for tup in my_list:
        nbr += tup[0] * tup[1]
        Denom += tup[1]
    weighted_avr = nbr / Denom
    return (weighted_avr)
