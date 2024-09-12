#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tot = 0
    for u in range(len(sys.argv) - 1):
        tot += int(sys.argv[u + 1])
    print(tot)
