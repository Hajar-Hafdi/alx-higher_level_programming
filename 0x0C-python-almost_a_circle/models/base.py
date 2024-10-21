#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads
import csv

class Base:
    '''Base class for managing unique IDs and serialization.'''

     __object_count = 0

     def __init__(self, id=None):
         '''Initialize a Base object with optional ID.'''
         if id is not None:
             self.id = id
         else:
             Base.__object_count += 1
             self.id = Base.__object_count
    @staticmethod
    def convert_to_json(data):
        '''Convert list of dictionaries to a JSON string'''
        if data is None or not data:
            return "[]"
        return dumps(data)

    @staticmethod
    def parse_json(json_string):
        '''Parse JSON string to a list of dictionaries'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def store_to_file(cls, obj_list):
        '''Save a list of objects to a file in JSON format'''
        if obj_list is not None:
            obj_list = [obj.to_dictionary() for obj in obj_list]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.convert_to_json(obj_list))

    @classmethod
    def create_instance(cls, **attrs):
        '''Create an instance of the class with specified attributes'''
        from models.rectangle import Rectangle
        from models.square import Square
        instance = None
        if cls is Rectangle:
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)
        instance.update(**attrs)
        return instance

    @classmethod
    def load_from_file(cls):
        '''Load instances from a JSON file'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create_instance(**d) for d in cls.parse_json(f.read())]

        @classmethod
        def save_as_csv(cls, obj_list):
            '''Save a list of objects to a CSV file'''
            from models.rectangle import Rectangle
            from models.square import Square
            if obj_list is not None:
                if cls is Rectangle:
                    obj_list = [[o.id, o.width, o.height, o.x, o.y]
                            for o in obj_list]
                else:
                    obj_list = [[o.id, o.size, o.x, o.y]
                            for o in obj_list]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(obj_list)

    @classmethod
    def load_from_file_csv(cls):
        '''Load objects from a CSV file'''
        from models.rectangle import Rectangle
        from models.square import Square
        result_list = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                            "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                            "x": row[2], "y": row[3]}
                result_list.append(cls.create_instance(**d))
        return result_list

    @staticmethod
    def draw_shapes(list_rectangles, list_squares):
        '''Draw rectangles and squares using the turtle module'''
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for shape in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.setpos((shape.x + t.pos()[0], shape.y - t.pos()[1]))
            t.pendown()
            t.pensize(10)
            t.forward(shape.width)
            t.left(90)
            t.forward(shape.height)
            t.left(90)
            t.forward(shape.width)
            t.left(90)
            t.forward(shape.height)
            t.left(90)
            t.end_fill()
        time.sleep(5)
