#!/usr/bin/python3
'''Module for lookup method.'''

def lookup(obj):
    '''Looks up object attributes and methods.

    Args:
        obj: the object to list

    Returns:
        list: list of attributes
    '''
    return dir(obj)
