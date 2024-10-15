#!/usr/bin/python3
"""
Has the class MyInt
"""

class MyInt(int):
    """an unconventional take on an integer, ideal for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """
        generates new instance of the class
        """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)
    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other
    def __ne__(self, other):
        """== and != operators inverted"""
        return int(self) == other
