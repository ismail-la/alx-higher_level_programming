#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    Delet_key = []

    for key in a_dictionary:
        if a_dictionary[key] == value:
            Delet_key.append(key)

    for key in Delet_key:
        del a_dictionary[key]

    return a_dictionary
