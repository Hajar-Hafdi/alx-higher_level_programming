#!/usr/bin/python3
"""Outlines class Student"""


class Student:
    """Depict a student"""

    def __init__(self, first_name, last_name, age):
        """Starts new Student
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: an integer representing age of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """set dictionnary rep of Student"""
        return self.__dict__
