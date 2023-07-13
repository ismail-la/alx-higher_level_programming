#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """represents a base geometry."""

    def area(self):
        """Not implemented yet"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value (parameter) as an integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
