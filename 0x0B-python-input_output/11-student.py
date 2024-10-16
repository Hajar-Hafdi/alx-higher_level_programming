#!/usr/bin/python3
"""Outlines class Student"""

class Student:
    """Depicts Student"""

    def __init__(self, first_name, last_name, age):
        """Starts new Student

        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: an integer depicting Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Sets a dictionnary depicting Student
        If attrs is a list of strings, represents only those attributes
        included in the list

        Args:
            attrs: attributes to be depicted
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {l: getattr(self, l) for l in attrs if hasattr(self, l)}
        return self.__dict__

    def reload_from_json(self, json):
        """Swap all attributes of the Student
        Args:
           json: key/value pairs to swap attributes with
        """
        for l, v in json.items():
            setattr(self, l, v)
