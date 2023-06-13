#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    neww_list = []

    for x in my_list:
        if x % 2 == 0:
            neww_list.append(True)
        else:
            neww_list.append(False)
    return (neww_list)
