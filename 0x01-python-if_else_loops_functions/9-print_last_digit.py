#!/usr/bin/python3
def print_last_digit(number):
    number = (number if number >= 0 else -number) % 10
    print(number, end="")
    return number
