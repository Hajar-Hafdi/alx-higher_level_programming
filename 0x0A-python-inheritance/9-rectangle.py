#!/usr/bin/python3
'''Mod Rectangle class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    '''A subclass that defines a rectangle'''
    def __init__(self, width, height):
        '''constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Technique for calculating area of Rectangle'''
        return self.__width * self.__height
    def __str__(self):
        '''String that represents method'''
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))

