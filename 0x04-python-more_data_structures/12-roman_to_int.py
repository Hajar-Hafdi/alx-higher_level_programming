#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    tot = 0
    ber = 0
    dgts = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
    for rv in reversed(roman_string):
        ber = dgts[rv]
        tot += ber if tot < ber * 5 else -ber
    return tot
