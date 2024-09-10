#!/usr/bin/python3
for u in range(10):
    for k in range(u, 10):
        if u < k:
            print("{:d} {:d}".format(u, k),
                    end="\n" if u == 8 and k == 9 else ", ")
