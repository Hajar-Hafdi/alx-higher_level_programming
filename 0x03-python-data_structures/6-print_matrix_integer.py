#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for smatrix in matrix:
        for u in range(len(smatrix)):
                print("{:d}".format(smatrix[u]),
                        end="\n" if u == len(smatrix) - 1 else " ")
        print()
