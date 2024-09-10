#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dt = number % 10 if number > 10 else number % -10
print(
        "Last digit of {:d} is {:d} and is "
        .format(number, dt), end="")
if dt > 5:
    print("greater than 5")
elif dt == 0:
    print("0")
else:
    print("Less than 6 and not 0")
