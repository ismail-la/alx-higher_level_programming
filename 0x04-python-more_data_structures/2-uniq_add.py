#!/usr/bin/python3

def uniq_add(my_list=[]):
    Num = 0
    set_list = set(my_list)

    for x in set_list:
        Num += x
    return (Num)
