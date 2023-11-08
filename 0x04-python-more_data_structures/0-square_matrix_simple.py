#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lamda submat: list(map(lamda e: e ** 2, submat)), matrix))
