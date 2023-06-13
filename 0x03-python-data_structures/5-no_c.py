#!/usr/bin/env python3

def no_c(my_string):
    filter_str = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            filter_str += i
    return (filter_str)
