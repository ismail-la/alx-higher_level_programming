#!/usr/bin/env python3
def no_c(my_string):
    filtered_str = [char for char in my_string if char.lower() != 'c']
    return ''.join(filtered_str)
