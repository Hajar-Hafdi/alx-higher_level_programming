#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda smat: list(map(lambda u: u**2, smat)), matrix))
