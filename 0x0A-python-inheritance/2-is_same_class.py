#!/usr/bin/python3
"""Defines a class-checking function -
Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class -
    Return true if object is an instance of the
    class, otherwise return false
    """
    return (type(obj) == a_class)
