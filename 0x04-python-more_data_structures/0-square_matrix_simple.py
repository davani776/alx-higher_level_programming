#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = []
    for i in matrix:
        sq.append([s**2 for s in i])
    return sq

