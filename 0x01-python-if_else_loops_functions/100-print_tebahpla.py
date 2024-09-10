#!/usr/bin/python3
for bt in range(ord('z'), ord('a') - 1, -1):
    if bt % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(bt - diff)), end=")
