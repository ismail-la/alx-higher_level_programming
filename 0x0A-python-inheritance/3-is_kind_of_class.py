#!/usr/bin/python3
""" Defines a class and inherited class-checking function -
checks if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class -
    returns true if object is an instance of a class
    or a class that the class in question inherits from
    """

    return (isinstance(obj, a_class))
