#!/usr/bin/python3
"""Outline class Student"""

class Student:
    """Depict student"""

    def __init__(self, first_name, last_name, age):
        """Starts new Student

        Args: 
            first_name: first name of the student
            last_name: last name of the student
            age: int represting age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Set dictionnary depicting Student

        If attrs is a list of strings, represents only those attributes
        included in the list

        Args:
            attrs: attributes to be represented
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {l: getattr(self, l) for l in attrs if hasattr(self, l)}
        return self.__dict__
