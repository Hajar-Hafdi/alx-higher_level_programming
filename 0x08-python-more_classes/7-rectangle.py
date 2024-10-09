#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle

    Attributes:
              number_of_instances (int): The num Rectangle instances
              print_symbol (any): The symbol used for str representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """starts new rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of new rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height
    @property
    def width(self):

