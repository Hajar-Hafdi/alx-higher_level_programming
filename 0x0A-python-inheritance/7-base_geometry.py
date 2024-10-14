#!/usr/bin/python3
'''Mod BaseGeometry class'''

class BaseGeometry:
    '''Represents a BaseGeometry class'''
    def area(self):
        '''Technique for calculating this area'''
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        '''Technique for confirming the value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
