#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.y = y
        self.x = x
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size value"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size value"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """updates an instance's attributes.
        *args: New attribute values.
        **kwargs: New key pairs of attributes.
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]

            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value

                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the Squaredictionary representation"""

        Dict_obj = {'id': self.id, 'size': self.size, 'x': self.x,
                          'y': self.y}

        return Dict_obj
    
    def __str__(self):
        """Defines a format for the class string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
