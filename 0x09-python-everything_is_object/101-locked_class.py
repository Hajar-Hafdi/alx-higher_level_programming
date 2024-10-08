#!/usr/bin/python3
"""Define locked class"""

class LockedClass:
    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        self.first_name = first_name
