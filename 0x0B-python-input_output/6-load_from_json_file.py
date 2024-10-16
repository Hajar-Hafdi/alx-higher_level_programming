#!/usr/bin/python3
"""Def JSON file-reading func"""
import json

def load_from_json_file(filename):
    """Makes a Py obj from JSON"""
    with open(filename) as f:
        return json.load(f)
