#!/usr/bin/python3
'''Mod inherits_from method'''


def inherits_from(obj, a_class):
    '''Decides if an object is a true subclass of a class'''
    return (isinstance(obj, a_class) and type(obj) != a_class)
