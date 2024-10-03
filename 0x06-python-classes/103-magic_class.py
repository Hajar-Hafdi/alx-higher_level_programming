#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode given by ALX"""

import math

class MagicClass:
    """depicts a circle"""

    def __init__(self, radius=0):
        """start a MagicClass"""
        self.__radius = 0
        if type (radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """depicts the area of MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return circumference of MagicClass"""
        return (2 * math.pi * self.__radius)
