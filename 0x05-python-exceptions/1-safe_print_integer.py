#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print(f"{value}")
            return (True)
        return (False)
    except Exception:
        return (False)