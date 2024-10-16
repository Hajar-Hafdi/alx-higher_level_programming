#!/usr/bin/python3
"""Outlines string-to-JSON func"""
import json

def to_json_string(my_obj):
    """Outputs JSON representation of a str object"""
    return json.dumps(my_obj)
