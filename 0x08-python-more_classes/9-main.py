#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

the_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(the_square.area(), the_square.perimeter()))
print(the_square)
