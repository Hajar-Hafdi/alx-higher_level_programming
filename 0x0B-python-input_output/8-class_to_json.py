#!/usr/bin/python3
"""Outlines Python class-to-JSON fun"""


def class_to_json(obj):
    """Returns dictionnary rep of simple data struct"""
    return obj.__dict__
