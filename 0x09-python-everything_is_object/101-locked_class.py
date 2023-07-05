type#!/usr/bin/python3
"""locked class"""


class LockedClass:

    """
    Only allows instatiation of an attribute called first_name.
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
