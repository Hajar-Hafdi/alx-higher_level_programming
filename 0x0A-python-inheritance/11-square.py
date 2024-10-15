#!/usr/bin/python3
'''Mod Rectangle class'''
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    '''A subclass that defines a rectangle'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def area(self):
        '''Technique for area of square'''
        return self.__size ** 2
    def __str__(self):
        '''Returns string depiction of square'''
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
