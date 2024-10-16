#!/usr/bin/python3
# 6-from_json_string.py
"""Outlines JSON-to-object function"""
import json

def from_json_string(my_str):
    """Returns Python object representation of a JSON str"""
    return json.loads(my_str)
