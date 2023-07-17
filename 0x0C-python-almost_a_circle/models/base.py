 #!/usr/bin/python3
"""This module contains a base model class"""

import turtle
import csv
import json
import os


class Base:
    """Base of all classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ New base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.
        list_dictionaries : a liste of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation of a list to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of JSON string representations (json_string)"""
        JSON_STRING_list = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            JSON_STRING_list = json.loads(json_string)

        return JSON_STRING_list
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        **dictionary : key pairs of attribues to initialize.
        """
        if cls.__name__ == 'Rectangle':
            New_dommy = cls(1, 1)
        elif cls.__name__ == 'Square':
            New_dommy = cls(1)

        New_dommy.update(**dictionary)
        return New_dommy
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances or
        a classes instantiated from a file of JSON strings.
        """
        file_name = cls.__name__ + ".json"
        List_intances = []
        list_dictionaries = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as File:
                Str = File.read()
                list_dictionaries = cls.from_json_string(Str)
                for dictionary in list_dictionaries:
                    List_intances.append(cls.create(**dictionary))
        return List_intances
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Create a file by serializing a list of objects in CSV format.
        list_objs: A list of inherited Base instances.
        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        """Files are deserialized into CSV format"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw rectangles and squares, using the turtle module.
        list_rectangles: A list of Rectangle objects to draw.
        list_squares: A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")
        turt.color("#ffffff")

        for Rec in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(Rec.x, Rec.y)
            turt.down()

            for i in range(2):
                turt.forward(Rec.width)
                turt.left(90)
                turt.forward(Rec.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for Squa in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(Squa.x, Squa.y)
            turt.down()
            for i in range(2):
                turt.forward(Squa.width)
                turt.left(90)
                turt.forward(Squa.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
