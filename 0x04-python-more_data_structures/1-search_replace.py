#!/usr/bin/python3

def search_replace(my_list, search, replace):
    New_list = my_list[:]
    for x in range(len(New_list)):
        if New_list[x] == search:
            New_list[x] = replace
    return (New_list)
