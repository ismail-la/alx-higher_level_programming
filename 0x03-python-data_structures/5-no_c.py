#!/usr/bin/python3
def no_c(my_string):
    filtered_chars = [char for char in my_string if char.lower() != 'c']
    return ''.join(filtered_chars)
